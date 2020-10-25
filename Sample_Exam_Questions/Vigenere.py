class Vigenere:

    def __init__(self, key):
        self.key = key

    # no self
    def _char_to_number(char):
        return ord(char) - 96

    # no self
    def _number_to_char(number):
        return chr(number + 96)

    def encrypt(self, text):
        letters = []
        j = 0
        text = text.lower()
        for i in text:
            letter_ascii = Vigenere._char_to_number(i)
            key_ascii = Vigenere._char_to_number(self.key[j % len(self.key)])
            letters.append(Vigenere._number_to_char((letter_ascii + key_ascii) % 26))
            j += 1
        return "".join(letters)

    def decrypt(self, text):
        letters = []
        j = 0
        text = text.lower()
        for i in text:
            letter_ascii = Vigenere._char_to_number(i)
            key_ascii = Vigenere._char_to_number(self.key[j % len(self.key)])
            letters.append(Vigenere._number_to_char((letter_ascii - key_ascii) % 26))
            j += 1
        return "".join(letters)
