n = int(input())
for i in range(n):
    s = input()
    if str(s) == str(s)[::-1]:
        print(0)
        continue

    count = 0
    m = list(s)
    for j in range(len(s[:len(s)//2])):
        while ord(m[j]) != ord(m[-j-1]):
            if ord(m[j]) < ord(m[-j-1]):
                m[-j-1] = chr(ord(m[-j-1])-1)
            else:
                m[j] = chr(ord(m[j])-1)
            count+=1
    print(count)
