#include "solution.h"
#include "helper.h"
#include <stdio.h>
#include <stdlib.h>

int main(const int argc, char* argv[]) {
    // Check if the user provided enough arguments (k + list of integers)
    if (argc < 3) {
        printf("Please provide a value for k followed by a list of integers.\n");
        return 1; // Exit if insufficient arguments
    }

    // Parse the value of k from the first argument
    int k = atoi(argv[1]);
    if (k <= 0) {
        printf("Invalid value for k. Please provide a positive integer for k.\n");
        return 1;  // Exit if k is not a valid positive integer
    }

    // Allocate an array to hold the integers from the command line (except the first argument, which is k)
    int* arr = malloc((argc - 2) * sizeof(int));  // Exclude the first argument (k)

    // Parse command-line arguments into an array of integers (excluding k)
    for (int i = 2; i < argc; i++) {
        arr[i - 2] = atoi(argv[i]); // Convert string to integer using atoi
    }

    // Build the linked list from the array
    struct ListNode* head = buildList(arr, argc - 2);

    // Debug: Print the original list before reversing in k-group
    printf("Original List: ");
    printList(head);

    // Perform the reverse in k-group
    struct ListNode* result = reverseKGroup(head, k);

    // Print the result
    printf("Reversed List in %d-Group: ", k);
    printList(result);

    // Free the dynamically allocated array
    free(arr);

    return 0;
}
