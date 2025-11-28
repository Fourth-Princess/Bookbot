def sorted_char(book):
    dictionary = get_char(book)
    alist = sorted(dictionary.items(), reverse=True, key=lambda item: item[1])
    for key in alist:
        if key[0].isalpha():
            print(f"{key[0]}: {key[1]} ")
        



def get_char(book):
    text = get_book_text(book).lower()
    characters = {"q": 0}
    for char in text:
        if char in characters:
             characters[char] += 1
        else :
            characters[char] = 1
    return characters        
    
    
def get_num_words(book):
    text = get_book_text(book)
    words = text.split()
    words_total = len(words)
    print(f"Found {words_total} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
