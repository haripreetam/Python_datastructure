import array

def create_and_display_array():
    arr = array.array('i', [1, 2, 3, 4, 5])
    for i in range(len(arr)):
        print(f"Element at index {i}: {arr[i]}")

create_and_display_array()
