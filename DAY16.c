#include <stdio.h>
char* is_valid_game(int N, int X) {
    if (X < N) {
        return "NO";
    }
    if (X % N == 0) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    int T;
    scanf("%d", &T);  
    while (T--) {
        int N, X;
        scanf("%d %d", &N, &X);  
        char* result = is_valid_game(N, X);
        printf("%s\n", result);
    }
    
    return 0;
}
