def find_common_items(list1, list2):
    return list(set(list1) & set(list2))

list_1 = [1,2,3,4,5,6]
list_2 = [34,23,56,89,5,6]
print(find_common_items(list_1,list_2))