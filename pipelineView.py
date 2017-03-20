############### 	Pipeline Viewer		###############
# Visual way to analyze pipeline with graphic data

# command = ["LW","SD","HALT","DADD","RAW","STALL"]

def newStep(stat1,stat2,stat3,stat4,stat5):
	print("|\t"+stat1+"\t|\t"+stat2+"\t|\t"+stat3+"\t|\t"+stat4+"\t|\t"+stat5+"\t|")

def Header():
	print("|\tSEARCH\t|\tDECODE\t|\tEXECUTE\t|\tMEMORY\t|\tWRBACK\t|")	

def newStepVector(ls):
	print("|\t"+ls[0]+"\t|\t"+ls[1]+"\t|\t"+ls[2]+"\t|\t"+ls[3]+"\t|\t"+ls[4]+"\t|")
