import math

comps = 20
fact = math.factorial(comps)

configs = 0

for i in range(2,21):
    binom = fact / (math.factorial(i)*math.factorial(20-i))
    configs = configs + binom

print(configs)