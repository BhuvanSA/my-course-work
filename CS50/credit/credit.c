// Importing all the required libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char *string; // Creating a string variable
string input_function();
int summer(int num);

int main(void) // Main method
{
  int a[20]; // An array of 20 integers
  int sum = 0;
  string s = input_function(); // Storing the input in this variable
  int len = strlen(s);
  for (int i = 0; i < len - 1;
       i += 2) // An algorithm to multiply the appropriate digits by 2 and
               // convert into integer array
  {
    if (len % 2 != 0) // if length is odd Eg.5
    {
      a[i] = (s[i] - '0');
      a[i + 1] = ((s[i + 1] - '0') * 2);
    } else // even
    {
      a[i] = ((s[i] - '0') * 2);
      a[i + 1] = ((s[i + 1] - '0'));
    }
  }
  if (len % 2 != 0) // adding the last digit to the array to not make it skip
  {
    a[len - 1] = (s[len - 1] - '0');
  }
  for (int j = 0; j < len; j++) // summing two digit number in the array
  {
    a[j] = summer(a[j]);
  }
  for (int j = 0; j < len; j++) // summing all the numbers in the array
  {
    sum += a[j];
  }
  if ((sum % 10 == 0) && (s[0] == '3') && ((s[1] == '4') || (s[1] == '7')) &&
      (len == 15)) // Checking for American Express
  {
    printf("AMEX\n");
  } else if ((len == 16) && (s[0] == '5') && (sum % 10 == 0) &&
             ((s[1] == '1') || (s[1] == '2') || (s[1] == '3') ||
              (s[1] == '4') || (s[1] == '5'))) // Checking for mastercard
  {
    printf("MASTERCARD\n");
  } else if (((len == 13) || (len == 16)) && (sum % 10 == 0) &&
             (s[0] == '4')) // Checking for visa

  {
    printf("VISA\n");
  } else // the invalid output option
  {
    printf("INVALID\n");
  }
  free(s); // freeing the allocated memory by malloc
}

string input_function() // Failproof methond to take input from the user
{
  string si =
      malloc(sizeof(char) * 20); // Allocation of the char array of 20 bytes
  int i;
  long val;
  char *next;
  int h = 1;
  while (h) // Can optimize this part by using ASCII values for conversion
  {
    printf("Number: ");
    scanf("%s", si);
    val = strtol(si, &next, 10);
    if ((next == si) || (*next != '\0')) {
      h = 1;
    } else {
      h = 0;
    }
  }
  return si;
}

int summer(int num) // A function to sum all the digits in a number and return
                    // the value
{
  int sum = 0;
  while (num > 0) {
    sum += num % 10;
    num /= 10;
  }
  return sum;
}
