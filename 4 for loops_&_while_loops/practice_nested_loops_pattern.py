# Variant 1:
steps = 6
for r in range(steps):
    print("#", end="")
    for c in range(r):
        print(" ", end="")
    print("#")

# Variant 2:
stepS = 6
for m in range(stepS):
    print('#' + (' ' * m) + '#')