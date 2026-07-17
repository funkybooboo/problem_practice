#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "solution.h"
#include "helper.h"

// Helper function to parse a list from a command-line argument string
int* parseList(const char* input, int* size) {
    // Create a copy of the input string to safely tokenize (avoid modifying the original)
    char* list_str = strdup(input);
    if (list_str == NULL) {
        perror("strdup failed");
        exit(1);  // Handle memory allocation failure
    }

    // First, count how many numbers there are in the string
    *size = 0;
    char* token = strtok(list_str, " ");
    while (token != NULL) {
        (*size)++;
        token = strtok(NULL, " ");
    }

    // Now allocate the array to hold the integers
    int* arr = malloc(*size * sizeof(int));
    if (arr == NULL) {
        perror("malloc failed");
        exit(1);  // Handle memory allocation failure
    }

    // Reset list_str to the original input string to re-tokenize it
    // We need to duplicate the string again to prevent strtok from modifying the input
    char* list_str_copy = strdup(input);
    if (list_str_copy == NULL) {
        perror("strdup failed");
        exit(1);  // Handle memory allocation failure
    }

    // Re-tokenize the string and store each number as an integer in the array
    token = strtok(list_str_copy, " ");
    int i = 0;
    while (token != NULL) {
        arr[i++] = atoi(token);  // Convert string to integer
        token = strtok(NULL, " ");
    }

    free(list_str);  // Free the first copied string
    free(list_str_copy);  // Free the second copied string
    return arr;
}

int main(const int argc, char* argv[]) {
    if (argc != 3) {
        printf("Please provide two lists in the format: %s \"1 2 3\" \"4 5 6\"\n", argv[0]);
        return 1;
    }

    int list1Size;
    int list2Size;
    int* list1Arr = parseList(argv[1], &list1Size);
    int* list2Arr = parseList(argv[2], &list2Size);

    struct ListNode* list1 = createList(list1Arr, list1Size);
    struct ListNode* list2 = createList(list2Arr, list2Size);

    const struct ListNode* mergedList = mergeTwoLists(list1, list2);

    printf("Merged List: ");
    printList(mergedList);

    free(list1Arr);
    free(list2Arr);

    return 0;
}
