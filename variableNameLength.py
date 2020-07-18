import configuration

def writeVariableNameLengthWarning(warnings):

	f = open("warnings.txt", "a")

	f.write("-------------------- Variable Name Length Warnings (" + str(len(warnings)) + ") --------------------\n\n")

	for warning in warnings:
		f.write("At line number: " + str(warning[0]) + " you have a variable name that's length is less than " + str(configuration.variableNameLength) + "\n")
		f.write("Line: " +  str(warning[1] + "\n"))

	f.close()
	return

def variableNameLengthChecker(fileExtension, filename):

	# If no extension, then we can't handle the file
	if fileExtension:
		fileContents = open(filename, "r")
		lineNumber = 0
		warnings = []

		for line in fileContents:
			lineNumber = lineNumber + 1
			lineContents = line.split(" ")

			previousWord = ""

			for word in lineContents:
				if word == "=":
					if len(previousWord) < configuration.variableNameLength:
						warnings.append([lineNumber, line])


				previousWord = word

		fileContents.close()
		writeVariableNameLengthWarning(warnings)

	return 