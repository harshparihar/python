import gc

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

# Function to delete a node in a Doubly Linked List.
# head_ref --> pointer to head node pointer.
# dele --> pointer to node to be deleted
  def deleteNode(self, dele):
    # If node to be deleted is head node
    if self.head == dele:
      self.head = dele.next

    if dele.next is not None:
      dele.next.prev = dele.prev

    # Change prev only if node to be deleted is NOT
    # the first node
    if dele.prev is not None:
      dele.prev.next = dele.next
    gc.collect()


  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node
    self.head = new_node

  def printList(self, node):
    while(node is not None):
      print node.data,
      node = node.next


# Driver program to test the above functions

# Start with empty list
dll = DoublyLinkedList()

# Let us create the doubly linked list 10<->8<->4<->2
dll.push(2);
dll.push(4);
dll.push(8);
dll.push(10);

print "\n Original Linked List",
dll.printList(dll.head)

# delete nodes from doubly linked list
dll.deleteNode(dll.head)
dll.deleteNode(dll.head.next)
dll.deleteNode(dll.head.next)
# Modified linked list will be NULL<-8->NULL
print "\n Modified Linked List",
dll.printList(dll.head)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
