import random

def f_A():
    r = random.random()
    if r <= 0.48:
        return 1
    else:
        return -1

def f_B(money):

    if money % 3 == 0:
        r = random.random()
        if r <= 0.01:
            return 1
        else:
            return -1
    else:
        r = random.random()
        if r <= 0.85:
            return 1
        else:
            return -1

money = 0
num = 1000000
for i in range(num):
    r = random.random()
    if r <= 0.5:
        money += f_A()
    else:
        money += f_B(money)
        
print(money / num)
        