from helpers import alphabet_position

def rotN(message, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet * 2
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_upper = alphabet_upper * 2
    result = ""
    for char in message:
        if char is not char.isalpha():
            result += char
        if char.isupper():
            char_idx= alphabet_upper.find(char)
            rot_idx = char_idx + rot
            result += alphabet_upper[rot_idx]
        if char.islower():
            char_idx= alphabet_position(char)
            rot_idx = char_idx + rot
            result += alphabet[rot_idx]
    return result
        

def main():
    from sys import argv,exit
    if argv[1].isdigit() == True:
        message = input("Type a message:")
        argv[1] = int(argv[1])
        print(rotN(message, argv[1]))  
    else:
        exit("usage: python caesar.py n, n must be an interger")
if __name__ == "__main__":
    main()


