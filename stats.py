from typing import TypedDict

class CharacterCount(TypedDict):
    char : str
    num : int


def count_words(text : str) -> int:
    words = text.split()
    return len(words)


def letter_count(text : str) -> dict[str, int]:
    letter_counts = {}
    text = text.lower()
    
    for char in text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

def sorting(items):
    return items["num"]

def dict_sort(letters : dict[str, int]) :
    list_of_dict = []
    for letter in letters:
        modified_dict = {"char" : letter , "num" : letters[letter]}
        list_of_dict.append(modified_dict)
    list_of_dict.sort(reverse = True, key = sorting)
    return list_of_dict

