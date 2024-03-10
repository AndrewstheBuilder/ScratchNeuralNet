from normalized import normalize

l = [10, 9, 80, 29, 49]
norm_input = normalize(l)
print('l',l)
separator = " "
print('norm_input',separator.join(map(str, norm_input)))