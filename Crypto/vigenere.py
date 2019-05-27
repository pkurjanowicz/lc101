from helpers import alphabet_position

def key(key_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot_amount_list = []
    for char in key_string:
        char_index = alphabet.find(char)
        rot_amount_list.append(char_index)
    return rot_amount_list

def rotN(message, key_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_upper = alphabet_upper * 2
    alphabet = alphabet * 2
    key_index = key(key_string)
    key_index = key_index * 20
    result = ""
    key_place = 0
    for char in message:
        key_index_amount = key_index[key_place]
        if char == "," or char == "!" or char == " ":
            result += char
            key_place += 0
        if char.isupper() == True:
            char_idx= alphabet_upper.find(char)
            rot_idx = char_idx + key_index_amount
            result = result + alphabet_upper[rot_idx]
            key_place += 1
        if char.islower() == True:
            char_idx= alphabet_position(char)
            rot_idx = char_idx + key_index_amount
            result = result + alphabet[rot_idx]
            key_place += 1
    return result

def main():
    from sys import argv, exit
    if argv[1].isalpha() == True:
        input_message = input("Please put your message here: ")
        print(rotN(input_message,argv[1]))
    else:
        exit("""usage: python vigenere.py keyword
            Arguments:
            -keyword : The string to be used as a "key" to encrypt your message. 
            Should only contain alphabetic characters-- no numbers or special characters.""")

if __name__ == "__main__":
    main()

