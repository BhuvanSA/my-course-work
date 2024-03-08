#include <stdio.h>

int main()
{
    int a = 3131;
    int b = 4;
    int temp = a;
    a = b;
    b = temp;
    printf("%i\n",a);
    printf("%i\n",b);
    return 0;
}
