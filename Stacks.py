class Stack():

    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        if len(self.stack)<=0:
            return "Underflow"
        else:
            return self.stack.pop()


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
print(stack1.peek())
print(stack1.pop())
print(stack1.peek())