import tqdm


def get_value(operand, regs):
    if operand.isalpha():
        return regs[operand]
    return int(operand)


def run(instrs, reg):
    i = 0
    counter = 0
    try:
        while True:
            ins = instrs[i].split()

            if ins[0] == 'set':
                reg[ins[1]] = get_value(ins[2], reg)

            elif ins[0] == 'sub':
                reg[ins[1]] -= get_value(ins[2], reg)

            elif ins[0] == 'mul':
                reg[ins[1]] *= get_value(ins[2], reg)
                counter += 1

            if ins[0] == 'jnz':
                if get_value(ins[1], reg) != 0:
                    i += get_value(ins[2], reg)
                else:
                    i += 1
            else:
                i += 1
    except IndexError:
        return counter


def optimized_run():
    h = 0
    for b in tqdm.tqdm(range(109300, 126300+1, 17)):
        f = True
        for d in range(2, b+1):
            for e in range(2, b+1):
                if d * e == b:
                    f = False
                    break
                if d * e > b:
                    break
            if not f:
                break
        if not f:
            h += 1
    print(h)



if __name__ == "__main__":
    with open('day23.txt') as file:
        instructions = [x.rstrip('\n') for x in file.readlines()]
    registers = dict()
    # init registers
    for i in instructions:
        reg_name = i.split()[1]
        if reg_name.isalpha():
            registers[reg_name] = 0
    registers['a'] = 1


    # print(run(instructions, registers))
    optimized_run()