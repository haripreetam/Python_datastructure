def multiply_list(numbers):
    mul = 1
    for i in numbers:
        mul *= i
    return mul

numbers = [4,2,1,3,5,]
print("product of the list is:",multiply_list(numbers))