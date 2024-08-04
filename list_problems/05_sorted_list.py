def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

sample_list = [(1, 1), (2, 2), (5, 6), (4, 4), (1,3)]
sorted_list = sort_by_last_element(sample_list)
print(sorted_list)
