from collections import defaultdict

# Check any number of letters in the word
def anagram_iterator(input_list: list):
    groups = defaultdict(list)
    for word in input_list:
        # сортируем буквы и делаем ключ
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(anagram_iterator(["eat","tea","tan","ate","nat","bat"]))

# Check if 1 word = 2 word, written backwards, classic anagram
def isanagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    # print(str1_list, str2_list)  # ['a', 'e', 't'] ['a', 'e', 't']

    return str1_list == str2_list

print(isanagram("eat", "ate"))