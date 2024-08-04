import array

def count_occurrences(arr, element):
    return arr.count(element)

arr = array.array('i', [1, 2, 3, 4, 2, 2, 5])
element = 2
occurrences = count_occurrences(arr, element)
print(occurrences)
