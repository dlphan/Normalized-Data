import math

NEW_MIN = 0
NEW_MAX = 1

# Min-max method
def minMaxMethod(column, lines, columnSelected):
	MIN = min(columnSelected)
	MAX = max(columnSelected)

	for line in lines:
		v = float(line[column])
		line[column] = str(round(((v - MIN)/(MAX - MIN))*(NEW_MAX - NEW_MIN) + NEW_MIN, 2))

# Z-score method
def zScoreMethod(column, lines, columnSelected):
	N = len(columnSelected)
	AVERAGE = sum(columnSelected)/N
	SUM = sum(list(map(lambda line: math.pow(float(line[column]) - AVERAGE, 2), lines)))
	STANDARD_DEVIATION = math.sqrt((1/N)*SUM)
	# print('AVERAGE: ',round(AVERAGE, 2),' - VARIANCE: ',round((1/N)*SUM, 2))
	for line in lines:
		v = float(line[column])
		line[column] = str(round((v - AVERAGE)/STANDARD_DEVIATION, 2))

# Change the value of the attributes
def changeValues(method, column, lines, columnSelected):
	if method == 'min-max':
		minMaxMethod(column, lines, columnSelected)
	elif method == 'z-score':
		zScoreMethod(column, lines, columnSelected)

# Normalization
def normalization(data, attributesChanged):
	lines = data[1:]
	method = input('Enter the normalize method (type: [min-max, z-score]: ')
	index = 0

	if (method in ['min-max', 'z-score']):
		for value in lines[0]:
			try:
				if isinstance(float(value), float):
					attributesChanged.append(data[0][index])
					columnSelected = list(map(lambda line: float(line[index]), lines))
					changeValues(method, index, lines, columnSelected)
			except:
				print
			index += 1
	else:
		print('The normalize method must be "min-max" or "z-score".\nPlease run the program again!')
		return

def main():
	attributesChanged = []

	fInput = open('./data/bank.txt', 'r')
	data = [line.rstrip('\n').split(',') for line in fInput]
	fInput.close()

	normalization(data, attributesChanged)

	fOutput = open('./data/data_output.txt', 'w+')
	dataOutput = '\n'.join(map(lambda line: ','.join(line), data))
	fOutput.write(dataOutput)
	fOutput.close()

	fLog = open('./data/data_log.txt', 'w+')
	dataLog = 'The attributes are normalized: [' + ', '.join(attributesChanged) + ']\nRange: [' + str(NEW_MIN) + ',' + str(NEW_MAX) + ']'
	fLog.write(dataLog)
	fLog.close()

main()