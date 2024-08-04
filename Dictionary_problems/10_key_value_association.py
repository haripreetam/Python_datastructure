def count_success(dict_list):
    success_count = 0
    for d in dict_list:
        if d.get('success') == True:
            success_count += 1
        
    return success_count,d

sample_data = [{'id': 1, 'success': True, 'name': 'hari'},
               {'id': 2, 'success': True, 'name': 'chinmay'},
               {'id': 3, 'success': False, 'name': 'ajinkya'}]
print(count_success(sample_data))
