my_dict = dict()

def add_to_dictionary(diction: dict, added_word: str, translation_en: str):
    diction.get(added_word, translation_en) # Same as if/else logic
    diction[added_word] = translation_en


dictionary = {}  # задаём пустую переменную
add_to_dictionary(dictionary, "Масло", "Butter")  # Вызываем вашу функцию

print(dictionary)  # Будет содержать  {"Масло": "Butter"}