// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"
#include <string.h>
#include <stdlib.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    unsigned int h = hash(word);
    node *list = table[h];
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        if ((strcasecmp(word, tmp->word)) == 0)
        {
            return true;
        }
    }
    return false;
}
// Global variable
unsigned int count = 0, indexNum = 0;

// Hashes word to a number
unsigned int hash(const char *word)
{
// TODO: Improve this hash function
    indexNum = (int) tolower(word[0]);
    indexNum -= 97;

    return indexNum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return false;
    }
    char *word = malloc(sizeof(char) * LENGTH);
    if (word == NULL)
    {
        return false;
    }
    while (fscanf(f, "%s", word) != EOF)
    {
        node *new = malloc(sizeof(node));
        if (new == NULL)
        {
            return false;
        }
        strcpy(new->word, word);
        hash(word);
        new->next = table[indexNum];
        table[indexNum] = new;
        count++;
    }
    fclose(f);
    free(word);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *tmp, *cursor;

    // Cycles through each hashtable index
    for (int i = 0; i < N; i++)
    {
        // Go to the prox i if there is nothing in the table [i]
        if (table[i] == NULL)
        {
            continue;
        }

        cursor = table[i];
        tmp = cursor;

        // Free the hastable
        while (cursor->next != NULL)
        {
            // point to the next node first so as not to lose the adress
            cursor = cursor->next;
            free(tmp);
            // point to the node actual node to free
            tmp = cursor;
        }
        free(cursor);
    }
    return true;
}
