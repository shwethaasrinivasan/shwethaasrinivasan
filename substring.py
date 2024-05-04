#String of length N, print all possible substrings
#n*(n+1)/2

def substring(s):
    for i in range(len(s)):
        for j in range(i,len(s)):
            print(s[i:j+1])
#Finding the nth occurrence of a substring within a string: To find the index corresponding to the nth occurrence of a substring within a string, you can use the following Python function:

def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start

# Example usage:
result = find_nth("foofoofoofoo", "foofoo", 2)
print(f"Index of the 2nd occurrence: {result}")

#In the example above, find_nth finds the second occurrence of "foofoo" within the string "foofoofoofoo", and it returns the index 6

#Generating all possible substrings from a given string: To generate all possible substrings of a given string, you can use string slicing. Here’s an example:

def generate_substrings(s: str):
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            res.append(substring)
    return res

# Example usage:
input_string = "hello"
all_substrings = generate_substrings(input_string)
print(all_substrings)

#The output will be a list containing all possible substrings of the string "hello"