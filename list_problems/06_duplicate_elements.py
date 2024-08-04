def remove_duplicates(input_list):
    return (set(input_list))
    # return list(set(input_list))

sample_list = [1, 2, 3, 2, 4, 1, 5]
unique_list = remove_duplicates(sample_list)
print(unique_list)
