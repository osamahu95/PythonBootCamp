import json


# Returns the Solution at Constant Time O(1)
# def Solution(list):
#     return set(list)

# Returns the Solution at Linear Time O(n)
def Solution(list):
    newList = []

    for element in list:
        if(element not in newList):
            newList.append(element)
    
    return newList


f = open("input.json")
inputs = json.load(f)

for input in inputs:
    arr = Solution(input)
    print(arr)