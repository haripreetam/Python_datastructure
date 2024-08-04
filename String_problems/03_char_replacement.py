def change_char(s):
    first_char = s[0]
    result = first_char
    for char in s[1:]:
        if char == first_char:
            result += '$'
        else:
            result += char
    return result

print(change_char("cricket"))

# def change_char(s):
#     first_char = s[0]
#     modified_str = first_char + s[1:].replace(first_char, '$')
#     return modified_str

# print(change_char("restart"))
