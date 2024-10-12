import json

# more efficient solution
# This function runs the given input to O(sqrt(n)) times
# Reference Help: https://www.geeksforgeeks.org/perfect-number/

# def Solution(num):
#     sum = 1

#     iter = 2
#     while(iter * iter <= num):
#         if(num%iter == 0):
#             if(iter*iter != num):
#                 sum = sum + iter + num/iter
#             else:
#                 sum +=iter
#         iter+=1
    
#     if (sum == num):
#         return True
    
#     return False

# Less Efficient Solution
# This function runs the given input to O(n) times

def Solution(num):
    nums = []

    for i in range(1, num):
        if(num%i == 0):
            nums.append(i)
    
    if(num == sum(nums)):
        return True
    else:
        return False

file = open("input.json")
numbers = json.load(file)

for number in numbers:
    is_perfect = Solution(number)

    if(is_perfect is True):
        print("Perfect")
    else:
        print("Not Perfect")