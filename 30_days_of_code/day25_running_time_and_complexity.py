import math
def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1 or (n & 1) == 0:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False

    return True

s = int(input())
for n in range(0,s):
    x = int(input())
    s = "Prime" if (is_prime(x)) else "Not prime"
    print(s)
    
