x = input("enter string :")


def isPalindrome(x):
    return x == x[::-1]

ans = isPalindrome(x)
if ans:
	print("Yes")
else:
	print("No")
