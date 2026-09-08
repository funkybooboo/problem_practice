#include "collatz_conjecture.h"

#include <stdint.h>

int steps(int start) {
    uint64_t count = 0;
    int n = start;
    while (n != 1) {
        if (n < 1) {
            return ERROR_VALUE;
        }
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = (n * 3) + 1;
        }
        count++;
    }
    return count;
}
