def get_text(path: str) ->str:
      with open("books/frankenstein.txt") as f:
        return f.read()

def add_char(counter: dict[str, int], char: str) -> None:    
    counter[char] = counter.get(char, 0) + 1 
     
def count_words(imput: str) -> int:
    return len(imput.split())


def main():   
    path = "books/frankenstein.txt"
    text = get_text(path)    
    number = count_words(text)
    character_dictionary = {}
    for char in text:
        #print(char)
        add_char( character_dictionary, char.lower())
    #print(dict)

    keylist = []
    for key in character_dictionary.keys():
        if key.isalpha():
            keylist.append(key)
    keylist.sort()
    for key in keylist:
        print("The '{}' character was found {} times".format(key, character_dictionary[key]))





main()