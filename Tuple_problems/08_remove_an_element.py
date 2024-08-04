my_tuple = (1, 2, 3, 4, 5)
item_to_remove = 3

my_tuple = tuple(item for item in my_tuple if item != item_to_remove)
print(my_tuple)
