# Read frankenstein project First proj
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    cou_words = same_words_count(text)
    print(text)
    print("///")
    print(f"{num_words} words found in the document")
    print("///")
    print(cou_words)

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def same_words_count(text):
    word_dict = {}
    lower_words = text.lower()
    for word in lower_words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

        
main()
    


