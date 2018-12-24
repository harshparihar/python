
// function return sum of all element smaller than
// and equal to Kth smallest element
int ksmallestElementSumRec(Node *root, int k, int &count)
{
  if (root == NULL)
    return 0;
  if (count > k)
    return 0;

  int res = ksmallestElementSumRec(root->left, k, count);
  if (count >= k)
    return res;

  res += root->data;

  // Add current Node
  count++;
  if (count >= k)
  return res;

  // If count is less than k, return right subtree Nodes
  return res + ksmallestElementSumRec(root->right, k, count);
}

// Wrapper over ksmallestElementSumRec()
int ksmallestElementSum(struct Node *root, int k)
{
int count = 0;
ksmallestElementSumRec(root, k, count);
}

/* Driver program to test above functions */
int main()
{

  /* 20
    / \
  8  22
  / \
  4  12
    / \
    10 14
    */
  Node *root = NULL;
  root = insert(root, 20);
  root = insert(root, 8);
  root = insert(root, 4);
  root = insert(root, 12);
  root = insert(root, 10);
  root = insert(root, 14);
  root = insert(root, 22);

  int k = 3;
  cout << ksmallestElementSum(root, k) <<endl;
  return 0;
}
