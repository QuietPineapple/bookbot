def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        text = f.read()
        wc = word_count(text)
        cc = character_count(text)
        report(book, wc, cc)

def word_count(text):
    text_list = text.split()
    return len(text_list)

def character_count(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def report(book, word_count, char_dict):
    report = f"--- Begin report of {book} --- {word_count} words found in the document"
    for char in char_dict:
        if char.isalpha():
            report += f" The {char} was found {char_dict[char]} times."
    
    print(report)
    

main()