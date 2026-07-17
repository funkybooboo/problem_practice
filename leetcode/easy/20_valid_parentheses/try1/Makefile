CC = gcc
CFLAGS = -Wall -g
OBJ_MAIN = main.o solution.o
OBJ_TEST = test.o solution.o

# Default target is to build both executables
all: main test

# Rule for building the main executable
main: $(OBJ_MAIN)
	$(CC) $(OBJ_MAIN) -o main

# Rule for building the test executable
test: $(OBJ_TEST)
	$(CC) $(OBJ_TEST) -o test

# Rule for compiling main.o
main.o: main.c solution.h
	$(CC) $(CFLAGS) -c main.c

# Rule for compiling test.o
test.o: test.c solution.h
	$(CC) $(CFLAGS) -c test.c

# Rule for compiling solution.o (common to both main and test)
solution.o: solution.c solution.h
	$(CC) $(CFLAGS) -c solution.c

# Clean up object files and executables
clean:
	rm -f *.o main test

# Run clang-format on all C and H files
format:
	clang-format -i *.c *.h

# Run clang-tidy on all C files
lint:
	clang-tidy *.c -- -I.
