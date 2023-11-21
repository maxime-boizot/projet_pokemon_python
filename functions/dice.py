import random

def dice():
    return random.randint(-6, 6)

def doubledice():
    val = []
    val.append(random.randint(-6, 6))
    val.append(random.randint(-6, 6))
    return val