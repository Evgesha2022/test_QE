def optimize_lenses_pairs(cyclops_prescriptions):
    # Step 1: Sort the prescriptions in ascending order
    sorted_prescriptions = sorted(cyclops_prescriptions)

    # Step 2: Initialize a variable to count the minimum pairs
    min_pairs = 0

    # Step 3: Greedy approach to find the minimum pairs
    n = len(sorted_prescriptions)
    i = 0
    while i < n:
        # Find the maximum valid power for the current cyclops
        max_valid_power = sorted_prescriptions[i] + 1

        # Look for the last cyclops that can share the same lens
        j = i
        while j < n and sorted_prescriptions[j] <= max_valid_power:
            j += 1

        # Increase the count of minimum pairs
        min_pairs += 1

        # Move to the next group of cyclops with different prescriptions
        i = j

    return min_pairs


# Example usage:
cyclops_prescriptions = [1, -1, 2, 3, -3]
min_pairs = optimize_lenses_pairs(cyclops_prescriptions)
print(min_pairs)  # Output: 3

