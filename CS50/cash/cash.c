#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char *string;
int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);
string input_function(); //Failproof methond to take input from the user

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents = atoi(input_function());
    return cents;
}

int calculate_quarters(int cents)
{
    // TODO
    int quo = cents / 25;
    return quo;
}

int calculate_dimes(int cents)
{
    // TODO
    int quo = cents / 10;
    return quo;
}

int calculate_nickels(int cents)
{
    // TODO
    int quo = cents / 5;
    return quo;
}

int calculate_pennies(int cents)
{
    // TODO
    return cents;
}
string input_function() //Failproof methond to take input from the user
{
    string si = malloc(sizeof(char) * 20); //Allocation of the char array of 20 bytes
    int i;
    long val;
    char *next;
    int h = 1;
    while (h) // Can optimize this part by using ASCII values for conversion
    {
        printf("Number: ");
        scanf("%s", si);
        val = strtol(si, &next, 10);
        if ((next == si) || (*next != '\0'))
        {
            h = 1;
        } 
        else
        {
            h = 0;
        }
        i = atoi(si);
        if (i < 0)
        {
            h = 1;
        }
    }
    return si;
}
