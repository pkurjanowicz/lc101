def count(string):
  lcDict= {}
  for letter in string:
    if letter in lcDict:
      lcDict[letter] +=1
    else:
      lcDict[letter]= 1
  string1 = ""
  for letter in lcDict.keys():
    value = letter+":"+str(lcDict[letter])
    string1 += value + "\n"
  return string1


def main():
    print(count("Hi there"))

main()