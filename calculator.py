# Calculator
# Implement each function required in execution phase of pipeline

# SUM operation
# @param operand1,operand2
# @return sum op1 with op2
def sum(op1,op2):
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
    if op1 == op2:
        return 0 # TRUE - equals
    return 1 # FALSE - not equals

# BRANCH NOT EQUALS operation
# @param operand1, operand2
# @return
# 0 - TRUE
# 1 - FALSE
def bne(op1,op2):
    if op1 != op2:
        return 0 # TRUE - not equals
    return 1 # FALSE - equals

# BRANCH EQUAL ZERO
# @param op1
# @return
# 0 - TRUE
# 1 - FALSE
def beqz(op1):
    if op1 == "0":
        return 0 # TRUE - equal ZERO
    return 1 # FALSE - not equal ZERO

# BRANCH NOT EQUAL ZERO
# @param op1
# @return
# 0 - TRUE
# 1 - FALSE
def bnez(op1):
    if op1 != "0":
        return 0 # TRUE - not equal ZERO
    return 1 # FALSE - equal ZERO

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
