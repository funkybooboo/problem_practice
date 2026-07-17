use std::collections::HashMap;

struct Solution {
    
}

impl Solution {
    
    /// Constraints:
    /// - 1 <= s.length <= 15
    /// - s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    /// - It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    pub fn roman_to_int(s: String) -> i32 {
        let mut result = 0;
        let roman_map: HashMap<char, i32> = [
            ('I', 1), ('V', 5), ('X', 10), ('L', 50),
            ('C', 100), ('D', 500), ('M', 1000)
        ].iter().cloned().collect();
        
        let chars: Vec<char> = s.chars().collect();
        
        for i in 0..chars.len() {
            let value = roman_map[&chars[i]];
            
            if i + 1 < chars.len() {
                let next = roman_map[&chars[i + 1]];
                if value < next {
                    result -= value;
                } else {
                    result += value;
                }
            } else {
                result += value;
            }
        }
        
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_3() {
        let roman = "III".to_string();
        let result = Solution::roman_to_int(roman);
        assert_eq!(result, 3);
    }

    #[test]
    fn test_58() {
        let roman = "LVIII".to_string();
        let result = Solution::roman_to_int(roman);
        assert_eq!(result, 58);
    }

    #[test]
    fn test_1994() {
        let roman = "MCMXCIV".to_string();
        let result = Solution::roman_to_int(roman);
        assert_eq!(result, 1994);
    }
}

fn main() {
    
}
