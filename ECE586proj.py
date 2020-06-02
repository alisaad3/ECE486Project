# -*- coding: utf-8 -*-
"""
Created on Fri May 22 02:03:35 2020

@author: disha
"""

op = " "
BITS = bin(32)
f = open("sample_memory_image.txt", "r")            # Open and Read contents inside of file 

for x in f:                                         # Name The contents in the file x, loop through file line by line

    scale = 16                                      # equals to hexaddecimal

    num_of_bits = 32                                # Number of bits is 32 per line 

    y = bin(int(x, scale))[2:].zfill(num_of_bits)   #Conver Hex to Binary

    print(y)    
trace = []  # list that tracks all the instructions and memory values from input trace
reg = {}  # dictionary that keeps track of all the register number and values 

for temp in range(0, 32):

    reg[temp] = 0

rtype = ['000000', '000010', '000100', '000110', '001000', '001010']  # list with all r-type instruction opcodes

itype = ['000001', '000011', '000101', '000111', '001001', '001011', '001100','001101','001110', '001111','010000','010001']  # list with all i-type instruction opcodes

arith = ['000000', '000001', '000010', '000011', '000100', '000101']  # list with all arithmetic opcodes

logic = ['000110', '000111', '001000', '001001', '001010', '001011']  # list with all logic opcodes

mem = ['001100', '001101']  # list with all memory instruction opcodes

cont = ['001110', '001111', '010000']  # list with all control instruction opcodes

ADD = rtype[0]
SUB = rtype[1]
AND = rtype[4]
MUL = rtype[2]
OR = rtype[3]
XOR = rtype[5]

ADDI= itype[0]
SUBI = itype[1]
MULI= itype[2]
ORI = itype[3]
ANDI = itype[4]
XORI = itype[5]
LDW = itype[6]
STW = itype[7]
BZ = itype[8]
BEQ = itype[9]
JR = itype[9]
HALT = itype[10]

for op in rtype:
    opcode = BITS[0:6]
    Rs = BITS[6:11]
    Rt = BITS[11:16]
    Rd = BITS[16:21]
    
for op in itype:
    opcode = BITS[0:6]
    Rs = BITS[6:11]
    Rt = BITS[11:16]
    imm = BITS[16:]
    
#add rd, rs ,rt 
if op == ADD:
    reg[Rd] = reg[Rs] + reg[Rt]
elif op == SUB:
    reg[Rd] = reg[Rs] - reg[Rt]
elif op == AND:
    reg[Rd] = reg[Rs] & reg[Rt]
elif op == MUL:
    reg[Rd] = reg[Rs] & reg[Rt]
elif op == OR:
    reg[Rd] = reg[Rs] | reg[Rt]
elif op == XOR:
    reg[Rd] = reg[Rs] ^ reg[Rt]
elif op == ADDI:
    reg[Rt] = reg[Rs] + imm
elif op == SUBI:
    reg[Rt] = reg[Rs] - imm
elif op == MULI:
    reg[Rt] = reg[Rs] * imm
elif op == ANDI:
    reg[Rt] = reg[Rs] & imm
elif op == ORI:
    reg[Rt] = reg[Rs] | imm
elif op == XORI:
    reg[Rt] = reg[Rs] ^ imm


#elif op == LDW:
 #   reg[Rt] = reg[Rs]  imm
#elif op == STW:
    
