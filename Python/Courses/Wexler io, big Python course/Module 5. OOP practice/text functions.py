# Text with a comma separator
def get_list_of_groceries(text: str):
    groceries = text.split(',')
    for grocery in groceries:
        print(grocery)

text_sample = """Молоко,Яйца,Сахар,Соль"""

get_list_of_groceries(text_sample)

# extra character
def get_list_of_groceries(text: str):
    groceries = text.split(', ')
    for grocery in groceries:
        print(grocery.strip())

text_sample = """Молоко, Яйца, Сахар, Соль"""

get_list_of_groceries(text_sample)

# Is palindrome. Works for str and list
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome(list('hello')))

# Simple poem parser
def parse_poem(poem: str):

    # print(poem)
    poem_normalized = poem.strip()
    dictionary = {}
    rows = poem_normalized.split('\n')
    keys = str()
    rows = str(rows)
    values = poem.split(":', '- ")
    rows_2 = str(rows)
    values_2 = rows_2.split("!")

    print(values)
    for words in values_2:
        print(words)

        # for keys in words:
        #     print(words)


poem = """
Свинки замяукали:
- Мяу, мяу!
Кошечки захрюкали:
- Хрю, хрю, хрю!
Уточки заквакали:
- Ква, ква, ква!
Курочки закрякали:
- Кря, кря, кря!
Воробышек прискакал
И коровой замычал:
- Мууу!
"""

res = parse_poem(poem)