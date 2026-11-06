import random as rnd

def generate_sample(n, low=1, high=100):
    sample = []
    for i in range(n):
        sample.append(rnd.randint(low,high))

    return sample

def summary(sample):
    max_num = max(sample)
    min_num = min(sample)
    avg = 0
    for i in sample:
        avg += i

    avg /= float(len(sample))
    return (max_num, min_num , round(avg, 2))
