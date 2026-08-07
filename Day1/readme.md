Loop through nums once, keeping track of numbers you've already visited in a dictionary (seen).
For each number, compute its complement (what it would need to add up to target).
If that complement is already in seen, you've found your pair — return the stored index and the current index.
Otherwise, add the current number and its index to seen and keep going.

Complexity: O(n) time, O(n) space — a single pass instead of the brute-force O(n²) nested loop.

Example walkthrough with nums = [2,7,11,15], target = 9:

i=0, num=2 → complement=7, not in seen → seen={2:0}
i=1, num=7 → complement=2, is in seen → return [0, 1] 