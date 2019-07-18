import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if yes, or N if no : " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't Exist. Please double check it !!!"
        else:
            return "We did not understand your input please try again !!!"

    else:
        return "The word doesn't Exist. Please double check it !!!"


print("Welcome to the Riyaz's Dictionary!!!")

while True:

    print("Enter Q to exit the dictionary")
    word = input("Enter the word: ")
    if word == "Q":
        break
    else:
        output =(translate(word))
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

print("Closing the Dictionary Bye Bye!!!!!!")