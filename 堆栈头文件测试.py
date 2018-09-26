from text12 import *

stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.isEmpty():
    print(stack.pop(), end=" ")
