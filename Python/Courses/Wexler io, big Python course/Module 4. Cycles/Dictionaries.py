my_dict = dict()

def add_to_dictionary(diction: dict, added_word: str, translation_en: str):
    diction.get(added_word, translation_en) # Same as if/else logic
    diction[added_word] = translation_en


def translate(diction: dict, word: str):
    # return diction[word]  # this is a key. Will return value
    # return diction.get(word)  # same but with None handling
    # if diction.get(word) is None:  # Same but prints exactly what happened in case of None
    #     return f"Слово {word} не найдено"
    # else:
    #     return diction.get(word)
    return diction.get(word, f"Слово {word} не найдено")  # Same but in 1 row


dictionary = {}  # задаём пустую переменную
add_to_dictionary(dictionary, "Масло", "Butter")  # Вызываем вашу функцию

print(dictionary)  # Будет содержать  {"Масло": "Butter"}

translation = translate(dictionary, "Масло")
print(translation)   # Будет содержать "Butter"

def get_words(diction: dict):
    return diction.keys()

print(get_words(dictionary))

def get_translations(diction: dict):
    return diction.values()

print(get_translations(dictionary))

def get_entries(diction: dict):
    return diction.items()

print(get_entries(dictionary))