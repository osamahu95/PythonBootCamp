import json

def Solution(str):

    reversedStr = ""

    # reversedStr = str[::-1]

    # param1: start position
    # param2: end place excluded
    # param3: step or increment
    for i in range((len(str) - 1), -1, -1):
        reversedStr += str[i]
    
    if(str == reversedStr):
        return True
    else:
        return False


# Opening the json file
file = open('input.json')
words = json.load(file)


for word in words:
    is_palindrome = Solution(word)
    
    if(is_palindrome is True):
        print("Yes")
    else:
        print("No")