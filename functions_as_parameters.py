def add(fnum, snum):
	return fnum + snum


def subtract(fnum, snum):
	return fnum - snum


def evaluate(funName, fnum, snum):
	return funName(fnum, snum)


retValue = evaluate(add,100,200)
# retValue = evaluate(subtract,100,200)
print(retValue)