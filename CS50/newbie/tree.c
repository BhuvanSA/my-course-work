#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

void free_tree(node *root);
void print_tree(node *root);

int main(void)
{
    node *tree = NULL;

    node *n = malloc(sizeof(node));
    n->number = 4;
    n->left = NULL;
    n->right = NULL;
    tree = n;

    // Adding a number to the list
    n = malloc(sizeof(node));
    n->number = 2;
    n->left = NULL;
    n->right = NULL;
    tree->left = n;

    // Adding another number to the tree
    n = malloc(sizeof(node));
    n->number = 6;
    n->left = NULL;
    n->right = NULL;
    tree->right = n;

    // Adding Third Layer elements to the tree
    n = malloc(sizeof(node));
    n->number = 1;
    n->left = NULL;
    n->right = NULL;
    tree->left->left = n;

    n = malloc(sizeof(node));
    n->number = 3;
    n->left = NULL;
    n->right = NULL;
    tree->left->right = n;

    n = malloc(sizeof(node));
    n->number = 5;
    n->left = NULL;
    n->right = NULL;
    tree->right->left = n;

    n = malloc(sizeof(node));
    n->number = 7;
    n->left = NULL;
    n->right = NULL;
    tree->right->right = n;

    print_tree(tree);
    free_tree(tree);
}
void print_tree(node *root)
{
    if(root == NULL)
    {
        return;
    }
    print_tree(root->right);
    printf("%i\n",root->number);
    print_tree(root->left);
}
void free_tree(node *root)
{
    if(root == NULL)
    {
        return;
    }
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}


