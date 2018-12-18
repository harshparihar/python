class Queue:
  def __init__(self):
    self.array = []

  def EnQueue(self, item):
    self.array.append(item)
    print("%s enqueued to queue" %str(item))

  def DeQueue(self):
    item = self.array.pop(0)
    print("%s dequeued from queue" %str(item))

  def que_front(self):
    print("Front item is", self.array[0])

  def que_rear(self):
    print("Rear item is", self.array[-1])

  def show(self):
    print(self.array)

print("======================")

queue = Queue()
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.EnQueue(50)
queue.show()
queue.DeQueue()
queue.show()
queue.que_front()
queue.que_rear()
queue.show()
