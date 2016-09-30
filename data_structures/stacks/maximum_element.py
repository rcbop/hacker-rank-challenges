class Stack(object):

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(max(self.peek(), value))

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return -999999999

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return self.data==[]

    def __str__(self):
        return ','.join([str(x) for x in self.data])


if __name__ == '__main__':
    stack = Stack()

    n = int(input())

    for i in range(n):
        inp = input().split(" ")
        operation = int(inp[0])

        if operation == 1:
            stack.push(int(inp[1]))

        elif operation == 2:
            stack.pop()

        elif operation ==3:
            print(stack.peek())

        else:
            print('invalid op')

        #print("operation",operation)
        #print("stack    ",stack)
        
