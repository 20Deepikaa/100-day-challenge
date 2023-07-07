#include <stdio.h>
int main()
{
    int T, N;
    scanf("%d", &T);  
    while (T--) {
        scanf("%d", &N);  
        int cars = (N + 3) / 4;
        printf("%d\n", cars);
    }
    return 0;
}


