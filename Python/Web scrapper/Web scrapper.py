import json
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

import re
from urllib.parse import parse_qs, quote, urljoin, urlsplit

from playwright.sync_api import Error as PlaywrightError, sync_playwright

#==================== №, Вопрос, Выбранный ответ. ====================#

def build_question_table(form):
    rows = []
    option_count = 0

    for question in form.select(".bl2 > .bl2Q"):
        text = " ".join(question.get_text(" ", strip=True).split())
        match = re.match(r"^(\d+)\.\s*(.*)$", text)
        number, prompt = match.groups() if match else (str(len(rows) + 1), text)

        choices = question.find_next_sibling()
        options = []
        if choices is not None and "bl2Q" not in choices.get("class", []):
            options = choices.select(".bl2AA")

        marks = [
            "✓" if "bl2ASel" in option.get("class", []) else ""
            for option in options
        ]
        option_count = max(option_count, len(marks))
        rows.append([number, prompt, *marks])

    if not rows:
        return []

    header = ["№", "", *(str(i) for i in range(1, option_count + 1))]
    return [header, *rows]

#===================== Load blank tables =====================#
def load_blank_tables(page, html, result_url):
    token = parse_qs(urlsplit(result_url).query).get("b", [""])[0]
    if not token:
        return []

    soup = BeautifulSoup(html, "html.parser")
    # Prefer the completed answer-sheet link supplied by the result page.
    for link in soup.find_all("a", href=True):
        label = " ".join(link.get_text(" ", strip=True).split()).casefold()
        if label == "бланк" and token in urlsplit(link["href"]).query:
            form_url = urljoin(result_url, link["href"])
            break
    else:
        # The standalone form URL verified for the GDS-15 example.
        # if not parse_qs(urlsplit(result_url).query).get("v", [""])[0].startswith("derG"):
        #     raise ValueError("Could not find the completed «Бланк» link")
        # form_url = urljoin(result_url, "/depr/gds15-bl.html?" + quote(token, safe=""))
        # build_question_table handle
        result_code = parse_qs(urlsplit(result_url).query).get("v", [""])[0]
        form_paths = {
            "derG": "/depr/gds15-bl.html",
            "vozG": "/life/gviz-bl.html",
        }
        form_path = form_paths.get(result_code[:4])
        if form_path is None:
            raise ValueError("Could not find the completed «Бланк» link")

        form_url = urljoin(result_url, form_path + "?" + quote(token, safe=""))

    page.goto(form_url, wait_until="domcontentloaded", timeout=20_000)
    page.wait_for_function(
        r"""() => document.querySelector('.bl2AA.bl2ASel') !== null ||
            [...document.querySelectorAll('.blGR [id^="q"]')].some(
                cell => /^q\d+a\d+$/.test(cell.id) && cell.textContent.trim()
            )""",
        timeout=10_000,
    )

    form = BeautifulSoup(page.content(), "html.parser")
    tables = []
    for grid in form.select(".blGR"):
        rows = []
        row = []
        for cell in grid.find_all("div", recursive=False):
            classes = cell.get("class", [])
            if "blQN" in classes and row:
                rows.append(row)
                row = []
            if {"blQH", "blQN", "blQ"}.intersection(classes) or re.fullmatch(
                r"q\d+a\d+", cell.get("id", "")
            ):
                row.append(cell.get_text(" ", strip=True))
        if row:
            rows.append(row)
        if rows:
            tables.append(rows)

    if not tables:
        question_table = build_question_table(form)
        if question_table:
            tables.append(question_table)

    if not tables:
        raise ValueError("Could not parse the completed «Бланк»")

    return tables


HEADINGS = ("h1", "h2", "h3", "h4", "h5", "h6")

#===================== Export page =====================#

def heading_text(tag):
    text = " ".join(tag.get_text(" ", strip=True).split())
    return text.rstrip("▾▸▴▼▲▶ ").casefold()

def section_elements(soup, title):
    heading = next(
        (
            tag for tag in soup.find_all(HEADINGS)
            if heading_text(tag) == title.casefold()),
        None,
    )
    if heading is None:
        return

    for element in heading.next_elements:
        if heading in element.parents:
            continue
        if isinstance(element, Tag) and element.name in HEADINGS:
            if HEADINGS.index(element.name) <= HEADINGS.index(heading.name):
                break
        yield element


def parse_page(html, url):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select("script, style, template, noscript"):
        tag.decompose()

    result_text = " ".join(
        element.strip()
        for element in section_elements(soup, "Результат теста")
        if isinstance(element, NavigableString) and element.strip()
    )
    if not result_text:
        raise ValueError("Could not find text under «Результат теста»")

    blank_tables = []
    for element in section_elements(soup, "Бланк"):
        if isinstance(element, Tag) and element.name == "table":
            rows = [
                [cell.get_text(" ", strip=True)
                 for cell in row.find_all(["th", "td"], recursive=False)]
                for row in element.find_all("tr")
                if row.find_parent("table") is element
            ]
            blank_tables.append(rows)

    return {
        "url": url,
        "result_text": result_text,
        "blank_tables": blank_tables,
    }


def main():
    with (
        Path("urls.txt").open(encoding="utf-8-sig") as links,
        Path("results_fixed.jsonl").open("a", encoding="utf-8") as output,
        requests.Session() as session,
        sync_playwright() as playwright,
    ):
        browser = playwright.chromium.launch()
        try:
            page = browser.new_page()

            for line in links:
                url = line.strip()
                if not url:
                    continue

                try:
                    response = session.get(url, timeout=20)
                    response.raise_for_status()
                    result = parse_page(response.content, url)
                except (requests.RequestException, ValueError) as error:
                    print(f"{url}: result page: {error}", file=sys.stderr)
                    continue

                if not result["blank_tables"]:
                    try:
                        result["blank_tables"] = load_blank_tables(
                            page, response.content, response.url
                        )
                    except (PlaywrightError, ValueError) as error:
                        print(f"{url}: «Бланк»: {error}", file=sys.stderr)

                output.write(json.dumps(result, ensure_ascii=False) + "\n")
                output.flush()

                table_count = len(result["blank_tables"])
                print(f"Saved {url} ({table_count} answer-sheet tables)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()