#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;
int count = 0;

void insert(node *list,int number);
void free_list(node *list);
void print_list(node *list);

int main()
{
    node *list = malloc(sizeof(node));
    list->number = 0;
    list->next = NULL;
    for(int i = 100000; i > 0; i--)
    {
        insert(list,i);
    }
    print_list(list);
    free_list(list);
}

// Aim: To Create a method to insert elements into linked list;
void insert(node *list,int number)
{
    node *n = malloc(sizeof(node));
    n->number = number;
    n->next = list->next;
    list->next = n;
}

// Free the list
void free_list(node *list)
{
    node *p = list->next;
    if (list->next == NULL)
    {
        return;
    }
    free(list);
    free_list(p);
}

// Printing the list using recursion
void print_list(node *list)
{
    if(list->next == NULL)
    {
        return;
    }
    printf("%i  ",list->number);
    print_list(list->next);
}
    
