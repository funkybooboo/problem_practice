from typing import List


class Solution:
    def characterReplacement(self, string: str, max_changes: int) -> int:
        # Initialize the result variable to store the maximum length of valid substring
        max_window_size = 0

        # Create a set of unique chars in the string (since we check each char individually)
        unique_chars = set(string)

        # Iterate through each unique char in the set
        for target_char in unique_chars:
            # Initialize two pointers (left and right) and a count variable for the current char `target_char`
            target_count = 0
            left_pointer = 0

            # Iterate through the string with the right pointer
            for right_pointer in range(len(string)):
                # If the current char matches the target char, increment the count
                if string[right_pointer] == target_char:
                    target_count += 1

                # Calculate the window size and the number of non-target chars
                window_size = right_pointer - left_pointer + 1
                non_target_chars = window_size - target_count

                # Check if the number of non-target chars exceeds max_changes
                too_many_non_target_chars = non_target_chars > max_changes

                # If there are too many non-target chars, shrink the window from the left
                while too_many_non_target_chars:
                    # If the char at the left pointer is `target_char`, reduce the count
                    if string[left_pointer] == target_char:
                        target_count -= 1
                    # Move the left pointer to shrink the window
                    left_pointer += 1

                    # Recalculate the window size and non-target chars after moving the left pointer
                    window_size = right_pointer - left_pointer + 1
                    non_target_chars = window_size - target_count

                    # Recheck the predicate after updating the window
                    too_many_non_target_chars = non_target_chars > max_changes

                # Update the result with the maximum valid window length encountered
                max_window_size = max(max_window_size, window_size)

        # Return the result after checking all possible chars
        return max_window_size
