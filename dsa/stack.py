class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def size(self):
    print("Size = " + str(len(self.items)))

  def show(self):
    print(self.items)

print("======================")

s = Stack()
s.push("Harsh1")
s.size()
s.show()
s.push("Harsh2")
s.push("Harsh3")
s.push("Harsh4")
s.size()
s.show()
item = s.pop()
print("Poped Item = " + item)
s.size()
s.show()