def main():
    print_report('books/frankenstein.txt')

# Prints a report to the console based on the provided text
def print_report(path):
    book_text = get_book_text(path)
    letter_count_dict = get_letter_count(book_text)
    letter_count_list = convert_letter_count_dict(letter_count_dict)
    letter_count_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path}---")
    print(f"{get_word_count(book_text)} words found in the document\n")
    
    for c in letter_count_list:
        print(f"The '{c['letter']}' character was found {c['num']} times")
    
    print('--- End report ---')

# Takes a dictionary and returns the value of the "num" key
def sort_on(dict):
    return dict["num"]

# Returns a list of dictionaries containing how many times each character appears
# Used for sorting
def convert_letter_count_dict(dict):
    return_list = []
    for k in dict:
        return_list.append(
            {"letter": k,
             "num" : dict[k]}
        )
    return return_list

# Returns a dictionary containing how many times each character appears
# in the text
def get_letter_count(text):
    return_dict = {}
    for c in text:
        if c.isalpha():
            c_lower = c.lower()
            if c_lower in return_dict:
                return_dict[c_lower] += 1
            else:
                return_dict[c_lower] = 1
    return return_dict

# Returns the number of words in the text
def get_word_count(text):
    words = text.split()
    return len(words)

# Returns the text from a book
def get_book_text(path):
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents

main()
