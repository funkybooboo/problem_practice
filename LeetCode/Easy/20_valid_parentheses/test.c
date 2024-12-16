#include "solution.h"
#include <stdio.h>

// Helper function to check and print the test result
void checkTestResult(const int condition, const char* testName) {
    if (condition) {
        printf("%s Passed!\n", testName);
    } else {
        printf("%s Failed!\n", testName);
    }

}

void testValidParentheses_EmptyString() {
    // Test case: empty string
    checkTestResult(isValid("") == true, "Test Case 1: Empty String");
}

void testValidParentheses_SinglePair() {
    // Test case: valid single pair "()"
    checkTestResult(isValid("()") == true, "Test Case 2: Single Pair");
}

void testValidParentheses_MultiplePairs() {
    // Test case: valid multiple pairs "()[]{}"
    checkTestResult(isValid("()[]{}") == true, "Test Case 3: Multiple Pairs");
}

void testValidParentheses_ValidNested() {
    // Test case: valid nested parentheses "([])"
    checkTestResult(isValid("([])") == true, "Test Case 4: Valid Nested");
}

void testValidParentheses_InvalidMismatch() {
    // Test case: invalid mismatch "(]"
    checkTestResult(isValid("(]") == false, "Test Case 5: Invalid Mismatch");
}

void testValidParentheses_InvalidUnmatchedOpening() {
    // Test case: invalid unmatched opening "{["
    checkTestResult(isValid("{[") == false, "Test Case 6: Invalid Unmatched Opening");
}

void testValidParentheses_InvalidUnmatchedClosing() {
    // Test case: invalid unmatched closing "})"
    checkTestResult(isValid("})") == false, "Test Case 7: Invalid Unmatched Closing");
}

void testValidParentheses_LongValid() {
    // Test case: long valid parentheses string "{[()()]}"
    checkTestResult(isValid("{[()()]}") == true, "Test Case 8: Long Valid");
}

int main() {
    // Run all individual tests
    testValidParentheses_EmptyString();
    testValidParentheses_SinglePair();
    testValidParentheses_MultiplePairs();
    testValidParentheses_ValidNested();
    testValidParentheses_InvalidMismatch();
    testValidParentheses_InvalidUnmatchedOpening();
    testValidParentheses_InvalidUnmatchedClosing();
    testValidParentheses_LongValid();

    return 0;
}
