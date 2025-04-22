

def get_book_text():

    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read()
        return file_content
    
def word_count(text):
    words = text.split()
    return len(words)

print(f"{word_count(get_book_text())} words found in the document")