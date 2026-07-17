#include "solution.h"
#include <stdio.h>

void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

void testDivide() {
    checkTestResult(divide(10, 3) == 3, "Test Case 1");
    checkTestResult(divide(7, -3) == -2, "Test Case 2");
    checkTestResult(divide(-2147483648, -1) == 2147483647, "Test Case 3 (Overflow case)");
    checkTestResult(divide(2147483647, 1) == 2147483647, "Test Case 4 (No change case)");
    checkTestResult(divide(-2147483648, 1) == -2147483648, "Test Case 5 (Negative dividend)");
    checkTestResult(divide(0, 1) == 0, "Test Case 6 (Zero dividend)");
    checkTestResult(divide(10, 5) == 2, "Test Case 7 (Exact division)");
    checkTestResult(divide(10, 7) == 1, "Test Case 8 (Truncated division)");
}

int main() {
    testDivide();
    return 0;
}
