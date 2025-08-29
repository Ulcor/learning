# Simple and good
# my_string = "AABBCC"
# char_list = list(my_string)
# print(char_list)

# With cycle, manual, for garbage interviews
my_string = "AABBCC"

def string_to_char_list(strng: str):
    char_list = []
    for items in my_string:
        for character in items:
            char_list.append(character)
    return char_list


print(string_to_char_list(my_string))


