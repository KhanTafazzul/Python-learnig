# Problem 3: Two Sum (The Two-Pointer Pattern)
#
# Description:
# Given a sorted list of integers and a target sum, find if there are two 
# numbers in the list that add up to the target. If found, return them as 
# a tuple (num1, num2). If not found, return None.
#
# Rules:
# - The input list is guaranteed to be sorted in ascending order.
# - Do not use nested loops (O(N^2) complexity). Use the O(N) Two-Pointer technique.
#
# ==============================================================================
# LOGIC EXPLANATION:
# 1. Pointer Placement:
#    - Set 'left' pointer at the start (index 0) and 'right' pointer at the end (len - 1).
# 2. Convergence Loop (while left < right):
#    - Calculate 'current_sum = sorted_list[left] + sorted_list[right]'.
#    - If current_sum == target: match found, return (sorted_list[left], sorted_list[right]).
#    - If current_sum < target: need a larger sum, so move left pointer forward (left += 1).
#    - If current_sum > target: need a smaller sum, so move right pointer backward (right -= 1).
# 3. Fallback:
#    - If pointers meet without finding a matching pair, return None.
# ==============================================================================

def find_pair_with_sum(sorted_list, target):
    # Initialize boundary pointers
    left = 0
    right = len(sorted_list) - 1

    # Shrink search window from both ends
    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]

        if current_sum == target:
            return (sorted_list[left], sorted_list[right])
        elif current_sum < target:
            left += 1   # Increase sum by moving rightward
        else:
            right -= 1  # Decrease sum by moving leftward

    # No valid pair found
    return None


# --- Test Section ---
if __name__ == "__main__":
    numbers = [1, 2, 4, 6, 8, 10, 13]
    target_1 = 14  # 1 + 13 = 14 or 4 + 10 = 14 (finds 1, 13)
    target_2 = 7   # 1 + 6 = 7
    target_3 = 25  # No pair

    print(f"Target 14: Pair is {find_pair_with_sum(numbers, target_1)}")  # Expected: (1, 13)
    print(f"Target 7:  Pair is {find_pair_with_sum(numbers, target_2)}")  # Expected: (1, 6)
    print(f"Target 25: Pair is {find_pair_with_sum(numbers, target_3)}")  # Expected: None

