def remove_item_if_present(input_set, item):
    input_set.discard(item)
    return input_set

# Example usage
my_set = {1, 2, 3}
item = 3
updated_set = remove_item_if_present(my_set, item)
print(updated_set)  # Output: {1, 3}
