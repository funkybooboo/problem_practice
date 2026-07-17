#include "solution.h"
#include <stdio.h>
#include <stdlib.h>

void testSingleMatch() {
    char* s = "barfoothefoobarman";
    char* words[] = {"foo", "bar"};
    int expected[] = {0, 9};
    int returnSize;
    int* result = findSubstring(s, words, 2, &returnSize);

    int pass = (returnSize == 2 && result[0] == expected[0] && result[1] == expected[1]);
    printf("Test Single Match: %s\n", pass ? "Passed" : "Failed");
    free(result);
}

void testNoMatch() {
    char* s = "wordgoodgoodgoodbestword";
    char* words[] = {"word", "good", "best", "word"};
    int returnSize;
    int* result = findSubstring(s, words, 4, &returnSize);

    int pass = (returnSize == 0);
    printf("Test No Match: %s\n", pass ? "Passed" : "Failed");
    free(result);
}

void testMultipleMatches() {
    char* s = "barfoofoobarthefoobarman";
    char* words[] = {"bar", "foo", "the"};
    int expected[] = {6, 9, 12};
    int returnSize;
    int* result = findSubstring(s, words, 3, &returnSize);

    int pass = (returnSize == 3 && result[0] == expected[0] && result[1] == expected[1] && result[2] == expected[2]);
    printf("Test Multiple Matches: %s\n", pass ? "Passed" : "Failed");
    free(result);
}

int main() {
    testSingleMatch();
    testNoMatch();
    testMultipleMatches();
    return 0;
}
