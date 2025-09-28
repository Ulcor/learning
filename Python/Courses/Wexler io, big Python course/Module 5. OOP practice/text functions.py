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
    # poem_normalized = poem.strip()

    # rows = poem_normalized.split('\n')
    # keys = str()
    # rows = str(rows)
    # values = poem.split(":', '- ")
    # rows_2 = str(rows)
    # values_2 = rows_2.split("!")

    res = {}
    animal = None

    for rows in poem.split('\n'): # print row by row
        if not rows:
            continue
        if animal is None:
            animal = rows.split(' ')[0] # first word
            # print(f'Животное: {animal}')
        elif rows.startswith('-'):
            rows = rows.replace('-', ' ').replace('!', '').strip()
            rows = rows.split(',')
            rows = rows[0]
            # print(f'Звук: {rows}')

            # Write animal and sound
            res[animal] = rows

            # Continue to a new
            animal = None




    return res


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
print(res)