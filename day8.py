import fileinput

program = []
for line in fileinput.input():
    s = line.split(' ')
    program.append((s[0], int(s[1])))

def run(program):
    visited = set()
    i_ptr = 0
    acc = 0
    while i_ptr not in visited:
        if i_ptr == len(program):
            return 0, acc
        visited.add(i_ptr)
        if program[i_ptr][0] == 'nop':
            i_ptr += 1
        elif program[i_ptr][0] == 'acc':
            acc += program[i_ptr][1]
            i_ptr += 1
        elif program[i_ptr][0] == 'jmp':
            i_ptr += program[i_ptr][1]
        else:
            raise ValueError(program[i_ptr][0])
    return -1, acc

for i in range(len(program)):
    if program[i] == 'add':
        continue
    mod_program = program.copy()
    instruction = 'nop' if program[i][0] == 'jmp' else 'jmp'
    mod_program[i] = (instruction, program[i][1])
    exit_code, acc = run(mod_program)
    if exit_code == 0:
        print('found: ' + str(acc))
        
