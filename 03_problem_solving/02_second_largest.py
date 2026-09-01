# Problem 2: Find the Second Largest Element (Running Max Pattern)
#
# Description:
# Given a list of numbers, find the second largest element in a single pass 
# (one loop) without sorting the list or using built-in sort functions.
#
# Rules:
# - Do not use list.sort(), sorted(), or max().
# - Handle edge cases: if the list has less than 2 unique elements, return None.
#
# ==============================================================================
# LOGIC EXPLANATION:
# 1. Edge Case Validation:
#    - If the list has fewer than 2 elements, a second largest element cannot exist.
# 2. Tracking Running Maximums:
#    - Initialize 'largest' and 'second_largest' to negative infinity (-inf).
#    - Loop through each number:
#      - If num > largest: demote current 'largest' to 'second_largest', then set 'largest' = num.
#      - Else if num > second_largest and num != largest: update 'second_largest' = num.
# 3. Final Verification:
#    - If 'second_largest' remains -inf (e.g., all elements are identical), return None.
#    - Otherwise, return 'second_largest'.
# ==============================================================================

def find_second_largest(numbers):
    # Edge case: list must contain at least 2 items
    if len(numbers) < 2:
        return None

    # Initialize trackers to negative infinity to support negative numbers
    largest = float('-inf')
    second_largest = float('-inf')

    # Single-pass iteration O(N)
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    # Return None if no distinct second largest exists; otherwise return the value
    if second_largest == float('-inf'):
        return None
    return second_largest


# --- Test Section ---
if __name__ == "__main__":
    test_list_1 = [12, 35, 1, 10, 34, 1]
    test_list_2 = [10, 10, 10]
    test_list_3 = [5]

    print(f"List 1: {test_list_1} -> Second Largest: {find_second_largest(test_list_1)}")  # Expected: 34
    print(f"List 2: {test_list_2} -> Second Largest: {find_second_largest(test_list_2)}")  # Expected: None
    print(f"List 3: {test_list_3} -> Second Largest: {find_second_largest(test_list_3)}")  # Expected: None
