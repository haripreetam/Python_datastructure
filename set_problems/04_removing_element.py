def remove_items(input_set, items_to_remove):
    input_set.difference_update(items_to_remove)
    return input_set

my_set = {1, 2, 3, 4}
items_to_remove = {3, 4, 7}
updated_set = remove_items(my_set, items_to_remove)
print(updated_set)
