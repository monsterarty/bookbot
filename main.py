from stats import word_count

def get_book_text():

    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read()
        return file_content
    


print(f"{word_count(get_book_text())} words found in the document")