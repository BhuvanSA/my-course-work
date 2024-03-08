// Importing libraries
#include <stdio.h>

int main(void) 
{
    int x = 0;
    while ((x < 1) || (x > 8)) //To get input
    {
        printf("Height: ");
        scanf("%i", &x);
    }
    for (int i = 0 ; i < x ; i++) //To print lines
    {
        for (int k = x - i; k > 1 ; k--) // To print spaces
        {
            printf(" ");
        }
        for (int j = 0; j <= i ; j++) // To print #
        {
            printf("#");
        }
        printf("\n"); // To move to next line
    }

    
}
