CC = gcc
CFLAGS = -Wall -g
OBJ_MAIN = main.o solution.o helper.o  # Added helper.o for the helper.c file
OBJ_TEST = test.o solution.o helper.o  # Added helper.o for the test executable

# Default target is to build both executables
all: main test

# Rule for building the main executable
main: $(OBJ_MAIN)
	$(CC) $(OBJ_MAIN) -o main

# Rule for building the test executable
test: $(OBJ_TEST)
	$(CC) $(OBJ_TEST) -o test

# Rule for compiling main.o
main.o: main.c solution.h helper.h
	$(CC) $(CFLAGS) -c main.c

# Rule for compiling test.o
test.o: test.c solution.h helper.h
	$(CC) $(CFLAGS) -c test.c

# Rule for compiling solution.o (common to both main and test)
solution.o: solution.c solution.h
	$(CC) $(CFLAGS) -c solution.c

# Rule for compiling helper.o (added for helper functions)
helper.o: helper.c helper.h
	$(CC) $(CFLAGS) -c helper.c

# Clean up object files and executables
clean:
	rm -f *.o main test

# Run clang-format on all C and H files
format:
	clang-format -i *.c *.h

# Run clang-tidy on all C files
lint:
	clang-tidy *.c -- -I.
