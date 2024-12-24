package main

import (
	"testing"
)

func TestStrStrFirstOccurrenceAtStart(t *testing.T) {
	haystack := "sadbutsad"
	needle := "sad"
	want := 0
	got := strStr(haystack, needle)
	if got != want {
		t.Errorf("strStr(%q, %q) = %d; want %d", haystack, needle, got, want)
	}
}

func TestStrStrNeedleNotFound(t *testing.T) {
	haystack := "leetcode"
	needle := "leeto"
	want := -1
	got := strStr(haystack, needle)
	if got != want {
		t.Errorf("strStr(%q, %q) = %d; want %d", haystack, needle, got, want)
	}
}

func TestStrStrFirstOccurrenceInMiddle(t *testing.T) {
	haystack := "hello"
	needle := "ll"
	want := 2
	got := strStr(haystack, needle)
	if got != want {
		t.Errorf("strStr(%q, %q) = %d; want %d", haystack, needle, got, want)
	}
}

func TestStrStrNeedleNotPresent(t *testing.T) {
	haystack := "aaaaa"
	needle := "bba"
	want := -1
	got := strStr(haystack, needle)
	if got != want {
		t.Errorf("strStr(%q, %q) = %d; want %d", haystack, needle, got, want)
	}
}

func TestStrStrEmptyHaystackAndNeedle(t *testing.T) {
	haystack := ""
	needle := ""
	want := 0
	got := strStr(haystack, needle)
	if got != want {
		t.Errorf("strStr(%q, %q) = %d; want %d", haystack, needle, got, want)
	}
}
