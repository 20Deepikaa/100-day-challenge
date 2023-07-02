#include <stdio.h>

int main() {
    int T; 
    scanf("%d", &T);
    while (T--) 
    {
        int X, Y;
        scanf("%d %d", &X, &Y);
        int total = (X * 10) + (Y * 5);
        printf("%d\n", total);
    }
    return 0;
}

