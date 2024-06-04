def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    num_words = count_words(text)
    chars = get_chars(text)

    generate_report(book_path, num_words, chars)

def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    letters_dict = {}
    for letter in text:
        letter = letter.lower()
        if letters_dict.get(letter) is not None:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def generate_report(file_path, words = 0, chars = {}):
    intro = f"--- Begin report of {file_path} ---"
    words = f"{words} words found in the document"
    print(intro)
    print(words)
    print("\r")

    for char in sorted(chars, key=chars.get, reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")

main()
