def circularly_identical(list1, list2):
    return len(list1) == len(list2) and ''.join(map(str, list2 * 2)).find(''.join(map(str, list1))) != -1
#just check the similarity while checking even if one misses break the loop
list_1 = [1,2,3,4,5,6]
list_2 = [1,2,3,4,5,6]
print(circularly_identical(list_1,list_2))