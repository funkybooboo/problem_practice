#include <stdbool.h>
#include <string.h>

#define MAX_STACK_SIZE 10000

// Helper function to implement the stack functionality
typedef struct {
    char data[MAX_STACK_SIZE];
    int top;
} Stack;

// Initialize the stack
void initStack(Stack* stack) {
    stack->top = -1;
}

// Push an element onto the stack
void push(Stack* stack, const char c) {
    if (stack->top < MAX_STACK_SIZE - 1) {
        stack->data[++stack->top] = c;
    }
}

// Pop an element from the stack
char pop(Stack* stack) {
    if (stack->top == -1) {
        return '\0'; // Return null character if stack is empty
    }
    return stack->data[stack->top--];
}

// Check if the character is a matching open parenthesis
bool isOpenParenthesis(const char c) {
    return c == '(' || c == '{' || c == '[';
}

// Check if the character is a matching close parenthesis
bool isCloseParenthesis(const char c) {
    return c == ')' || c == '}' || c == ']';
}

// Check if two parentheses match
bool isMatch(const char open, const char close) {
    return (open == '(' && close == ')') || (open == '{' && close == '}') ||
           (open == '[' && close == ']');
}

// Function to check if the parentheses in the string are valid
bool isValid(char* s) {
    Stack stack;
    initStack(&stack);

    for (int i = 0; i < strlen(s); i++) {
        char c = s[i];

        // If it's an opening bracket, push it onto the stack
        if (isOpenParenthesis(c)) {
            push(&stack, c);
        }
        // If it's a closing bracket, check if it matches the top of the stack
        else if (isCloseParenthesis(c)) {
            const char top = pop(&stack);
            if (!isMatch(top, c)) {
                return false;
            }
        }
    }

    // If the stack is empty, all parentheses were matched
    return stack.top == -1;
}
