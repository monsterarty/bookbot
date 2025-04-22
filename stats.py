

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def char_count_sorted(text):
    char_dict = char_count(text)
    my_list = []

    for key, value in char_dict.items():
        if key.isalpha():
            my_list.append({"name":key, "num":value})
    return sorted(my_list, key=lambda x: x["num"], reverse=True)

