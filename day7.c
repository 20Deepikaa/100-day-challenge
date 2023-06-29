#include <stdio.h>

int main()
{
    int T, N, M, total;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d %d", &N, &M);
        total= N * 2 + M * 4;
        printf("%d\n", total);
    }
    return 0;
}
