
sample_dict = {0: 30, 1: 10, 2: 20}

def value(item):
    # print(item[0])
    return item[1] 

sorted_dict_asc = dict(sorted(sample_dict.items(),key=value))
sorted_dict_dec = dict(sorted(sample_dict.items(),key=value, reverse=True))
#if omitting "key=value" gives based on key sorting
#writing it will give the value based sorting

print("Ascending order:", sorted_dict_asc)
print("Ascending order:", sorted_dict_dec)