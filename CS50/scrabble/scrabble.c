#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char *string;

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


int compute_score(string word);
string get_string(string s);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    //Freeing malloced memory spaces
    free(word1);
    free(word2);
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int score = 0;
    for (int i = 0 ; i < strlen(word) ; i++)
    {
        if ((word[i] >= 'a') && (word[i] <= 'z'))
        {
            score += POINTS[((int)word[i]) - 97];
        }
    }

    return score;    
}
string get_string(string s)
{
    string str = malloc(sizeof(char) * 20);
    printf("%s", s);
    scanf("%s", str);
    for (int i = 0 ; i < strlen(str) ; i++)
    {
        str[i] = tolower(str[i]);
    }
    return str;
}
