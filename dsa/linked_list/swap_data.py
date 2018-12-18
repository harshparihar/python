class LinkedList(object):
  def __init__(self):
    self.head = None

  class Node(object):
    def __init__(self, d):
      self.data = d
      self.next = None

  def swapNodes(self, x, y):
    if x == y:
      return

    # Search for x (keep track of prevX and CurrX)
    prevX = None
    currX = self.head
    while currX != None and currX.data != x:
      prevX = currX
      currX = currX.next

    # Search for y (keep track of prevY and currY)
    prevY = None
    currY = self.head
    while currY != None and currY.data != y:
      prevY = currY
      currY = currY.next

    # If either x or y is not present, nothing to do
    if currX == None or currY == None:
      return
    # If x is not head of linked list
    if prevX != None:
      prevX.next = currY
    else: #make y the new head
      self.head = currY

    # If y is not head of linked list
    if prevY != None:
      prevY.next = currX
    else: # make x the new head
      self.head = currX

    temp = currX.next
    currX.next = currY.next
    currY.next = temp

  def push(self, new_data):
    new_Node = self.Node(new_data)
    new_Node.next = self.head
    self.head = new_Node

  def printList(self):
    tNode = self.head
    while tNode != None:
      print tNode.data,
      tNode = tNode.next

# Driver program to test above function
llist = LinkedList()

# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print "Linked list before calling swapNodes() "
llist.printList()
llist.swapNodes(2,6)
print "\nLinked list after calling swapNodes() "
llist.printList()

# This code is contributed by BHAVYA JAIN
