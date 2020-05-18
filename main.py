# ECE 486 Project
# Ali Saad, Disha Shetty, Pooja
# Mips Simulation
# Professor Zeshan Chishti 


# Open memory image file and read it(take it's inputs)  
# Need to change the numbers in the file from Hex to binary
# Then parse it to get Rs, Rt, Rd intaking the correct numbers
# To run the correct operation   

f = open("sample_memory_image.txt", "r")            # Open and Read contents inside of file 
for x in f:                                         # Name The contents in the file x, loop through file line by line
    scale = 16                                      # equals to hexaddecimal
    num_of_bits = 32                                # Number of bits is 32 per line 
    y = bin(int(x, scale))[2:].zfill(num_of_bits)   #Conver Hex to Binary
    print(y)                                        # Print to make sure numbers are being converted correcctly 
    
# opcode 000000 is ADD instruction, rest of opcode instructions in Project specs pdf
# After we read in instruction goes case statment to decide the formart or  if statement

# Need to do Arithmetic Instructions

# Need to do Logiccal Instructions

# Need to do Memory Access Instructions

# Need to do Control Flow Instructions

# Need to figure out Instruction Format
# If statement is R-Type format, first 11 bits unused, 5 for RD, 5 of Rt, 5 for Rs, last 6 opcode
# Else I-type format, first 16 bits unused, 5 for Rt, 5 for Rs, last 6 opcode

# Need to do memory image

# Need to figure out how do stalling and how much to stall for no forwarding/forwarding 





# Variable Output
# All Variables need to be changed to express equation of how to get their content
Total_Number_of_Instructions = 638
Arithmetic_Instructions = 333
Logical_Instructions = 50
Memory_Access_Instructions = 103
Control_Transfer_Instructions = 152 
Program_Counter = 100
R1 = 1200 # Need to be changed to the equatiion on how to get the contents of R1
R2 = 1400 # Need to be changed to the equatiion on how to get the contents of R2
R3 = 100  # Need to be changed to the equatiion on how to get the contents of R3
R4 = 50   # Need to be changed to the equatiion on how to get the contents of R4
R5 = 50   # Need to be changed to the equatiion on how to get the contents of R5
R6 = 0    # Need to be changed to the equatiion on how to get the contents of R6
R7 = 25   # Need to be changed to the equatiion on how to get the contents of R7
R8 = 2550 # Need to be changed to the equatiion on how to get the contents of R8
R9 = 1275 # Need to be changed to the equatiion on how to get the contents of R9
R10 = 50  # Need to be changed to the equatiion on how to get the contents of R10
R11 = 50  # Need to be changed to the equatiion on how to get the contents of R11
R12 = 32  # Need to be changed to the equatiion on how to get the contents of R12
Address = 1400
Address1 = 1404
Address2 = 1408
Contents = 25
Contents1 = 2550
Contents2 = 1275

# Simulation Output
# What needs to be shown after code compliles all instructions
print("Instruction Counts: \n")
print("Total Number of Instructions:", Total_Number_of_Instructions)
print("Arithmetic Instructions:", Arithmetic_Instructions)
print("Logical Instructions:", Logical_Instructions)
print("Memory Access Instructions:", Memory_Access_Instructions)
print("Control Transfer Instructions:", Control_Transfer_Instructions, "\n\n")
print("Final Register State: \n")
print("(Contents shown in decimal number system; not in base 16. In addition, only those registers are shown whose contents change during the program) \n")
print("Program Counter:", Program_Counter)
print("R1:", R1)
print("R2:", R2)
print("R3:", R3)
print("R4:", R4)
print("R5:", R5)
print("R6:", R6)
print("R7:", R7)
print("R8:", R8)
print("R9:", R9)
print("R10:", R10)
print("R11:", R11)
print("R12:", R12, "\n")
print("Final Memory State: \n")
print("(Contents shown in decimal number system; not in base 16. In addition, only those registers are shown whose contents change during the program) \n")
print("Address:", Address, "Contents:", Contents)
print("Address:", Address1, "Contents:", Contents1)
print("Address:", Address2, "Contents:", Contents2)

print("Timing Simulator Output can be provided upon request")


