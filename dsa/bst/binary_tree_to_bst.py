class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# Helper function to store the inroder traversal of a tree
def storeInorder(root, inorder):
  if root is None:
    return
  storeInorder(root.left, inorder)
  inorder.append(root.data)
  storeInorder(root.right, inorder)

def countNodes(root):
  if root is None:
    return 0
  return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array to Binary tree
def arrayToBST(arr, root):
  if root is None:
    return
  arrayToBST(arr, root.left)
  root.data = arr[0]
  arr.pop(0)
  arrayToBST(arr, root.right)

# This function converts a given binary tree to BST
def binaryTreeToBST(root):
  if root is None:
    return

  # Count the number of nodes in Binary Tree so that
  # we know the size of temporary array to be created
  n = countNodes(root)

  # Create the temp array and store the inorder traveral of tree
  arr = []
  storeInorder(root, arr)

  # Sort the array
  arr.sort()

  # copy array elements back to binary tree
  arrayToBST(arr, root)

# Print the inorder traversal of the tree
def printInorder(root):
  if root is None:
    return
  printInorder(root.left)
  print root.data,
  printInorder(root.right)

# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right= Node(5)

# Convert binary tree to BST
binaryTreeToBST(root)

print "Following is the inorder traversal of the converted BST"
printInorder(root)
