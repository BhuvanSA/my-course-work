//importing libraries
#include <stdio.h>

int main(void)
{
    char str[40]; //Declaring a char array of 40 char
    printf("What's your name? "); //Asking name of the user
    scanf("%s", str); //Scanning the name of the user
    printf("hello, %s\n", str); //print hello and user name
    return 0;
}
