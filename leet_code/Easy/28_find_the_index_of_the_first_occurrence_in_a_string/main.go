package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run main.go <haystack> <needle>")
		return
	}

	haystack := os.Args[1]
	needle := os.Args[2]
	result := strStr(haystack, needle)
	fmt.Println(result)
}
