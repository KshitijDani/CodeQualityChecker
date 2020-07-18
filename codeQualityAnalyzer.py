#code quality annalyzer

#Input a file
#check what language it's in C, Java, Python, Cpp
#for now, show which variables have been named that have a single letter named.

import sys

def fileExtensionMapping(fileExtension):
    switcher={
        "js": ["js", "JavaScript"],
        "c": ["c", "C"],
        "java": ["java", "Java"],
        "py": ["py", "Python"]
    }
    return switcher.get(fileExtension, ["Error: can not process file type " + fileExtension])

def getFileType(filename): 

	fileNameSplit = filename.split(".")

	# Error if no file extension passed
	if len(fileNameSplit) < 2: 
		print("Error: The file you've specified isn't a processible file and has no extension")
		return

	fileExtension = fileNameSplit[1]
	fileExtensionArray = fileExtensionMapping(fileExtension)

	# Error if we can't handle the language
	if len(fileExtensionArray) < 2:
		print(fileExtensionArray[0])
		return

	print("You gave us a " + fileExtensionArray[1] +  ". Processing it now...\n")


	return fileExtensionArray[0]


def printVariableNameLengthErrors(errors):

	f = open("errors.txt", "a")

	for error in errors:
		#print("At line number: ", error[0], " you have a variable name that's length is less than 4")
		f.write("At line number: " + str(error[0]) + " you have a variable name that's length is less than 4\n")
		#print("Line: ", error[1])
		f.write("Line: " +  str(error[1] + "\n"))

	f.close()

def variableNameLengthChecker(fileExtension, filename):

	# If no extension, then we can't handle the file
	if fileExtension:
		fileContents = open(filename, "r")
		lineNumber = 0
		errors = []

		for line in fileContents:
			lineNumber = lineNumber + 1
			lineContents = line.split(" ")

			previousWord = ""

			for word in lineContents:
				if word == "=":
					if len(previousWord) < 4:
						errors.append([lineNumber, line])


				previousWord = word

		printVariableNameLengthErrors(errors)


		fileContents.close()

	return 


def main(): 

	fileExtension = getFileType(str(sys.argv[1]))

	f = open("errors.txt", "w")
	f.write("File Name: " + sys.argv[1] + "\n\n")
	f.close()

	variableNameLengthChecker(fileExtension, sys.argv[1])




main()
