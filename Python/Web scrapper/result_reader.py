import json
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def main():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "PsyTests"

    sheet.append(["Record", "URL", "Результат теста", "Table", "Row"])
    max_cells = 0

    with Path("results_fixed.jsonl").open(encoding="utf-8") as source:
        for record_number, line in enumerate(source, start=1):
            if not line.strip():
                continue

            result = json.loads(line)
            prefix = [record_number, result["url"], result["result_text"]]
            tables = [table for table in result.get("blank_tables", []) if table]

            if not tables:
                sheet.append(prefix + [None, None])
                continue

            for table_number, table in enumerate(tables, start=1):
                for row_number, cells in enumerate(table, start=1):
                    sheet.append(prefix + [table_number, row_number, *cells])
                    max_cells = max(max_cells, len(cells))

    for index in range(1, max_cells + 1):
        sheet.cell(row=1, column=5 + index, value=f"Cell {index}")

    # Keep scraped strings as literal text, including cells beginning with "=".
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            if isinstance(cell.value, str):
                cell.data_type = "s"

    sheet.freeze_panes = "D2"
    sheet.auto_filter.ref = sheet.dimensions
    sheet.column_dimensions["B"].width = 45
    sheet.column_dimensions["C"].width = 55
    for column in range(6, 6 + max_cells):
        sheet.column_dimensions[get_column_letter(column)].width = 22

    workbook.save("results.xlsx")
    print("Loaded to results.xlsx")


if __name__ == "__main__":
    main()