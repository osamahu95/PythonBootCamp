import json


import string

# provides the solution in constant time O(1)
# def Solution(str):
#     alphabets = set(string.ascii_lowercase)
#     sentence = str.lower()     
#     return set(sentence) >= alphabets


# provides the solution in Linear time O(n)
def Solution(str):
    sentence = set(str.lower())

    counts = 0
    alphabets = set(string.ascii_lowercase)

    for char in sentence:
        if(char in alphabets):
            counts+=1
    
    if(counts >= len(alphabets)):
        return True
    else:
        return False

file = open("inputset.json")
inputs = json.load(file)

for input in inputs:
    is_pangram = Solution(input)
    if(is_pangram is True):
        print("Panagram")
    else:
        print("Not Panagram")