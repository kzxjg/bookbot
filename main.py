from stats import word_count, letter_count, sorted_letters # type: ignore
import sys


if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

arg1 = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        file_string = file.read()
        return(file_string)


def main():
    text = get_book_text(arg1)
    letters = letter_count(text)
    letters_sorted = sorted_letters(text)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {letters}...')
    print('----------- Word Count ----------')
    print(f"Found {word_count(text)} total words")
    print('--------- Character Count -------')
    
    for i in letters_sorted:
        print(f"{i['letter']}: {i['count']}")

    print('============= END ===============')


if __name__ == '__main__':
    main()
