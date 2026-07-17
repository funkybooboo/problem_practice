package main

import (
	"testing"
)

func TestLongestCommonPrefix_FlowerFlowFlight(t *testing.T) {
	strs := []string{"flower", "flow", "flight"}
	expected := "fl"
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_NoCommonPrefix(t *testing.T) {
	strs := []string{"dog", "racecar", "car"}
	expected := ""
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_SingleString(t *testing.T) {
	strs := []string{"apple"}
	expected := "apple"
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_EmptyArray(t *testing.T) {
	var strs []string
	expected := ""
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_EmptyStringInArray(t *testing.T) {
	strs := []string{"", "flow", "flight"}
	expected := ""
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_AllIdenticalStrings(t *testing.T) {
	strs := []string{"identical", "identical", "identical"}
	expected := "identical"
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_SingleCharacterStrings(t *testing.T) {
	strs := []string{"a", "a", "a"}
	expected := "a"
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_AllEmptyStrings(t *testing.T) {
	strs := []string{"", "", ""}
	expected := ""
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}

func TestLongestCommonPrefix_AbAndA(t *testing.T) {
	strs := []string{"ab", "a"}
	expected := "a"
	got := longestCommonPrefix(strs)
	if got != expected {
		t.Errorf("longestCommonPrefix(%v) = %v; want %v", strs, got, expected)
	}
}
