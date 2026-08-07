## Algorithm

1. Check if the input string is empty.
   - If it is empty, return an empty string.

2. Initialize two variables:
   - `start = 0` (starting index of the longest palindrome)
   - `end = 0` (ending index of the longest palindrome)

3. Create a helper function `expand(left, right)`:
   - Expand from the center while:
     - `left >= 0`
     - `right < len(s)`
     - `s[left] == s[right]`
   - Move `left` one step left and `right` one step right.
   - Return the length of the palindrome found.

4. Traverse each character in the string using a loop.

5. For every character, check two possible palindrome centers:
   - Odd-length palindrome using `(i, i)`
   - Even-length palindrome using `(i, i + 1)`

6. Find the longer palindrome between the two.

7. If the current palindrome is longer than the previously found longest palindrome:
   - Update the starting index:
     ```
     start = i - (length - 1) // 2
     ```
   - Update the ending index:
     ```
     end = i + length // 2
     ```

8. After checking all possible centers, return the substring:
   ```
   s[start:end + 1]
   ```

---

## Time Complexity

- **O(n²)**

## Space Complexity

- **O(1)**

---

## Conclusion

This algorithm uses the **Expand Around Center** approach. It treats each character (and the gap between two characters) as the center of a possible palindrome and expands outward while the characters match. It efficiently finds the longest palindromic substring without using extra memory.