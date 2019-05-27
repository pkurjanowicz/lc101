def pig_latin(string):
    string = string.lower()
    split_string = string.split()
    pig_latin= ''
    for word in split_string:
        new_word = word[1:]
        pig_latin += new_word + word[:1] + "ay" + ' ' 
    return pig_latin

print(pig_latin(input("What would you like to make into pig latin?")))