# Create a header TODO
import csv
import re

# Auxiliar method in case of take only the instruction code
def breakInst(instruction):
    for row in instruction:
        return  re.findall(r'\S+',instruction)

# Auxiliar method in case of break instruction string
def breakData(data):
    for row in data:
        row[1] = row[1].split(",")
    return row[1]

# Method to return instructions in case of default mode for MIPS
# @param file -> memory file
# @return - list of instructions
def readInstructions(file):

    instructions = []

    with open(file, newline='\n') as inputfile:
        for row in csv.reader(inputfile):
            instructions.append(row)
    # -- print(str(instructions))

    return instructions

# Method to return instructions in case of separated by commas --- MAYBE USELESS
# @param file -> memory file
# @return - list of instructions
def readInstructionsByCommas(file):

    instructions = []

    with open(file, newline='\n') as inputfile:
        for row in csv.reader(inputfile):
            instructions.append(str(row).split(','))
    # -- print(str(instructions))

    return instructions

# @param program counter
# @param value for jump --> if taken in branch
# @return - PC with correct increment
def incrementPc(PC,jump):
    if int(jump) != 0:
        return PC + int(jump)
    else:
        return PC + 1

# @param instructionList
# @param nextInstruction
# @param adjustmentRequired
# @return - list of Instructions
def scaling(instructionList, nextInstruction, adjustmentRequired):

    adjust = 0

    # Shift register algorithm
    instructionList[4] = instructionList[3]
    instructionList[3] = instructionList[2]
    instructionList[2] = instructionList[1]
    instructionList[1] = instructionList[0]
    instructionList[0] = nextInstruction

    # Adjustment required due invalid instruction
    if adjustmentRequired == 1:
        adjust = 1

    if adjust == 1 and instructionList[2] == "beq":
        instructionList[1] = "    "
        adjust = 0

    return instructionList

# Read complete vector with prediction data from predictionTable.txt
# @param file
# @return list of prediction
def readFromPredictionTable(file):

    predictionTable = []

    with open(file, newline='\n') as inputfile:
        for row in csv.DictReader(inputfile):
            predictionTable.append(row['Value'])

    return predictionTable

# Read complete vector with registers from registers.txt
# @param file
# @return list of registers
def readRegisters(file):

    registers = []

    with open(file, newline='\n') as inputfile:
        for row in csv.DictReader(inputfile):
            #print(row['Register'],row['Value'])
            lst=str(row['Value'])
            registers.append(lst)

    return registers

# Write complete vector in registers.txt file
# @param file
# @return 0 - no error to save data
def writeRegisters(file, R):

    with open(file, 'w') as csvfile:
        fieldnames = ['Register', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for i in range(0,32):
            writer.writerow({'Register': 'R[' + str(i) + ']', 'Value': str(R[i])})

        return 0 # data correctly stored in registers.txt

# Check if a LOAD operation
# 0 - OK
# 1 - NOK
def isLoadFunction(operation):
    if operation == "lw":
        return 0
    return 1

# Check if a STORE operation
# 0 - OK
# 1 - NOK
def isStoreFunction(operation):
    if operation == "st":
        return 0
    return 1

# Verify if third element of vector has been defined
# @param operation - hardcoded definition
# @return
# 0 - has destination
# 1 - has not destination
def hasDestination(operation):
    if operation == "dadd" or operation == "dsub" or operation == "dsubi":
    #if operation.find("dadd") != -1 or operation.find("dsub") != -1 or operation.find("dsubi") != -1:
        return 0
    return 1

# Verify if is a math operation
def isImportingData(operation):
    if operation == "daddi":
        return 0
    return 1

# Verify if is a branch operation
def isBranchOperation(operation):
    if operation == "beq" or operation == "bne" or operation == "bnez" or operation == "beqz":
        return 0
    return 1

def clearRegister():
    empty = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    writeRegisters('registers.txt', empty)

def clearVectors():
    clearRegister()

# ADDITIONAL

# Print data on screen for test reason
def printInstruction(instructionMemory,pc):
    if ( len(instructionMemory[pc]) == 5):
        print(instructionMemory[pc][4])
    if ( len(instructionMemory[pc]) == 4):
        print(instructionMemory[pc][3])
    if ( len(instructionMemory[pc]) == 3):
        print(instructionMemory[pc][2])
    print(instructionMemory[pc][1])
    print(instructionMemory[pc][0])