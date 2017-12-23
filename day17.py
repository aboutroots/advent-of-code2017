steps = 345
counter = 0
result = 0
for i in range(1, 50000000):
    counter = (counter + steps + 1) % i
    if not counter:
        result = i
print(result)

