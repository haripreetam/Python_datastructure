def print_table(dictionary):
    print("Key\tValue\tend")
    print("----\t-----")
    for key, value in dictionary.items():
        print(f"{key}\t{value}")

dictionary = {'a': 1, 'b': 2, 'c': 3}
print_table(dictionary)
