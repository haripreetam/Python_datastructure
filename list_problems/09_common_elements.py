def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

list_1 = [1,23,90,45,6,4,]
list_2 = [0,95,95,88,11,66,1]
print(have_common_member(list_1,list_2))