import math

# Min-max method
def minMaxMethod(column, lines, columnSelected):
	MIN = min(columnSelected)
	MAX = max(columnSelected)

	NEW_MIN = 0
	NEW_MAX = 1

	for line in lines:
		v = float(line[column])
		line[column] = str(round(((v - MIN)/(MAX - MIN))*(NEW_MAX - NEW_MIN) + NEW_MIN, 2))

# Z-score method
def zScoreMethod(column, lines, columnSelected):
	N = len(columnSelected)
	AVERAGE = sum(columnSelected)/N
	SUM = sum(list(map(lambda line: math.pow(float(line[column]) - AVERAGE, 2), lines)))
	STANDARD_DEVIATION = math.sqrt((1/N)*SUM)

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
def normalization(data):
	attributes = data[0]
	lines = data[1:]

	method = input('Enter the normalize method (type: [min-max, z-score]: ')

	if (method in ['min-max', 'z-score']):
		for value in lines[0]:
			try:
				if isinstance(float(value), float):
					column = lines[0].index(value)
					columnSelected = list(map(lambda line: float(line[column]), lines))
					changeValues(method, column, lines, columnSelected)
			except:
				print
	else:
		print('The normalize method must be "min-max" or "z-score".\nPlease run the program again!')
		return

def main():
	fInput = open('./data/data.txt', 'r')
	data = [line.rstrip('\n').split(',') for line in fInput]
	fInput.close()

	normalization(data)

	fOutput = open('./data/data_output.txt', 'w+')
	dataOutput = '\n'.join(map(lambda line: ','.join(line), data))
	fOutput.write(dataOutput)
	fOutput.close()

main()