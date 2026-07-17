#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "solution.h"

// Helper function to convert a string to an integer array
int* stringToArray(const char* str, int* size) {
    const int len = (int)strlen(str);
    int* arr = malloc(len * sizeof(int));
    int count = 0;

    const char* p = str;
    while (*p) {
        while (isspace(*p)) {
            p++; // Skip any spaces
        }
        if (isdigit(*p)) {
            arr[count++] = (int)strtol(p, (char**)&p, 10);
        } else {
            p++; // Move on if the character is not a number
        }
    }
    *size = count;
    return arr;
}

int main(const int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: %s <list> <n>\n", argv[0]);
        return 1;
    }

    // Parse arguments
    int size;
    int* arr = stringToArray(argv[1], &size);
    int n = atoi(argv[2]);

    // Create the linked list from the array
    struct ListNode* head = createList(arr, size);

    // Remove the nth node from the end
    head = removeNthFromEnd(head, n);

    // Print the updated list
    printf("Updated List: ");
    printList(head);

    // Free memory (important!)
    free(arr);
    while (head) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
