import random
n1 = random.randint(0, 10)
n2 = random.randint(30,45)

print(f"Values of n1, n2: {n1}, {n2}.")

for num in range(n1, n2, 1):
    if num % 2 != 0 or num % 3 == 0:
        continue
    print(num)