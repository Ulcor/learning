# Simple and good
# my_string = "AABBCC"
# char_list = list(my_string)
# print(char_list)

# With cycle, manual, for garbage interviews
my_string = "AABBCC"
char_list = []

for items in my_string:
    for character in items:
        char_list.append(character)

print(char_list)


