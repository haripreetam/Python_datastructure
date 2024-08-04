def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example usage
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff = symmetric_difference(set1, set2)
print(sym_diff)  # Output: {1, 2, 4, 5}
