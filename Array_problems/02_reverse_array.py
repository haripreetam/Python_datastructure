import array

def reverse_array(arr):
    return arr[::-1]

arr = array.array('i', [1, 2, 3, 4, 5])
reversed_arr = reverse_array(arr)
print(reversed_arr)
