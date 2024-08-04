def clone_lisr(input_list):
    a = input_list.copy()
    return a

sample_list = [1, 2, 3, 2, 4, 1, 5]
cloned_list = clone_lisr(sample_list)
print(cloned_list)