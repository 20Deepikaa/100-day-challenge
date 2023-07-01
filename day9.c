#include <stdio.h>

int main() 
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        int C, X, Y;
        scanf("%d %d %d", &C, &X, &Y);
        int add = C - X;
        int minimum = add * Y;
        printf("%d\n", minimum);
    }

    return 0;
}
