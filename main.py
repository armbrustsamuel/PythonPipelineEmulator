#!/usr/bin/env python3

# Main
import calculator 	as calc
import pipelinePhase 	as ppPhase
import pipelineView 	as ppView
import prediction       as pred
import miscellaneous 	as misc
import cleaner
import time

import sys

cleaner.clearVectors()

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
branch_value = 0
branch_execution = 0

# Branch History Register
BHR = [0,0,0,0]
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
for i in range(1,len(instructionMemory)+12):

    # SEARCH ############ - OK
    current_search = ppPhase.search(PC) # TO ADJUST RETURN
    #print("current Search" + str(current_search))

    # WRITE BACK ############
    # current_register = ppPhase.saveAtRegister(current_memory,0,R)
    #print(current_register)

    # MEMORY ############
    # if misc.isLoadFunction(current_decode[0]) == 0:
    #     #  READ FROM MEMORY
    #     current_memory = misc.readRegisters('registers.txt')[int(current_decode[2][1:])]
    #     #print(current_memory)
    # else:
    #
    #     if misc.isStoreFunction(current_decode[0]) == 0:
    #         #  SAVE AT MEMORY
    #         print("tentando entender o MEMORY")
    #         print(current_decode[2] + " has been assigned to " + current_decode[1])
    #         R[int(current_decode[1])] = current_decode[2]
    #         misc.writeRegisters('registers.txt', R)
    #         current_memory = "saved"
    #current_memory = ppPhase.memory(current_execute)

    # Test if an operation to assign data for other register

    #  ----##### AJUSTAR PREDICAO #####-------
    #print("BHR:"+str(BHR)+" addressGselect:"+str(addressGselect)+ " resultPrediction:"+ str(resultPrediction))
    # Must start prediction? ----
    if predictionEnabled == 1:
        if pipelineList[2] == "beq" or pipelineList[2] == "bne" or pipelineList[2] == "beqz" or pipelineList[2] == "bnez":
            #start prediction
            addressGselect = PC + BHR[0] + BHR[1] + BHR[2] + BHR[3]
            # print("Branch value: " + str(branch_value))
            misc.shiftBHR(BHR,branch_value)
            while addressGselect >= 32:
                addressGselect = addressGselect - 32
                #ADJUST GSELECT - REFACTORY
            prediction = pred.gselect(addressGselect)
            last_Gselect = addressGselect
            # BHR = BHR + 1
            # print("prediction called")
            # print("prediction")
            # print(prediction)
            # print("current execution: " + str(branch_execution))
            if branch_execution == 0:
                # branch_value = 0
                if prediction == 0:
                    rightPrediction += 1
                    wrongInstruction = 0
                else:
                    wrongPrediction += 1
                    wrongInstruction = 1
                    wrongInstructionCounter+=1
            else:
                # print("how much branch: " + str(branch_value))
                newPC = misc.incrementPc(PC,branch_value)
                if prediction == 0:
                    wrongPrediction += 1
                    wrongInstruction = 1
                    wrongInstructionCounter+=1
                    # continue
                    break
                else:
                    # newPC = misc.incrementPc(PC,current_decode[3])
                    rightPrediction += 1
                    wrongInstruction = 0
            branch_execution = 0
            branch_value = 0
            # print("wrong instruction: " + str(wrongInstruction))


    # EXECUTE ############
    if(current_decode[0].find("j") != -1):
        #call jump execution
        current_execute = "JUMP"
    # elif(current_decode[0].find("daddi") != -1):
    #     #fill registers
    #     # print(current_decode[3])
    #     R[int(current_decode[1][1:])] = int(R[int(current_decode[2][1:])]) + int(current_decode[3][1:])
    #     current_execute = 0
    elif misc.isImportingData(current_decode[0]) == 0:
        # print("DADDI: " + str(current_decode[3][1:]))
        R[int(current_decode[1][1:])] = str(current_decode[3][1:])
        # print(R[int(current_decode[1][1:])])

        current_execute = 0
        # misc.writeRegisters('registers.txt',R)

    elif misc.isBranchOperation(current_decode[0]) == 0:
        current_execute = ppPhase.execute(
            str(current_decode[0]).strip(),
            str(current_decode[1]),
            str(current_decode[2]))
        # print("Execution branch: " + str(branch_execution))
        # print("Current decode: " + str(current_decode[2][1:]))
        if misc.isBranchThreeOperation(current_decode[0]) == 0:
            branch_value = current_decode[3][1:]
            # current_execute = 0
            branch_execution = current_execute
            # print(current_decode[0])
            # print(current_decode[1])
            # print(current_decode[2])
            # print("Current decode: " + str(current_decode[3][1:]))
        else:
            branch_value = current_decode[2][1:]
            current_execute = 0
            branch_execution = current_execute
            # print("Current decode: " + str(current_decode[2][1:]))

    elif(current_decode[0].find("dsubi") != -1):
        #fill registers
        # print(current_decode[3])
        R[int(current_decode[1][1:])] = int(R[int(current_decode[2][1:])]) - int(current_decode[3][1:])
        # misc.writeRegisters('registers.txt',R)
        current_execute = 0
    elif(current_decode[0] is "dadd"):
        R[int(current_decode[1][1:])] = int(R[int(current_decode[2][1:])]) - int(R[int(current_decode[2][1:])])
        current_execute = 0
    else:
        current_execute = ppPhase.execute(
            str(current_decode[0]).strip(),
            str(current_decode[1]),
            str(current_decode[2]))

    print("current Execution:" + str(current_execute))

    misc.writeRegisters('registers.txt',R)

    if current_execute == "JUMP":
        newPC = misc.incrementPc(PC,current_decode[1])

    # Test if an operation as SUM or SUB
    if misc.hasDestination(current_decode[0]) == 0:
        R[int(current_decode[1][1:])] = str(current_execute)
        #misc.writeRegisters('registers.txt',R)

    # Test if a branch operation - wrong moment
    # if misc.isBranchOperation(current_decode[0]) == 0:

    # Must adjust the scaling function only in case of wrong instruction
    # 0 - Adjustment not required
    # 1 - Adjustment required

    # DECODE ############ - OK
    current_decode = ppPhase.decode(PC)
    # print("current Decoding:" + str(current_decode))

    # pipelineList[PC] = currentInstruction[0]

    # print(wrongInstruction)

    pipelineList = misc.scaling(pipelineList, current_decode[0], wrongInstruction)
    wrongInstruction = 0
    #print(pipelineList)

    if pipelineList[4].find(" ") == -1:
        instructionCounter+=1

    # At the end, increment PC
    print("PC:" + str(PC) + "newPC: " + str(newPC))
    if newPC != 0:
        PC = newPC
        newPC = 0
    else:
        PC = misc.incrementPc(PC,0)

    misc.writeRegisters('registers.txt',R)

    print("R[1] = " + str(R[1]))
    print("R[2] = " + str(R[2]))
    print("R[3] = " + str(R[3]))
    print("R[4] = " + str(R[4]))
    print("R[7] = " + str(R[7]))
    print("R[19] = " + str(R[19]))
    print("R[20] = " + str(R[20]))
    # print("R[7] = " + str(R[7]))

    # time.sleep(1)

    # Write each pipeline step at screen
    ppView.newStep(pipelineList[0],pipelineList[1],pipelineList[2],pipelineList[3],pipelineList[4])

misc.writeRegisters('registers.txt',R)
print('Wrong Prediction: ' + str(wrongPrediction) + '\nRight Prediction: ' + str(rightPrediction))
print('Instruction executed: ' + str(instructionCounter))
print('Wrong instructions: ' + str(wrongInstructionCounter))