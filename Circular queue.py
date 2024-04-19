class CircularQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.items = [None] * capacity  
    self.head = self.tail = -1  

  def is_full(self):
    return (self.tail + 1) % self.capacity == self.head

  def is_empty(self):
    return self.head == -1

  def enqueue(self, item):
    if self.is_full():
      print("Queue Overflow!")
      return
    if self.is_empty():
      self.head = 0
    self.tail = (self.tail + 1) % self.capacity
    self.items[self.tail] = item

  def dequeue(self):
    if self.is_empty():
      print("Queue Underflow!")
      return
    item = self.items[self.head]
    self.items[self.head] = None 
    if self.head == self.tail:  
      self.head = self.tail = -1
    else:
      self.head = (self.head + 1) % self.capacity
    return item

  def size(self):
    if self.is_empty():
      return 0
    return (self.tail + 1) % self.capacity - self.head

  def __str__(self):
    if self.is_empty():
      return "Queue is empty"
    result = "Circular Queue: "
    i = self.head
    while i != self.tail:
      result += str(self.items[i]) + " -> "
      i = (i + 1) % self.capacity
    result += str(self.items[i])
    return result

# Example code
myQueue = CircularQueue(5)
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
print(myQueue)  

print(myQueue.dequeue()) 
print(myQueue)  

myQueue.enqueue(40)
myQueue.enqueue(50)
myQueue.enqueue(60)  

print(myQueue)  
