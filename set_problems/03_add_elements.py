def add_members(input_set, new_members):
    input_set.update(new_members)
    return input_set

# Example usage
my_set = {1, 2, 3}
new_members = {4, 5, 6, 7}
updated_set = add_members(my_set, new_members)
print(updated_set)  # Output: {1, 2, 3, 4, 5}
