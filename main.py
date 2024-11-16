# Read frankenstein project First proj
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    count_letters = same_letters_count(text)
    count_letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter in count_letters:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")
    print("--- End report ---")
    

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def same_letters_count(text):
    word_dict = {}
    lower_words = text.lower()
    letter_list = []
    for word in lower_words:
        if word.isalpha():
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    for letter, count in word_dict.items():
        new_dict = {"name": letter, "num": count}
        letter_list.append(new_dict)

    return letter_list

def sort_on(letter_list):
    return letter_list["num"]

main()
    


