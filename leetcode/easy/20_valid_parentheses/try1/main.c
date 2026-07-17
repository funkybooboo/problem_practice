#include "solution.h"
#include <stdio.h>

int main(const int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <string>\n", argv[0]);
        return 1;
    }

    char* input = argv[1];
    if (isValid(input)) {
        printf("true\n");
    } else {
        printf("false\n");
    }

    return 0;
}
