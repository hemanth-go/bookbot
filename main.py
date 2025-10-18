import sys
from stats import count_words,count_characters,sort_dict
def get_book_text(fi):
    with open(fi) as f:
        contents=f.read()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    word_count=count_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count=count_characters(contents)
    sorted_characters=sort_dict(character_count)
    for ch in sorted_characters:
        print(f"{ch["char"]}: {ch["num"]}")
    print("============= END ===============")
    


    #print(character_count)
    

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(sys.argv[1])
        #print(sys.argv)
    #print(out)



main()
