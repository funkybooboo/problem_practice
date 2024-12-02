package main

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	// Iterate over the characters of the first string
	for i := 0; i < len(strs[0]); i++ {
		// Check the current character in all strings
		for j := 1; j < len(strs); j++ {
			// If the current character is out of bounds or does not match
			if i >= len(strs[j]) || strs[0][i] != strs[j][i] {
				return strs[0][:i] // Return the prefix up to the matched index
			}
		}
	}

	return strs[0] // If the entire first string is the common prefix
}
