def get_initials(fullname):
    upper_fullname = fullname.upper()
    list_upper = upper_fullname.split()
    initials = ''
    for first_letter in list_upper:
        first_letter = first_letter[0]
        initials += first_letter
    return initials



def main():
    initials = get_initials(input("What is your full name?"))
    print(initials)

if __name__ == '__main__':
    main()
