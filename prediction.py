# implement a gselect function
# save data to statistic
# get from a gselect table


import miscellaneous as misc

# @param 
# @return 
def gselect(address):
	# taken / not taken
	turn = "ntaken"
	# retrieve from memory
	return misc.readFromPredictionTable('predictionTable.txt')[int(address)]

def setGselect(shift):
	# change value
	turn = shift
	# save in memory
	return 0
