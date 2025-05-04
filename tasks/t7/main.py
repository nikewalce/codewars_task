def tribonacci(signature: list, n: int)->list:
    if (all([i == 1 for i in signature]) == True) and (n == 1):
        return[1]
    elif all([i == 0 for i in signature]) == True:
        return [0 for i in range(n)]
    elif n == 0:
        return []
    elif n == 1:
        return signature[:1]
    elif n == 2:
        return signature[0:2]
    else:
        [signature.append(sum(signature[-1:-4:-1])) for i in range(n-3)]
        return signature

print(tribonacci([1,1,1], 2))
