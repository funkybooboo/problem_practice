use std::env;

struct Solution;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }

        // Mapping digits to letters as on a telephone keypad
        let mapping: Vec<Vec<char>> = vec![
            vec![],             // index 0 (unused, as 1 doesn't map to letters)
            vec![],             // index 1 (unused)
            vec!['a', 'b', 'c'], // 2
            vec!['d', 'e', 'f'], // 3
            vec!['g', 'h', 'i'], // 4
            vec!['j', 'k', 'l'], // 5
            vec!['m', 'n', 'o'], // 6
            vec!['p', 'q', 'r', 's'], // 7
            vec!['t', 'u', 'v'], // 8
            vec!['w', 'x', 'y', 'z'], // 9
        ];

        // Helper function for backtracking
        fn backtrack(digits: &str, start: usize, current: &mut String, result: &mut Vec<String>, mapping: &Vec<Vec<char>>) {
            if start == digits.len() {
                result.push(current.clone()); // Add the combination to the result
                return;
            }

            let digit = digits[start..start + 1].parse::<usize>().unwrap(); // Get the current digit
            for &letter in &mapping[digit] {
                current.push(letter); // Try the letter
                backtrack(digits, start + 1, current, result, mapping); // Recurse for the next digit
                current.pop(); // Backtrack
            }
        }

        let mut result = Vec::new();
        let mut current = String::new();
        backtrack(&digits, 0, &mut current, &mut result, &mapping);

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    // Test case for empty input
    #[test]
    fn test_empty_input() {
        assert_eq!(Solution::letter_combinations("".to_string()), Vec::<String>::new());
    }

    // Test case for a single digit "2"
    #[test]
    fn test_single_digit_2() {
        let expected = vec!["a", "b", "c"];
        assert_eq!(Solution::letter_combinations("2".to_string()), expected);
    }

    // Test case for a single digit "9" (maximum letters for a digit)
    #[test]
    fn test_single_digit_9() {
        let expected = vec!["w", "x", "y", "z"];
        assert_eq!(Solution::letter_combinations("9".to_string()), expected);
    }

    // Test case for two digits: "23"
    #[test]
    fn test_two_digits_23() {
        let expected = vec!["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"];
        assert_eq!(Solution::letter_combinations("23".to_string()), expected);
    }

    // Test case for two digits: "79"
    #[test]
    fn test_two_digits_79() {
        let expected = vec!["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"];
        assert_eq!(Solution::letter_combinations("79".to_string()), expected);
    }

    // Test case for multiple digits: "234"
    #[test]
    fn test_multiple_digits_234() {
        let expected = vec![
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi",
        ];
        assert_eq!(Solution::letter_combinations("234".to_string()), expected);
    }

    // Test case for digits "7" and "9"
    #[test]
    fn test_seven_and_nine() {
        let expected = vec![
            "pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"
        ];
        assert_eq!(Solution::letter_combinations("79".to_string()), expected);
    }


    // Test case for "2345" with larger input
    #[test]
    fn test_large_input() {
        let expected = vec![
            "adgj", "adgk", "adgl", "adhj", "adhk", "adhl", "adij", "adik", "adil", 
            "aegj", "aegk", "aegl", "aehj", "aehk", "aehl", "aeij", "aeik", "aeil", 
            "afgj", "afgk", "afgl", "afhj", "afhk", "afhl", "afij", "afik", "afil", 
            "bdgj", "bdgk", "bdgl", "bdhj", "bdhk", "bdhl", "bdij", "bdik", "bdil", 
            "begj", "begk", "begl", "behj", "behk", "behl", "beij", "beik", "beil", 
            "bfgj", "bfgk", "bfgl", "bfhj", "bfhk", "bfhl", "bfij", "bfik", "bfil", 
            "cdgj", "cdgk", "cdgl", "cdhj", "cdhk", "cdhl", "cdij", "cdik", "cdil", 
            "cegj", "cegk", "cegl", "cehj", "cehk", "cehl", "ceij", "ceik", "ceil", 
            "cfgj", "cfgk", "cfgl", "cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"
        ];
        assert_eq!(Solution::letter_combinations("2345".to_string()), expected);
    }
}

fn main() {
    // Get command line arguments
    let args: Vec<String> = env::args().collect();

    // Check if a digit string is provided
    if args.len() < 2 {
        eprintln!("Please provide a string of digits (2-9) as an argument.");
        return;
    }

    // Get the digits string from the arguments
    let digits = &args[1];

    // Call the function to get the letter combinations
    let result = Solution::letter_combinations(digits.to_string());

    // Print the result
    if result.is_empty() {
        println!("No letter combinations available.");
    } else {
        println!("Letter combinations for '{}':", digits);
        for combination in result {
            println!("{}", combination);
        }
    }
}

