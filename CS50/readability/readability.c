// Importing all the required libraries
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(void) 
{
    char *s = malloc(sizeof(char) * 50); //Declaring a char and allocating 50 bytes of data to it
    printf("Text: ");
    scanf("%[^\n]s", s); //Scanf modified to accept values to \n is used
    float letters = 0;
    float words = 1;
    float sentences = 0;
    int len = strlen(s);
    for (int i = 0 ; i < len ; i++) // A for loop which runs for the length of the sentence
    {
        if (isalpha(s[i]) != 0)
        {
            letters++;
        }
        if (isspace(s[i]) != 0)
        {
            words++;
        }
        if ((s[i] == '.') || (s[i] == '!') || (s[i] == '?'))
        {
            sentences++;
        }
    }
    float L = (letters / words) * 100; // Calculationg L
    float S = (sentences / words) * 100; // Calculating S
    float index = 0.0588 * L - 0.296 * S - 15.8; // Calculating index
    int rounded = round(index);
    if (rounded < 1) // Printing all three usecases
    {
        printf("Before Grade 1\n");
    }
    else if (rounded >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rounded);
    }
    free(s); // Freing the memory used to take up the variable
}
