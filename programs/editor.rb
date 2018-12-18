#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;

struct node{
  char data;
  node * next;
};
void addtolist(node *&head, node*&tail, char data, int &size,node*¤t)

{
  if (tail == nullptr)
  {
    head = tail = new node;
    head->data = data;
    head->next = nullptr;
    current = head;
  }
  else
  {
    tail->next = new node;
    tail = tail->next;
    tail->data = data;
    tail->next = nullptr;
    current = tail;
    size++;
  }
}
void printlist(node *head, int size, node *tail, node* current)
{
  current = head;
  while (current != nullptr)
  {

    cout << current->data;
    current = current->next;
  }
}
void remove(node*&head, node*&tail, node *& current)//It is still to be Completed
{
  node *prev = nullptr, *current1 = head;
  while (current1 != nullptr && current1 != current)
  {
    prev = current1;
    current1 = current1->next;
  }
  if (current1 == nullptr)
  {
    cout << "Key not found !";
  }
  else if (prev == nullptr)
  {
    head = head->next;
    delete[]current1;
    cout << "yes";
  }
  else
  {
    prev->next = current1->next;
    delete[]current1;
    cout << "yes";
  }
}

int main()
{
  int n, n1, n2, n3;
  char w='a', w1, w2;
  node * head = nullptr;
  int size = 0;
  node *tail = nullptr;
  node *current = head;
  while (w != 13)
  {
    w = _getch();
    if (w <= 126 || w >= 32)
    {
      addtolist(head, tail, w, size,current);


    }
    else if(w == 8)
    {
      remove(head, tail, current);
    }

    Sleep(1500);
    printlist(head, size, tail, current);

  }

}