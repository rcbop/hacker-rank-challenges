
def left_rotation(a, k):
    return a[k:]+a[:k]

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = left_rotation(list(a), k);
print(*answer, sep=' ')
