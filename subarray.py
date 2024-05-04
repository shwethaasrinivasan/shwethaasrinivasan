from itertools import combinations

def generate_subsets(input_string):
    all_combinations = [''.join(l) for i in range(len(input_string)) for l in combinations(input_string, i + 1)]
    return list(reversed(list(dict.fromkeys(all_combinations))))
all_subsets = generate_subsets("abcde")
print(all_subsets)

#Recursive Approach: We can recursively generate subsets by fixing the first element and recursively finding subsets of the remaining part of the string.
#This recursive approach builds subsets by either including or excluding each character in the string.

def generate_subsets_recursive(input_string, sub="", i=0):
    if i == len(input_string):
        return [sub]
    else:
        # Include the current character
        include_current = generate_subsets_recursive(input_string, sub + input_string[i], i + 1)
        # Exclude the current character
        exclude_current = generate_subsets_recursive(input_string, sub, i + 1)
        return include_current + exclude_current
all_subsets_recursive = generate_subsets_recursive("abcde")
print(all_subsets_recursive)

#Bit Manipulation (Binary Representation): We can use the binary representation of numbers from 0 to (2^n - 1) (where (n) is the length of the string) to generate subsets.
# Each bit position corresponds to whether an element is included or excluded in the subset.
#In this approach, we iterate through all possible numbers from 0 to (2^n - 1), and for each number, we check which bits are set (corresponding to the elements to include).
def generate_subsets_bitwise(input_string):
    n = len(input_string)
    all_subsets = []
    for i in range(2**n):
        subset = [input_string[j] for j in range(n) if (i & (1 << j)) != 0]
        all_subsets.append(''.join(subset))
    return all_subsets

all_subsets_bitwise = generate_subsets_bitwise("abcde")
print(all_subsets_bitwise)

