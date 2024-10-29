def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # print(get_num_words(text))
    # print(f"{get_num_words(text)} words found in the document")
    chars_dict = get_chars_dict(text)
    # print(chars_dict)
    #print(print_book_report(text))
    # chars_dict.sort(reverse=False, key=sort_on)
    # chars_dict.items()
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(get_num_words(text))+ " words found in the document")
    print()
    # print(sorted(chars_dict.items()))
    # print(print_book_report(text))
    print_book_report(text)
    # print(chars_dict.items())
    # print(chars_dict)
    print("--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return sorted(chars.items())    

   

def print_book_report(text):
        chars_dict = get_chars_dict(text)
        for char in chars_dict:
            line = (f"The '{char[0]}' character was found {char[1]} times")
            print(line)

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(chars_dict):
    return chars_dict["num"]


def get_num_words(text):
    words = text.split()
    return len(words)



main()
