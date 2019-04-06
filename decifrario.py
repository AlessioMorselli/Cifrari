import sys
import re


def decipher(text, offset):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto = list(alfabeto)

    text_list = list(text)
    new_text = []

    for character in text_list:
        isUpper = character.isupper()
        character = character.lower()

        if character in alfabeto:
            index = alfabeto.index(character)
            index -= offset
            if index < 0:
                index += 26
            
            character = alfabeto[index]
            if isUpper:
                character = character.upper()

        new_text.append(character)


    return ''.join(new_text)


def count_words(words, dictionary):
    count = 0
    for word in words:
        word = word.lower()
        if word in dictionary:
            count += 1
    
    return count


dictionary = []
with open("dizionario.txt", "r") as f:
    for line in f.readlines():
        dictionary.append(line[:-1])

max_count = 0
right_offset = -1
deciphered_text = ''

for offset in range(1, 25):
    attempt_text = ''
    new_lines = []
    count = 0
    i = 0

    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            i += 1
            new_lines.append(decipher(line, offset))
            count += count_words(re.split("[^a-zA-Z0-9_]", new_lines[-1]), dictionary)
            if i > 20:
                break
    
    
    print("Offset: " + str(offset) + " - Count: " + str(count))
    if count > max_count:
        max_count = count
        right_offset = offset

deciphered_lines = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        deciphered_lines.append(decipher(line, right_offset))
    
    deciphered_text = ''.join(deciphered_lines)

with open(sys.argv[2], "w") as f:
    f.write(deciphered_text)

