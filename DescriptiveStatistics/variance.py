# l = [10, 9, 80, 29, 49] # std dev = 29.821
# n = len(l)
# mean = sum(l) / n
# num = 0.0
# for i in l:
#     num += (i - mean) ** 2
# variance = num/(n-1)
# std_dev = variance ** (1/2)
# print('calculated std_dev:', std_dev)
# print('true std_dev: 29.821')

def variance(l):
    n = len(l)
    mean = sum(l) / n
    variance = sum((x - mean)**2 for x in l) / n
    return variance
