def num(N: int) -> int:
    return [i for i in range(1, N+1) if N % i == 0]

N = 36
res = num(N)
cnt = len(res)
print(f"Factorial of {N} is {res} and the count is {cnt}")

from typing import List
def factors(N:int) -> [List[int],int]:
    cnt = 0
    nums = []
    for i in range(1, N+1):
        if N%i == 0:
            nums.append(i)
            cnt+=1
    return nums, cnt

result=factors(36)
print(result)
