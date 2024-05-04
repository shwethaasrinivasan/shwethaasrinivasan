#Basic approach

def power(N, P):
    if P == 0:
        return 1
    return N * power(N, P - 1)
N = 2
P = 5
result = power(N,P)
print(f"{N}^{P} = {result}")

#Effificent

def power(N, P):
    if P == 0:
        return 1
    if P % 2 == 0:
        result = power(N, P // 2)
        return result * result
    else:
        result = power(N, (P - 1) // 2)
        return N * result * result

N = 2
P = 5
result = power(N, P)
print(f"{N}^{P} = {result}")

#power 3

def power(N, P):
    if P == 0:
        return 1
    if P % 2 == 0:
        result = power(N, P // 2)
        return result * result
    else:
        result = power(N, (P - 1) // 2)
        return N * result * result

N = 2
P = 5
result = power(N, P)
print(f"{N}^{P} = {result}")