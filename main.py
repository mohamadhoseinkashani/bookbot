import sys
from stats import count_words
from stats import letter_count
from stats import dict_sort



def system_repair_and_give_path(another_path : str)-> str :
    sys.argv.append(another_path)
    return another_path


def get_book_text(book_path : str) -> str:
    file_content = ""
    with open(book_path) as f:
        file_content = f.read()
    return file_content






if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = system_repair_and_give_path(sys.argv[1])
    book_text = get_book_text(book_path)
    
    num_of_words = count_words(book_text)
    words = letter_count(book_text)
    sorted_words = dict_sort(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for s_letter in sorted_words:
        the_letter = s_letter["char"]
        the_number = s_letter["num"]
        if the_letter.isalpha():
            print(f"{the_letter}: {the_number}")
        
    print("============= END ===============")


    
    

