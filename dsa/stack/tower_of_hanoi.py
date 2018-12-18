class Stack:
  def __init__(self, name):
    self.top = -1
    self.name = name
    self.array = []

    # check if the stack is empty
    def isEmpty(self):
      return True if self.top == -1 else False

    # Pop the element from the stack
    def pop(self):
      if not self.isEmpty():
        self.top -= 1
        return self.array.pop()
      else:
        return "$"

    # Push the element to the stack
    def push(self, op):
      self.top += 1
      self.array.append(op)

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
  if n == 1:
    print "Move disk 1 from rod",from_rod,"to rod",to_rod
    return
  TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
  print "Move disk",n,"from rod",from_rod,"to rod",to_rod
  x = from_rod.pop()
  to_rod.push(x)
  TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

s1 = Stack("s1")
s2 = Stack("s2")
s3 = Stack("s3")

n = 4
print(s1)
print(s3)
# TowerOfHanoi(n, s1, s3, s2)
print("=============")
print(s1)
print(s3)



# s1.push(2)
# s1.push(6)
# s1.push(3)
# print(s1)
