# Calculator
# Implement each function required in execution phase of pipeline

# SUM operation
# @param operand1,operand2
# @return sum op1 with op2
def sum(op1,op2):
    # print("op1: " + str(int(op1)) + " op2: " + str(int(op2)))
    return int(op1)+int(op2)

# SUB operation
# @param operand1,operand2
# @return sub op1 with op2
def sub(op1,op2):
    return int(op1)-int(op2)

# BRANCH EQUALS operation
# @param operand1, operand2
# @return:
# 0 - TRUE
# 1 - FALSE
def beq(op1,op2):
    if int(op1) == int(op2):
        print(str(op1) + "  " + str(op2))
        return 1 # TRUE - equals
    return 0 # FALSE - not equals

# BRANCH NOT EQUALS operation
# @param operand1, operand2
# @return
# 0 - TRUE
# 1 - FALSE
def bne(op1,op2):
    if op1 != op2:
        return 1 # TRUE - not equals
    return 0 # FALSE - equals

# BRANCH EQUAL ZERO
# @param op1
# @return
# 0 - TRUE
# 1 - FALSE
def beqz(op1):
    # print("OP1: " + str(op1))
    if str(op1) == str(0):
        # print('eq zero:'+ str(op1))
        return 1 # TRUE - equal ZERO
    return 0 # FALSE - not equal ZERO

# BRANCH NOT EQUAL ZERO
# @param op1
# @return
# 0 - TRUE
# 1 - FALSE
def bnez(op1):
    if str(op1) != str(0):
        print('not eq zero:'+ str(op1))
        return 1 # TRUE - not equal ZERO
    return 0 # FALSE - equal ZERO

# LOAD operation
def lw(op1):
    return 0

# ADD IMMEDIATE operation: op1 <- op2
# Only return op2 to be stored in op1
# @param destination, origin
# @return op2
def daddi(op1,op2):
    return op2

# LOAD operation
def load(address):
    # retrieve data from memory
    # readmemory(address)
    address = 2
    return address

# STORE operation
# @param address(memory address)
# @param value(value to be saved in memory)
# @return statuscode
#   0 - OK
#   1 - NOK
def store(address,value):
    # save data in memory
    # writememory(address, value)
    statuscode = 0
    return statuscode
