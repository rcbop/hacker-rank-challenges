size = int(input())
arr=[]
for i in range(size):
    string = list(input())
    rev_string = list(reversed(string))
    msg = "Funny"
    for j in range(len(string)):
        #print(j)
        if not abs(ord(string[j])-ord(string[j-1])) == abs(ord(rev_string[j])-ord(rev_string[j-1])):
            msg="Not Funny"
            break
    print(msg)
