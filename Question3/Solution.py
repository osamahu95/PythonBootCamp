import re
import wikipediaapi

def Solution(str):

    uppercase_count = 0
    lowercase_count = 0

    uppercase_regex = "[A-Z]"
    lowercase_regex = "[a-z]"

    for char in str:
        if(re.search(uppercase_regex, char) is not None):
            uppercase_count+=1

        if(re.search(lowercase_regex, char) is not None):
            lowercase_count+=1

    return [uppercase_count, lowercase_count]        

wiki = wikipediaapi.Wikipedia('en')
page = wiki.page('Allah')

if(page.exists()):
    sol_arr = Solution(page.summary)
    print(f"Uppercase Chars: {sol_arr[0]}")
    print(f"Lowercasecase Chars: {sol_arr[1]}")
else:
    print("Page does not exists")