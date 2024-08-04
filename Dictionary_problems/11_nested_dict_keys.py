def list_to_nested_dict(list1):
    nested_dict = current = {}
    for item in list1:
        current[item] = {}
        current = current[item]
    return nested_dict

list1 = [1, 2, 3, 4]
print(list_to_nested_dict(list1))
