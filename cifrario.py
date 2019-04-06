import sys
import re


def encipher(text, offset):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto = list(alfabeto)

    text_list = list(text)
    new_text = []

    for character in text_list:
        isUpper = character.isupper()
        character = character.lower()

        if character in alfabeto:
            index = alfabeto.index(character)
            index += offset
            while index > 25:
                index -= 26
            
            character = alfabeto[index]
            if isUpper:
                character = character.upper()

        new_text.append(character)


    return ''.join(new_text)


def add_to_dictionary(line, dictionary):
    new_words = []
    words = re.split("[^a-zA-Z0-9_òàùèé]", line)

    for word in words:
        word = word.lower()
        if not word == '' and not word in dictionary:
            new_words.append(word)
    
    return new_words


dictionary = []
with open("dizionario.txt", "r") as f:
    for line in f.readlines():
        dictionary.append(line[:-1])

if not int(sys.argv[2]):
    print("Il secondo argomento deve essere un intero!")

offset = int(sys.argv[2])
new_lines = []
new_words = []

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        new_words += add_to_dictionary(line, dictionary)
        new_lines.append(encipher(line, offset))

with open(sys.argv[3], "w") as f:
    for line in new_lines:
        f.write(line)

with open("dizionario.txt", "a") as f:
    for word in list(dict.fromkeys(new_words)):
        f.write(word + "\n")

