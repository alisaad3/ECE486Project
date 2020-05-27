"""
ECE 486/586 Project
Authors: POOJA GOPALAKRISHNAN
         ALI SAAD
         DISHA SHETTY
Objective: To implement MIPS instructions with functional and timing simulations.
"""
pc = 0  # variable to track program counter value
ain = 0  # variable to track count of arithmetic instructions
lin = 0  # variable to track count of logical instructions
memin = 0  # variable to track count of memory instructions
contin = 0  # variable to track count of control instructions
imm = 0  # variable that tracks immediate value for current instructions
stalls = 0  # variable to track count of stalls without forwarding
stallsf = 0  # variable to track count of stalls with forwading
penal = 0  # variable to track count of penalties from branches
trace = []  # list that tracks all the instructions and memory values from input trace
curr = ''  # variable that tracks current instruction from trace
bf = {}  # dictionary that keeps track of branch flags
f = 0      # flag
raw = {}  # dictionary that keeps track of raw hazard occurances
bran = {}  # to track branches leading to penalties
memst = {}  # dictionary that keeps all the updated memory locations and their content
reg = {}  # dictionary that keeps track of all the register number and values
for temp in range(0, 32):
    reg[temp] = 0
rtype = ['000000', '000010', '000100', '000110', '001000', '001010']  # list with all r-type instruction opcodes
itype = ['000001', '000011', '000101', '000111', '001001', '001011']  # list with all i-type instruction opcodes
arith = ['000000', '000001', '000010', '000011', '000100', '000101']  # list with all arithmetic opcodes
logic = ['000110', '000111', '001000', '001001', '001010', '001011']  # list with all logic opcodes
mem = ['001100', '001101']  # list with all memory instruction opcodes
cont = ['001110', '001111', '010000']  # list with all control instruction opcodes

# Block that reads all instructions and memory values from input trace
lf = [l.rstrip('\n') for l in
      open(r"C:\Users\pooja\Downloads\proj_trace.txt")]
for temp in lf:
    trace.append(str(bin(int(temp, 16)))[2:].zfill(32))

# To display the final results
def display():
    global reg, ain, lin, memin, contin, stallsf, f
    print('Total no. of cycles(without forwarding): ', f + 5 + stalls + penal)
    print("Total no. of cycles(with forwarding): ", f + 5 + stallsf + penal)
    print('Stalls: ', stalls)
    print('Stallsf: ', stallsf)
    print('Penalties because of branches: ', penal)
    print('Single stalls: ')
    print('Double stalls: ')
    print('No. of RAW hazards: ', len(raw))
    print('No. of branches leading to penalties: ', len(bran))
    
    print('Instruction counts are as follows:')
    print('Total instructions: ', ain + lin + memin + contin)
    print('Arithmetic instructions: ', ain)
    print("Logical instructions: ", lin)
    print('Memory instructions: ', memin)
    print('Control instructions: ', contin)
    
    
    print('Final register states are as follows:')
    for ite, val in reg.items():
        print(ite, ':', val)
    print('Program counter: ', pc)

    print('Final memory state->')
    for ite, val in memst.items():
        print('Address: ', ite, ', Contents: ', val)

# To immplement two's complement
def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val


# To decode value for immediate operands
def imme():
    global curr, imm
    imm = twos_comp(int(curr[16:], 2), len(curr[16:]))


# To implement arithmetic operations in functional simulation
def arit():
    global reg, imm, curr
    if curr[:6] == '000000':  # ADD
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] + reg[int(curr[11:16], 2)]
        return
    elif curr[:6] == '000010':  # SUB
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] - reg[int(curr[11:16], 2)]
        return
    elif curr[:6] == '000100':  # MUL
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] * reg[int(curr[11:16], 2)]
        return
    else:
        imme()
        if curr[:6] == '000001':  # ADDI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] + imm
            return
        elif curr[:6] == '000011':  # SUBI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] - imm
            return
        elif curr[:6] == '000101':  # MULI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] * imm
            return


# To implement logical operations in functional simulation
def logi():
    global reg, imm, curr
    if curr[:6] == '000110':  # OR
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] | reg[int(curr[11:16], 2)]
        return
    elif curr[:6] == '001000':  # AND
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] & reg[int(curr[11:16], 2)]
        return
    elif curr[:6] == '001010':  # XOR
        reg[int(curr[16:21], 2)] = reg[int(curr[6:11], 2)] ^ reg[int(curr[11:16], 2)]
        return
    else:
        imme()
        if curr[:6] == '000111':  # ORI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] | imm
            return
        elif curr[:6] == '001001':  # ANDI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] & imm
            return
        elif curr[:6] == '001011':  # XORI
            reg[int(curr[11:16], 2)] = reg[int(curr[6:11], 2)] ^ imm
            return


# To implement memory operations in functional simulation
def memo():
    global reg, imm, curr
    imme()
    if curr[:6] == '001100':  # LDW
        reg[int(curr[11:16], 2)] = twos_comp(int(trace[int((reg[int(curr[6:11], 2)] + imm) / 4)], 2), 32)
        return
    elif curr[:6] == '001101':  # STW
        trace[int((reg[int(curr[6:11], 2)] + imm) / 4)] = str(bin(reg[int(curr[11:16], 2)]))[2:].zfill(32)
        memst[(reg[int(curr[6:11], 2)] + imm)] = reg[int(curr[11:16], 2)]
        return


# To implement control operations in functional simulation
def contr():
    global reg, pc, curr, bf, f
    imme()
    bf[f] = 0
    if curr[:6] == '001110':  # BZ
        if reg[int(curr[6:11], 2)] == 0:
            pc += (imm * 4)
            bf[f] = 1
        else:
            pc += 4
            return
    elif curr[:6] == '001111':  # BEQ
        if reg[int(curr[6:11], 2)] == reg[int(curr[11:16], 2)]:
            pc += (imm * 4)
            bf[f] = 1
        else:
            pc += 4
            return
    elif curr[:6] == '010000':  # JR
        pc = reg[int(curr[6:11], 2)]
        bf[f] = 1



while True:
    curr = trace[int(pc / 4)]
    bf[f] = 0
    if curr[:6] == '010001':  # HALT
        contin += 1  # incrementing control instruction count
        pc += 4  # updating program counter
        break
    elif curr[:6] in arith:  # checking if current instruction is arithmetic operation
        ain += 1  # incrementing arithmetic instruction count
        arit()
        pc += 4  # updating program counter
    elif curr[:6] in logic:  # checking if current instruction is logical operation
        lin += 1  # incrementing logical instruction count
        logi()
        pc += 4  # updating program counter
    elif curr[:6] in mem:  # checking if current instruction is memory operation
        memin += 1  # incrementing memory instruction count
        memo()
        pc += 4  # updating program counter
    elif curr[:6] in cont:  # checking if current instruction is control operation
        contin += 1  # incrementing control instruction count
        contr()
    f += 1
display()
