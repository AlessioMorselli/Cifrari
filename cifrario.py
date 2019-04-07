import re
import operator
from collections import OrderedDict

class Cifrario:
    def __init__(self, method):
        self.method = method
        self.dictionary = []
        with open("dizionario.txt", "r") as f:
            for line in f.readlines():
                self.dictionary.append(line[:-1])
        
        self.characters = {}
        with open("lettere.txt", "r") as f:
            alfabeto = "abcdefghijklmnopqrstuvwxyz"
            i = 0
            for line in f.readlines():
                self.characters[alfabeto[i]] = int(line)
                i += 1
        tmp = sorted(self.characters.items(), key=operator.itemgetter(1))
        tmp.reverse()
        self.ordered_characters = dict(tmp)

    def new_method(self, new_method):
        self.method = new_method

    def encipher(self, text, decipher=False):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        new_text = []

        enciphered_alfabeto = self.method.encipher(alfabeto)

        for character in text:
            isUpper = character.isupper()
            character = character.lower()

            if character in alfabeto:
                if not decipher:
                    index = alfabeto.index(character)
                    character = enciphered_alfabeto[index]
                else:
                    index = enciphered_alfabeto.index(character)
                    character = alfabeto[index]

                if isUpper:
                    character = character.upper()

            new_text.append(character)

        return ''.join(new_text)

    def add_to_dictionary(self, line):
        new_words = []
        words = re.split("[^a-zA-Z0-9_òàùèé]", line)

        for word in words:
            word = word.lower()
            if not word == '' and not word in self.dictionary:
                new_words.append(word)
        
        return new_words
    
    def write_new_words(self, words):
        with open("dizionario.txt", "a") as f:
            for word in list(dict.fromkeys(words)):
                f.write(word + "\n")
    
    def count_words(self, line):
        count = 0
        words = re.split("[^a-zA-Z0-9_òàùèé]", line)

        for word in words:
            word = word.lower()
            if word in self.dictionary:
                count += 1
        
        return count
    
    def count_characters(self, line):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto_dictionary = {}
        for c in alfabeto:
            alfabeto_dictionary[c] = 0
        
        for c in line:
            if c.lower() in alfabeto:
                alfabeto_dictionary[c.lower()] += 1
        
        return alfabeto_dictionary

    def compares_characters(self, characters):
        tmp = sorted(characters.items(), key=operator.itemgetter(1))
        tmp.reverse()
        ordered_file_characters = dict(tmp)

        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto_dictionary = {}
        for c in alfabeto:
            alfabeto_dictionary[c] = c

        for c, fc in zip(self.ordered_characters, ordered_file_characters):
            alfabeto_dictionary[c] = fc

        return ''.join(alfabeto_dictionary.values())