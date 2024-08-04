def keys_exist(dictionary, keys):
    return all(key in dictionary for key in keys)

dictionary = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'c']
print(keys_exist(dictionary, keys))

keys = ['a', 'd']
print(keys_exist(dictionary, keys))
