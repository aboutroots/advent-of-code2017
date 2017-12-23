def get_value(operand, regs):
    if operand.isalpha():
        return regs[operand]
    return int(operand)


def run(instrs, reg, start_i, received_buffer):
    send_buffer = []
    i = start_i
    try:
        while True:
            ins = instrs[i].split()
            if ins[0] == 'snd':
                send_buffer.append(get_value(ins[1], reg))

            elif ins[0] == 'set':
                reg[ins[1]] = get_value(ins[2], reg)

            elif ins[0] == 'add':
                reg[ins[1]] += get_value(ins[2], reg)

            elif ins[0] == 'mul':
                reg[ins[1]] *= get_value(ins[2], reg)

            elif ins[0] == 'mod':
                reg[ins[1]] %= get_value(ins[2], reg)

            elif ins[0] == 'rcv':
                if len(received_buffer):
                    reg[ins[1]] = received_buffer[0]
                    del received_buffer[0]
                else:
                    return i, send_buffer[:]

            if ins[0] == 'jgz':
                if get_value(ins[1], reg) > 0:
                    i += get_value(ins[2], reg)
                else:
                    i += 1
            else:
                i += 1
    except IndexError:
        return


if __name__ == "__main__":
    with open('day18.txt') as file:
        instructions = [x.rstrip('\n') for x in file.readlines()]
    registers0 = dict()
    # init registers
    for i in instructions:
        reg_name = i.split()[1]
        if reg_name.isalpha():
            registers0[reg_name] = 0

    registers1 = dict(registers0)
    registers1['p'] = 1
    i_0, i_1,send_0, send_1 = 0, 0, [], []

    globl_prog1_send = 0

    while True:
        # program 0
        i_0, send_0 = run(instructions, registers0, i_0, send_1)
        # program 1
        i_1, send_1 = run(instructions, registers1, i_1, send_0)
        globl_prog1_send += len(send_1)
        if not len(send_1):
            break
    print(globl_prog1_send)
