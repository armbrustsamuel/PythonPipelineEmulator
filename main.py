#!/usr/bin/env python3

# Main
import calculator 	as calc
import pipelinePhase 	as ppPhase
import pipelineView 	as ppView
import prediction       as pred
import miscellaneous 	as misc
import sys

predictionEnabled = 1

#if sys.argv[1] == "-p" or sys.argv[1] == "-P":
#    predictionEnabled = 0

# Prediction table with 32 positions
prediction = []
addressGselect = 0
wrongInstruction = 0
newPC = 0
wrongPrediction = 0
rightPrediction = 0

# Branch History Register
BHR = 0
last_Gselect = 0
resultPrediction = 0

# Current data for steps
current_search 	= 0
current_decode 	= ["  "," "," "," "]
current_execute = ["  "," "," "]
current_memory 	= 0
current_execute = 0
current_register = 0

# Instructions table
instructionMemory = []
# Carry out instruction memory to get size
instructionMemory = misc.readInstructions("inputfile.txt")

instructionCounter = 0
wrongInstructionCounter = 0

# pipeline steps List
pipelineList = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

# Register table (32 slots)
R = []
R = misc.readRegisters("registers.txt")

# Program counter - PC
PC = 0

# Write header at screen
ppView.Header()

#misc.clearVectors()

# Execution of instructions - Implement for in range
#for instruction in instructionMemory:
for i in range(1,30):

    # SEARCH ############ - OK
    current_search = ppPhase.search(PC) # TO ADJUST RETURN
    #print("current Search" + str(current_search))

    # WRITE BACK ############
    current_register = ppPhase.saveAtRegister(current_memory,0,R)
    #print(current_register)

    # MEMORY ############
    if misc.isLoadFunction(current_decode[0]) == 0:
        #  READ FROM MEMORY
        current_memory = misc.readRegisters('registers.txt')[int(current_decode[2])]
        #print(current_memory)
    else:

        if misc.isStoreFunction(current_decode[0]) == 0:
            #  SAVE AT MEMORY
            print("tentando entender o MEMORY")
            print(current_decode[2] + " has been assigned to " + current_decode[1])
            R[int(current_decode[1])] = current_decode[2]
            misc.writeRegisters('registers.txt', R)
            current_memory = "saved"
    #current_memory = ppPhase.memory(current_execute)

    # EXECUTE ############
    current_execute = ppPhase.execute(
        str(current_decode[0]).strip(),
        str(current_decode[1]),
        str(current_decode[2]))
##print("current Execution:" + str(current_execute))

    if current_execute == "JUMP":
        newPC = misc.incrementPc(PC,current_decode[1])

    # Test if an operation as SUM or SUB
    if misc.hasDestination(current_decode[0]) == 0:
        R[int(current_decode[3])] = str(current_execute)
        #misc.writeRegisters('registers.txt',R)

    # Test if an operation to assign data for other register
    if misc.isImportingData(current_decode[0]) == 0:
        R[int(current_decode[1])] = str(current_execute)

    # Test if a branch operation
    if misc.isBranchOperation(current_decode[0]) == 0:

        #if current_execute == resultPrediction:
        # By Default - never jump - "1"
        if resultPrediction == 1:
            #print("right prediction")
            rightPrediction = rightPrediction + 1
            wrongInstruction = 0 ## -- WHEN IT MUST BE CHANGED ?
            # save data in prediction table
        else:
            #print("wrong prediction")
            wrongPrediction = wrongPrediction + 1
            wrongInstruction = 1 ## -- WHEN IT MUST BE CHANGED ?
            wrongInstructionCounter+=1

        if current_execute == 0:
            newPC = misc.incrementPc(PC,current_decode[3])
            if resultPrediction == 0:
                rightPrediction = rightPrediction + 1

    #print(PC)

    # Must adjust the scaling function only in case of wrong instruction
    # 0 - Adjustment not required
    # 1 - Adjustment required

    # DECODE ############ - OK
    current_decode = ppPhase.decode(PC)
##print("current Decoding:" + str(current_decode))
    #print(current_decode[0])

    # pipelineList[PC] = currentInstruction[0]

    pipelineList = misc.scaling(pipelineList, current_decode[0], wrongInstruction)
    #print(pipelineList)

    #print("BHR:"+str(BHR)+" addressGselect:"+str(addressGselect)+ " resultPrediction:"+ str(resultPrediction))
    # Must start prediction? ----
    if predictionEnabled == 1:
        if pipelineList[2] == "beq" or pipelineList[2] == "bne" or pipelineList[2] == "beqz" or pipelineList[2] == "bnez":
            #start prediction
            addressGselect = PC + BHR
            while addressGselect >= 32:
                addressGselect = addressGselect - 32

            resultPrediction = pred.gselect(addressGselect)
            last_Gselect = addressGselect
            BHR = BHR + 1
            # print("prediction called")

    if pipelineList[4].find(" ") == -1:
        instructionCounter+=1

    # At the end, increment PC
    if newPC != 0:
        PC = newPC
        newPC = 0
    else:
        PC = misc.incrementPc(PC,0)

    # Write each pipeline step at screen
    ppView.newStep(pipelineList[0],pipelineList[1],pipelineList[2],pipelineList[3],pipelineList[4])

misc.writeRegisters('registers.txt',R)
print('Wrong Prediction: ' + str(wrongPrediction) + '\nRight Prediction: ' + str(rightPrediction))
print('Instruction executed: ' + str(instructionCounter))
print('Wrong instructions: ' + str(wrongInstructionCounter))