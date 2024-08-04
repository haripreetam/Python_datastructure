def count_list_items(dictionary):
    count = 0
    for value in dictionary.values():
        #print(value)
        if isinstance(value, list):
            count += len(value)
            #print(count)
    return count

dictionary = {'a': [1, 2, 3], 'b': 'hello', 'c': [4, 5]}



print(count_list_items(dictionary))

