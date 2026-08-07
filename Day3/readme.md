# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

A substring is a contiguous sequence of characters within a string.

---

## Examples

### Example 1

**Input:**
```
s = "abcabcbb"
```

**Output:**
```
3
```

**Explanation:**
The longest substring without repeating characters is `"abc"`, which has a length of **3**.

---

### Example 2

**Input:**
```
s = "bbbbb"
```

**Output:**
```
1
```

**Explanation:**
The longest substring without repeating characters is `"b"`, which has a length of **1**.

---

## Algorithm

1. Create an empty set to store unique characters.
2. Initialize two pointers:
   - `left = 0`
   - `max_length = 0`
3. Traverse the string using the `right` pointer.
4. If the current character already exists in the set:
   - Remove characters from the left side until the duplicate is removed.
   - Move the `left` pointer forward.
5. Add the current character to the set.
6. Update the maximum length using:
   ```
   max_length = max(max_length, right - left + 1)
   ```
7. Continue until the end of the string.
8. Return `max_length`.

---

## Python Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```

---

## Time Complexity

- **O(n)**
- Each character is visited at most twice (once by the `right` pointer and once by the `left` pointer).

---

## Space Complexity

- **O(min(n, m))**
- `n` = Length of the string.
- `m` = Number of unique characters in the character set.

---

## Conclusion

This solution uses the **Sliding Window** technique to efficiently find the longest substring without repeating characters. By maintaining a window of unique characters and adjusting it whenever a duplicate is found, the algorithm achieves **O(n)** time complexity, making it optimal for this problem.