class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.isEmpty():
      print("Stack Underflow!")
      return
    return self.items.pop()

  def peek(self):
    if self.isEmpty():
      print("Stack Underflow!")
      return
    return self.items[-1]

  def size(self):
    return len(self.items)

# Example code
myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)

print(myStack.pop())  
print(myStack.peek())  
print(myStack.size()) 
