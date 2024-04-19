class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty!")
      return
    return self.items.pop(0)

  def size(self):
    return len(self.items)

# Example code
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.dequeue())  
print(myQueue.size())     
