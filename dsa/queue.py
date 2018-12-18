class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    print("Size of queue is " + str(len(self.items)))

  def show(self):
    print(self.items)


print("=========================")

q = Queue()
q.enqueue("Harsh1")
q.enqueue("Harsh2")
q.enqueue("Harsh3")
q.show()
q.size()
print("Popped element is : " + q.dequeue())
q.show()
q.size()