def remove_elements(input_list):

    print([item for indx, item in enumerate(input_list) if indx in [0, 4, 5]])


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
expected_output = remove_elements(sample_list)

#print(expected_output)  # Output: ['Green', 'White', 'Black']
