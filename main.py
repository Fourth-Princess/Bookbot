import sys
def main():
    if len(sys.argv) == 2 :
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("----------- Word Count ----------")
        from stats import get_num_words
        get_num_words(book)
        print(" --------- Character Count -------")
        from stats import sorted_char
        sorted_char(book)
    else :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    


 
main()
