def reallocate(filename):
    cycles = 0
    with open(filename) as f:
        banks = [int(x) for x in f.readline().rstrip('\n').split('\t')]

    # banks = [0, 2, 7, 0]

    uniques = dict()
    uniques[tuple(banks)] = cycles
    flag = True
    distance = 0
    while flag:
        # one cycle
        cycles += 1
        bank_index, amount = max(enumerate(banks), key=lambda x: x[1])
        banks[bank_index] = 0

        for item in range(amount):
            bank_index += 1
            if bank_index == len(banks):
                bank_index = 0
            banks[bank_index] += 1

        if tuple(banks) in uniques.keys():
            distance = cycles - uniques[tuple(banks)]
            break
        else:
            uniques[tuple(banks)] = cycles

    return cycles, distance

if __name__ == "__main__":
    print(reallocate('day6.txt'))