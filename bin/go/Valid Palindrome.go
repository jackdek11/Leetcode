package main

import (
    "strings"
)

func isPalindrome(s string) bool {
    // Convert the string to lowercase
    s = strings.ToLower(s)

    // Remove all non-alphanumeric characters from the string
    var alphanumericStr strings.Builder
    for _, ch := range s {
        if ('a' <= ch && ch <= 'z') || ('0' <= ch && ch <= '9') {
            alphanumericStr.WriteRune(ch)
        }
    }

    // Get the modified string without non-alphanumeric characters
    modifiedStr := alphanumericStr.String()

    // Compare the modified string with its reverse to check for a palindrome
    return modifiedStr == reverse(modifiedStr)
}

// Function to reverse a string
func reverse(s string) string {
    runes := []rune(s)
    n := len(runes)
    for i := 0; i < n/2; i++ {
        runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
    }
    return string(runes)
}