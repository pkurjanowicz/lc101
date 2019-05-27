def get_initials(fullname):
    output = ""
    for i in fullname.upper().split():
        output += i[0]
    return output

def main():
    name_input = input("What is your full name?")
    print(get_initials(name_input))
    

if __name__ == "__main__":
    main()