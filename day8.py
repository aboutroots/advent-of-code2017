def make_script(filename):
    newlines = []
    with open(filename) as f:
        lines = [x.rstrip('\n') for x in f.readlines()]
        for instr in lines:
            reg_a, i_type, amount, _if, reg_b, cond, value = instr.split()
            check1 = 'if \'' + reg_a  +'\' not in registers.keys(): ' \
                      'registers[' '\'' + reg_a + '\'] = 0 \n'
            check2 = 'if \'' + reg_b + '\' not in registers.keys(): ' \
                      'registers[\'' + reg_b + '\'] = 0 \n'
            check_highest = 'if registers[' '\'' + reg_a + '\'] > highest:\n'+\
                            '   highest = registers[' '\'' + reg_a + '\']'
            newline = check1 + check2 + i_type + "(\'" + reg_a + '\', ' +\
                      amount + ") " + _if + ' registers[\'' + reg_b + '\'] ' +\
                      cond + ' ' + value + ' else do_nothing()\n' + \
                     check_highest +' \n'

            newlines.append(newline)
    file = open('day8_solved.py', 'w')
    file.write('registers = dict()\n'
               'highest = 0 \n'
               'def inc(a, b): \n'
               '    registers[a] += b \n'
               'def dec(a, b): \n'
               '    registers[a] -= b \n'
               'def do_nothing():\n'
               '    pass\n')

    for newline in newlines:
        file.write(newline)

    file.write('\nprint(max(registers.items(), key=lambda k: k[1]))')
    file.write('\nprint(highest)')

if __name__ == "__main__":
    make_script('day8.txt')