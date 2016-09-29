input_size = int(input())
arr=[]
for i in range(input_size):
    arr.append(input())

count=0
for i,v in enumerate(arr):
    for j,c in enumerate(arr[i]):
        if j-1>=0 and arr[i][j-1] == arr[i][j]:
            count+=1
    print(count)
    count=0
