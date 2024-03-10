from variance import variance

def normalize(l):
    var = variance(l)
    normalized_l = (x/var for x in l)
    return normalized_l