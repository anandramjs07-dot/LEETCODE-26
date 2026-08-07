# Add Two Numbers (Linked List)

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zeros, except the number 0 itself.

### Example

**Input:**
```
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output:**
```
[7,0,8]
```

**Explanation:**
```
342 + 465 = 807
```

---

## Algorithm

1. Create a dummy node to store the result.
2. Initialize a pointer (`current`) to the dummy node.
3. Initialize `carry = 0`.
4. Traverse both linked lists until both lists and the carry become empty.
5. Read the current values from both lists. If a list has ended, consider its value as 0.
6. Calculate:
   ```
   total = value1 + value2 + carry
   ```
7. Update the carry:
   ```
   carry = total // 10
   ```
8. Create a new node with:
   ```
   total % 10
   ```
   and attach it to the result list.
9. Move the pointers of both linked lists to the next node.
10. Return `dummy.next`, which is the head of the resulting linked list.

---

## Python Code

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

## Time Complexity

- **O(max(n, m))**
- We traverse each linked list only once.

## Space Complexity

- **O(max(n, m))**
- A new linked list is created to store the result.

---

## Conclusion

This solution efficiently adds two numbers represented as linked lists by traversing both lists simultaneously while maintaining a carry value. It handles linked lists of different lengths and any remaining carry after the final addition.