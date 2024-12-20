#include "solution.h"
#include "helper.h"
#include <stdio.h>
#include <stdlib.h>

int main(const int argc, char* argv[]) {
    if (argc < 2) {
        printf("Please provide a list of integers.\n");
        return 1; // Exit if no arguments are provided
    }

    // Allocate an array to hold the integers from the command line
    int* arr = malloc((argc - 1) * sizeof(int));

    // Parse command-line arguments into an array of integers
    for (int i = 1; i < argc; i++) {
        arr[i - 1] = atoi(argv[i]); // Convert string to integer using atoi
    }

    // Build the linked list from the array
    struct ListNode* head = buildList(arr, argc - 1);

    // Debug: Print the original list before swapping
    printf("Original List: ");
    printList(head);

    // Perform swap in pairs
    const struct ListNode* result = swapPairs(head);

    // Print the result
    printf("Swapped List : ");
    printList(result);

    // Free the dynamically allocated array
    free(arr);

    return 0;
}
