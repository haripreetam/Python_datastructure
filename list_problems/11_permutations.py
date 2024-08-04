def generate_permutations(lst):
    def permute(current, remaining):
        if not remaining:
            result.append(current)
        else:
            for i in range(len(remaining)):
                new_current = current + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i+1:]
                permute(new_current, new_remaining)
    
    result = []
    permute([], lst)
    return result

input_list = [1, 2, 3]
permutations = generate_permutations(input_list)
print(permutations)
