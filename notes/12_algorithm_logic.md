# 🧠 Python Core: Advanced Problem Solving & Algorithm Logic

Algorithmic logic is about designing step-by-step procedures to solve complex problems efficiently. Instead of relying purely on built-in helper functions, you learn patterns that allow you to manipulate data structures directly.

---

## 1. Core Algorithmic Patterns

### Pattern A: The Frequency Counter
This pattern uses a dictionary to keep track of how many times different items (like letters, numbers, or words) appear in a sequence. It is much faster than running nested loops to count items.

*   **Logic:** Loop through the list/string. For each item:
    *   If it is already in the dictionary, increment its count by 1.
    *   If it is not in the dictionary, add it with a count of 1.
*   **Example:**
    ```python
    def count_frequencies(items):
        freq = {}
        for item in items:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

    print(count_frequencies(["apple", "banana", "apple", "cherry", "banana", "apple"]))
    # Output: {'apple': 3, 'banana': 2, 'cherry': 1}
    ```

---

### Pattern B: Manual Search & Peak Finding (Min/Max)
Instead of using `min()`, `max()`, or `sort()`, you track a running "best" value by iterating through a sequence exactly once.

*   **Logic (Finding Maximum):**
    *   Initialize `max_val` to the first element of the list.
    *   Loop through the rest of the list.
    *   If the current element is larger than `max_val`, update `max_val` to the current element.
*   **Example:**
    ```python
    def find_maximum(numbers):
        if not numbers:
            return None
        max_val = numbers[0]
        for num in numbers:
            if num > max_val:
                max_val = num
        return max_val
    ```

---

### Pattern C: Two-Pointer Sum Search
When searching for a pair of values in a sorted list that meet a condition (like adding up to a target number), you place one pointer at the start and one at the end.

*   **Logic:**
    *   Set `left = 0` and `right = len(list) - 1`.
    *   While `left < right`:
        *   Calculate the current sum: `current_sum = list[left] + list[right]`.
        *   If `current_sum == target`, you found the pair!
        *   If `current_sum < target`, move the `left` pointer to the right (to increase the sum).
        *   If `current_sum > target`, move the `right` pointer to the left (to decrease the sum).
*   **Example:**
    ```python
    def has_target_sum(sorted_numbers, target):
        left = 0
        right = len(sorted_numbers) - 1
        
        while left < right:
            current_sum = sorted_numbers[left] + sorted_numbers[right]
            if current_sum == target:
                return (sorted_numbers[left], sorted_numbers[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None
    ```

---

## 2. Tips for Effective Problem Solving
1.  **Understand the Inputs & Outputs:** What type of data is coming in? (Is it a list? Are there negative numbers?) What should it return? (A list, a boolean, or print the result?)
2.  **Dry Run with Simple Examples:** Test your logic on paper with a small list (e.g. `[1, 2, 3]`) before writing the code.
3.  **Trace Edge Cases:** Think about what happens if the input list is empty `[]` or has only one element.
