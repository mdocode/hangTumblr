from random import random, shuffle

def random_items(iterable, k=1):
    result = [None] * k
    for i, item in enumerate(iterable):
        if i < k:
            result[i] = item
        else:
            j = int(random() * (i+1))
            if j < k:
                result[j] = item
    shuffle(result)
    return result
