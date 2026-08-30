#include "grains.h"

#include <math.h>

uint64_t square(uint8_t index) {
    if (index == 0) { return 0; }
    if (index == 1) { return 1; }
    return pow(2, index - 1);
}

uint64_t total(void) {
    uint64_t sum = 0;
    for (uint8_t index = 1; index <= 64; index++) {
        sum += square(index);
    }
    return sum;
}
