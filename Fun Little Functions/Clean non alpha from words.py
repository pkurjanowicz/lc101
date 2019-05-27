def is_alpha(word):
    for letter in word:
        new_word = ''.join([letter for letter in word if letter.isalpha()])
    return new_word