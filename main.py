def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        print("--- Begin report of books/frankenstein.txt ---")
        
        # Prints the amount of words
        words = count(file_contents)
        print(f"{words} words found in the document")
        
        # Prints a dictionary of the amount of characters in the book
        word_dict = amount_char(file_contents)
        
        # Sorts and prints each character and its count
        sorted_chars = sort_on(word_dict)
        for item in sorted_chars:
            print(f"The '{item['character']}' character was found {item['count']} times.")
        
def sort_on(char_counts):
    list_of_dicts = []
    for char, count in char_counts.items():
        list_of_dicts.append({"character": char, "count": count})
    list_of_dicts.sort(key=lambda item: item["count"], reverse=True)
    return list_of_dicts
        
def count(text):
    words = text.split()
    return len(words)

def amount_char(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():  # Ensure only alphabetic characters are counted
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    return characters

main()