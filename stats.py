def word_count(book):
    word_list = book.split()
    return len(word_list)

def char_count(book):
    book = book.lower()
    char_dict = {}
    for char in book:
        if char in char_dict:
            char_dict[char] += 1
            continue
        char_dict[char] = 1
    return char_dict

def sort_on(entries):
    return entries["num"]

def sort_dict(dict):
    dict_list = []
    for entry in dict:
        char_dict = {}
        num = dict[entry]
        char_dict["char"] = entry
        char_dict["num"] = num
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list