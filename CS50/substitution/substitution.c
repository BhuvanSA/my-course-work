//Importing all required libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char *string; //Declaring string datatype
string inputs();

int main(int argc, string argv[])  // Main method code to read values from the terminal
{
    if (argc != 2) // Checking if 2nd argument is given
    {
        printf("Usage: ./substitution KEY\n");
        exit(1);
    }
    if (strlen(argv[1]) != 26) //Checking for length of the key
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    char *key = argv[1]; // Declaring key as the second Second Argument
    for (int i = 0; i < 26; i++)
    {
        int ch = (int) key[i];
        if ((ch >= 97) && (ch <= 122)) //Checking for a - z and converting to uppercase
        {
            ch -= 32;
        }
        else if ((ch >= 65) && (ch <= 90)) //Checking for A - Z
        {
        }
        else // Checking for characters other than that
        {
            printf("Key must only contain alphabetic characters.\n");
            return (1);
        }
        key[i] = (char) ch;
        for (int j = 0; j <= 26; j++) // Checking for repeated character in the key
        {
            if (i == j)
            {
                continue;
            }
            if (key[i] == key[j])
            {
                printf("Key must not contain repeated characters.\n");
                return (1);
            }
        }
    }
    string str = inputs();
    int len = strlen(str); // A new array delcared to store the string
    string str2 = malloc(sizeof(char) * len);
    for (int i = 0; i <= len; i++)
    {
        int ch = (int) str[i];
        if ((ch >= 65) && (ch <= 90)) // Substituting required keys to A-Z places
        {
            ch -= 65;
            str2[i] = key[ch];
        }
        else if ((ch >= 97) && (ch <= 122)) // Substituting required keys to a-z places and converting them to lower case
        {
            ch -= 97;
            str2[i] = (char)(((int) key[ch]) + 32);
        }
        else
        {
            str2[i] = str[i];
        }
        
    }
    printf("ciphertext: %s\n", str2); //printing the cipertext
    free(str); //Freeing all the malloc memory spaces
    free(str2);
}

string inputs() // A funtion to take input from the user
{
    char *si = malloc(sizeof(char) * 50);
    printf("plaintext: ");
    scanf("%[^\n]s", si);
    return si;
}
