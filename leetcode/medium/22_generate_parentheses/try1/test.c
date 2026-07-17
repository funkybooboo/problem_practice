#include "solution.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper function to check and print the test result
void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }
}

// Test case: n = 1
void testGenerateParenthesis_n1() {
    int returnSize;
    char** result = generateParenthesis(1, &returnSize);
    checkTestResult(returnSize == 1, "Test Case n=1 - Return size check");
    checkTestResult(strcmp(result[0], "()") == 0,
                    "Test Case n=1 - First result check");
    free(result[0]);
    free(result);
}

// Test case: n = 2
void testGenerateParenthesis_n2() {
    int returnSize;
    char** result = generateParenthesis(2, &returnSize);
    checkTestResult(returnSize == 2, "Test Case n=2 - Return size check");
    checkTestResult(strcmp(result[0], "(())") == 0,
                    "Test Case n=2 - First result check");
    checkTestResult(strcmp(result[1], "()()") == 0,
                    "Test Case n=2 - Second result check");
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

// Test case: n = 3
void testGenerateParenthesis_n3() {
    int returnSize;
    char** result = generateParenthesis(3, &returnSize);
    checkTestResult(returnSize == 5, "Test Case n=3 - Return size check");
    checkTestResult(strcmp(result[0], "((()))") == 0,
                    "Test Case n=3 - First result check");
    checkTestResult(strcmp(result[1], "(()())") == 0,
                    "Test Case n=3 - Second result check");
    checkTestResult(strcmp(result[4], "()()()") == 0,
                    "Test Case n=3 - Last result check");
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

// Test case: n = 4
void testGenerateParenthesis_n4() {
    int returnSize;
    char** result = generateParenthesis(4, &returnSize);
    checkTestResult(returnSize == 14, "Test Case n=4 - Return size check");

    // Checking first few results as examples
    checkTestResult(strcmp(result[0], "(((())))") == 0,
                    "Test Case n=4 - First result check");
    checkTestResult(strcmp(result[1], "((()()))") == 0,
                    "Test Case n=4 - Second result check");
    checkTestResult(strcmp(result[13], "()()()()") == 0,
                    "Test Case n=4 - Last result check");

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

// Test case: n = 5
void testGenerateParenthesis_n5() {
    int returnSize;
    char** result = generateParenthesis(5, &returnSize);
    checkTestResult(returnSize == 42, "Test Case n=5 - Return size check");

    // Checking first few results as examples
    checkTestResult(strcmp(result[0], "((((()))))") == 0,
                    "Test Case n=5 - First result check");
    checkTestResult(strcmp(result[1], "((()()))()") == 0,
                    "Test Case n=5 - Second result check");
    checkTestResult(strcmp(result[41], "()()()()()") == 0,
                    "Test Case n=5 - Last result check");

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

int main() {
    testGenerateParenthesis_n1();
    testGenerateParenthesis_n2();
    testGenerateParenthesis_n3();
    testGenerateParenthesis_n4();
    testGenerateParenthesis_n5();

    return 0;
}
