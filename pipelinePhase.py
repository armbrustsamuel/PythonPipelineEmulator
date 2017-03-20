#   PIPELINE PHASES

import re
import miscellaneous as misc
import calculator as calc

instructionMemory = []

# Search phase
# @param program counter
# @return a instruction such as "dadd","daddi","dsub" ...
def search(pc):
	# Retrieve next instruction in memory
	instruction = misc.readInstructions("inputfile.txt")

	dummyReturn = ["       "," "," "]
	if pc >= len(instruction):
		return dummyReturn
	return instruction[pc]
	#returnIntruction = ["lw", "$s1", "$s2", "$s3"]
	#return returnIntruction

# Decode phase
# @param
# @return
def decode(pc):
	# Decode instruction and call execute
	instructionMemory = misc.readInstructions("inputfile.txt")

	dummyDecode = [" "," "," "," "," "]
	# Adjust length
	if pc >= len(instructionMemory):
		return dummyDecode
	else:
		instructionMemory[pc].append(" ")
		# -- print(len(instructionMemory[pc]))
		if len(instructionMemory[pc]) > 3 :
			instructionMemory[pc][3] = instructionMemory[pc][2]
		if len(instructionMemory[pc]) > 2:
			instructionMemory[pc][2] = instructionMemory[pc][1]
		instructionMemory[pc][1] = instructionMemory[pc][0][5:].strip()
		instructionMemory[pc][0] = instructionMemory[pc][0][:5].strip()
		return instructionMemory[pc]

	# To be removed
	#misc.printInstruction(instructionMemory,pc)

# Execute phase
# @param
# @return exit[code, message]
#  - 0 - correct execution	, result of calculation
#  - 1 - wrong execution	, "Wrong instruction"
#  - 2 - shift address		, "ok" or "nok"
def execute(opCode,reg1,reg2):

	# Read registers
	registers = misc.readRegisters('registers.txt')
	if reg1 != " ":
		op1 = registers[int(reg1)]
	if reg1 != " ":
		op2 = registers[int(reg2)]

	if opCode.find("dadd") != -1:
		return calc.sum(op1,op2)
	elif opCode.find("daddi") != -1:
		return calc.daddi(op1,op2)
	elif opCode.find("dsub") != -1:
		return calc.sub(op1,op2)
	elif opCode.find("lw") != -1:
		return "LW"
	elif opCode.find("dsubi") != -1:
		return calc.sub(int(op1),int(op2))
	elif opCode.find("beqz")  != -1:
		return calc.beqz(op1)
	elif opCode.find("bnez") != -1:
		return calc.bnez(op1)
	elif opCode.find("beq") != -1:
		return calc.beq(op1,op2)
	elif opCode.find("bne") != -1:
		return calc.bne(op1,op2)
	elif opCode.find("j") != -1:
		return "JUMP"
	elif opCode.find("   ") != -1:
		return 0
	else:
		#print("Wrong instruction - review code")
		return 1

# MEMORY phase
# Reuse already created function

# Writeback
# @param
# @return
def saveAtRegister(data, address, registers):

	registers[address] = data

	if ( misc.writeRegisters('registers.txt', registers) == 0):
		return 0
	else:
		print("Error saving registers")
		return 1

