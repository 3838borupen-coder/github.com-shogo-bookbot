import sys
from stats import get_num_words, get_num_characters, make_word_frequency_dict

try:

    file_path = sys.argv[1]
    total_num = get_num_words(file_path)    #note: github.com-shogo-bookbot/books
                                        #[frankenstein.txt][mobydick.txt][prideandprejudice.txt]

    num_char = get_num_characters(file_path)
    frequency_list = make_word_frequency_dict(num_char)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(total_num)
    print("--------- Character Count -------")
    print("\n".join(frequency_list))
    print("============= END ===============")

except:
    sys.exit("Usage: python3 main.py <path_to_book>")

#print(sys.argv)
