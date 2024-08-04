def add_ing(s):
    if len(s) < 3:
        return s
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

print(add_ing("jump"))
print(add_ing("tooning"))
print(add_ing("ab"))
