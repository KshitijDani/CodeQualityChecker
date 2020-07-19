import configuration

def fileExtensionMapping(fileExtension, filename):
    switcher = {
        "js": lambda: funtionNameLengthCheckerJS(filename),
        "c": lambda: funtionNameLengthCheckerC(filename),
        "java": lambda: funtionNameLengthCheckerJava(filename),
        "py": lambda: funtionNameLengthCheckerPy(filename)
    } 

    return switcher.get(fileExtension, lambda: ["nothing"])()

def writeFunctionNameLengthWarning(warnings):

	f = open("warnings.txt", "a")

	f.write("-------------------- Function Name Length Warnings (" + str(len(warnings)) + ") --------------------\n\n")

	for warning in warnings:
		f.write("At line number " + str(warning[0]) + ": " +  str(warning[1] + "\n"))

	f.close()
	return

def funtionNameLengthCheckerJS(filename): 
	#TODO: write logic for this function
	print("Inside functionName JS " + filename)
	return

def funtionNameLengthCheckerC(filename): 
	#TODO: write logic for this function
	print("Inside functionName C " + filename)
	return

def funtionNameLengthCheckerJava(filename): 
	#TODO: write logic for this function
	print("Inside functionName java " + filename)
	return

def funtionNameLengthCheckerPy(filename): 

	fileContents = open(filename, "r")
	lineNumber = 0
	warnings = []

	for line in fileContents:
		lineNumber = lineNumber + 1
		lineContents = line.split(" ")
		defFoundFlag = 0

		for word in lineContents:

			if defFoundFlag == 1:

				defFoundFlag = 0
				functionName = word.split("(")[0]
				
				if len(functionName) < configuration.functionNameLength:
					warnings.append([lineNumber, line])

			if word == "def":
				defFoundFlag = 1


	fileContents.close()
	writeFunctionNameLengthWarning(warnings)

	return


def functionNameLengthChecker(fileExtension, filename):

	if configuration.variableNameLengthFlag: 

		# If no extension, then we can't handle the file
		if fileExtension:
			fileExtensionMapping(fileExtension, filename)

	return 