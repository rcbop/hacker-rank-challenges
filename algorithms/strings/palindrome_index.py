# NOT WORKING FOR SOME TEST CASES
# investigate later
def unmatches(s):
    length = len(s)
    i = 0
    no_match = []
    while i < length:
        if s[i] != s[-i - 1]:
            no_match.append(i)
        i += 1
    return no_match

def palindrome(word):
    return str(word) == str(word)[::-1]

def find_remove_idx(idxs, s):
    if len(idxs) == 0:
        return
    temp = list(s)
    popped = idxs.pop()
    del(temp[popped])
    if palindrome(''.join(temp)):
        print(popped)
        return
    else:
        find_remove_idx(idxs, s)

n = int(input())

for i in range(n):
    s = input().strip()
    if palindrome(s):
        print(-1)

    idxs = unmatches(s)

    find_remove_idx(idxs, s)
