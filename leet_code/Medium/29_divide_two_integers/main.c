#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: %s <dividend> <divisor>\n", argv[0]);
        return 1;
    }

    int dividend = atoi(argv[1]);
    int divisor = atoi(argv[2]);

    int result = divide(dividend, divisor);
    printf("Result of %d / %d = %d\n", dividend, divisor, result);

    return 0;
}
