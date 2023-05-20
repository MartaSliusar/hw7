import random
def common_elements(n1, n2):
    l1 = []
    l2 = []
    while len(l1) != n1:
        number = random.randint(0, 100)
        if number % 3 == 0:
            l1.append(number)
    while len(l2) != n2:
        number = random.randint(0, 100)
        if number % 5 == 0:
            l2.append(number)
    return set(l1) & set(l2)

print(common_elements(20, 25))
