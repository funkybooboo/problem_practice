pub fn isIsogram(str: []const u8) bool {
    // Create an array of 26 booleans (one for each letter A-Z), all initialized to false
    // The [_] syntax lets Zig infer the array size from the initialization
    // The ** operator repeats the value 'false' 26 times
    var seen = [_]bool{false} ** 26;

    // Iterate through each character in the input string
    // The |c| syntax captures each character into the variable 'c'
    for (str) |c| {
        // Check if the character is an uppercase letter (A-Z)
        if (c >= 'A' and c <= 'Z') {
            // Convert the uppercase letter to an array index (0-25)
            // 'A' becomes 0, 'B' becomes 1, etc.
            const idx = c - 'A';
            // If we've already seen this letter, it's not an isogram
            if (seen[idx]) return false;
            // Mark this letter as seen
            seen[idx] = true;
        } else if (c >= 'a' and c <= 'z') {
            // Check if the character is a lowercase letter (a-z)
            // Convert the lowercase letter to an array index (0-25)
            // 'a' becomes 0, 'b' becomes 1, etc.
            const idx = c - 'a';
            // If we've already seen this letter, it's not an isogram
            if (seen[idx]) return false;
            // Mark this letter as seen
            seen[idx] = true;
        }
        // Non-alphabetic characters (spaces, hyphens, etc.) are ignored
    }

    // If we made it through the entire string without finding duplicates, it's an isogram
    return true;
}
