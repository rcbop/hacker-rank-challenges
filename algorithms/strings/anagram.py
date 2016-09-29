from collections import Counter
def number_needed(a, b):
    #print(a,b)
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    #print(ct_a)
    return sum(abs(i) for i in ct_a.values())//2

n = int(input())
for i in range(n):
    s = input();
    a, b = s[:len(s)//2], s[len(s)//2:]
    if len(a)>len(b) or len(b)>len(a):
        print(-1)
    else:
        print(number_needed(a,b))
