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
    global ain, lin, memin, contin, stallsf, f
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

while True:
    curr = trace[int(pc / 4)]
   
    if curr[:6] == '010001':  # HALT
        contin += 1  # incrementing control instruction count
        pc += 4  # updating program counter
        break
    elif curr[:6] in arith:  # checking if current instruction is arithmetic operation
        ain += 1  # incrementing arithmetic instruction count
        pc += 4  # updating program counter
        break
    elif curr[:6] in logic:  # checking if current instruction is logical operation
        lin += 1  # incrementing logical instruction count
        pc += 4  # updating program counter
        break
    elif curr[:6] in mem:  # checking if current instruction is memory operation
        memin += 1  # incrementing memory instruction count
        pc += 4  # updating program counter
        break
    elif curr[:6] in cont:  # checking if current instruction is control operation
        contin += 1  # incrementing control instruction count
    f += 1
    break
display()
