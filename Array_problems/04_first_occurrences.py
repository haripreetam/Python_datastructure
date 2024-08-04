import array

def remove_first_occurrence(arr, element):
    try:
        arr.remove(element)
    except ValueError:
        print(f"element {element} not found in array.")
    return arr

arr = array.array('i', [1, 2, 3, 4, 2, 5])
element = 0
updated_arr = remove_first_occurrence(arr, element)
print(updated_arr)
