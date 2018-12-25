
// Returns true if tree with given root contains
// dead end or not. min and max indicate range
// of allowed values for current node. Initially
// these values are full range.
bool deadEnd(Node* root, int min=1, int max=INT_MAX)
{
  // if the root is null or the recursion moves
  // after leaf node it will return false
  // i.e no dead end.
  if (!root)
    return false;

  // if this occurs means dead end is present.
  if (min == max)
    return true;

  // heart of the recursion lies here.
  return deadEnd(root->left, min, root->data - 1) ||
    deadEnd(root->right, root->data + 1, max);
}

// Driver program
int main()
{
  /* 8
  / \
  5 11
  / \
  2 7
  \
  3
  \
    4 */
  Node* root = NULL;
  root = insert(root, 8);
  root = insert(root, 5);
  root = insert(root, 2);
  root = insert(root, 3);
  root = insert(root, 7);
  root = insert(root, 11);
  root = insert(root, 4);
  if (deadEnd(root) == true)
    cout << "Yes " << endl;
  else
    cout << "No " << endl;
  return 0;
}
