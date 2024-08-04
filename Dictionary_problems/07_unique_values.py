def unique_values(dict_list):
    unique_vals = set()
    for d in dict_list:
        for value in d.values():
            unique_vals.add(value)
    return unique_vals
dict_list = [{"k1":"1"},{"k2":"2"},{"k3":"3"},{"k4":"4"},{"k5":"4"},{"k6":"6"}]
print(unique_values(dict_list))
