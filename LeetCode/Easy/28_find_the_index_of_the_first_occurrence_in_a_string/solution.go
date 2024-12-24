package main

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	hlen := len(haystack)
	nlen := len(needle)

	for i := 0; i <= hlen-nlen; i++ {
		if haystack[i:i+nlen] == needle {
			return i
		}
	}

	return -1
}
