def alphabet_position(letter):
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphabet:
        return alphabet.index(letter)

def rotate_character(char, rot):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        position = alphabet_position(char)
        character_position = position + rot % 26
        return str(alphabet.find(character_position))

print(rotate_character('k', 13))
