# Node class
class Node:
  def __init__(self, data):
    self.data = data # Assign data
    self.next = None # Initialize next as null

class LinkedList:

  def __init__(self):
    self.head = None

  def push_at_front(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def printList(self):
    temp = self.head
    while (temp):
      print temp.data,
      temp = temp.next

  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print "The given previous node must inLinkedList."
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


# Code execution starts here
if __name__=='__main__':
  llist = LinkedList()

  # llist.head = Node(10)
  llist.printList()
  # print(aa)
  # second = Node(20)
  # third = Node(30)

  # llist.head.next = second;
  # print(llist.printList())
  # second.next = third;


  # print(llist.printList())

  # llist.insertAfter(second, 25)
  # print(llist.printList())