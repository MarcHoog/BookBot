def get_word_count(text:str):
    return len(text.split())
    
def get_text(path:str):
    with open(path) as f:
        return f.read()

def get_character_count(text:str):
    
    lower_txt = text.lower()
    characters = {}

    for char in lower_txt:
        if char in characters:
            characters[char] += 1 
        else:
            characters[char] = 1
            
    return characters
    
def report_book(path:str):
    
    text = get_text(path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    
    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    
    sorted_char_count = [{'char': k, 'count': v} for k, v in char_count.items() if k.isalpha()]
    sorted_char_count.sort(reverse=True, key=lambda x : x['count'])
    
    for char in sorted_char_count:
        print(f"The '{char['char']}' character was found {char['count']} times")
        
    print('--- End report ---')
        
    
    
def main():
        book_path = 'books/frankenstein.txt'
        text = get_text(book_path)
        print(get_word_count(text))
        print(get_character_count(text))
        report_book(book_path)
    
        
if __name__ == "__main__":
    main()