class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def inorder(root):
  if root is not None:
    inorder(root.left)
    print root.key,
    inorder(root.right)

def insert(node, key):
  if node is None:
    return Node(key)
  if key < node.key:
    node.left = insert(node.left, key)
  else:
    node.right = insert(node.right, key)
  return node

# Given a non-empty binary search tree, return the node
# with minum key value found in that tree. Note that the
# entire tree does not need to be searched
def minValueNode( node):
  current = node
  while(current.left is not None):
    current = current.left
  return current

def deleteNode(root, key):
  if root is None:
    return root
  if key < root.key:
    root.left = deleteNode(root.left, key)
  elif(key > root.key):
    root.right = deleteNode(root.right, key)
  else:

    # Node with only one child or no child
    if root.left is None :
      temp = root.right
      root = None
      return temp

    elif root.right is None :
      temp = root.left
      root = None
      return temp

    # Node with two children: Get the inorder successor
    # (smallest in the right subtree)
    temp = minValueNode(root.right)

    # Copy the inorder successor's content to this node
    root.key = temp.key

    # Delete the inorder successor
    root.right = deleteNode(root.right , temp.key)


  return root

# Driver program to test above functions
""" Let us create following BST
      50
     /  \
    30   70
    / \ / \
  20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print "Inorder traversal of the given tree"
inorder(root)

print "\nDelete 20"
root = deleteNode(root, 20)
print "Inorder traversal of the modified tree"
inorder(root)

print "\nDelete 30"
root = deleteNode(root, 30)
print "Inorder traversal of the modified tree"
inorder(root)

print "\nDelete 50"
root = deleteNode(root, 50)
print "Inorder traversal of the modified tree"
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
