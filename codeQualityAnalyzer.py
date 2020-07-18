#code quality annalyzer

#Input a file
#check what language it's in C, Java, Python, Cpp
#for now, show which variable names that have a length less than 4.

import sys
import variableNameLength


def fileExtensionMapping(fileExtension):
    switcher = {
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

	print("You gave us a " + fileExtensionArray[1] +  ". Processing it now...")
	print("If there were any errors you can find them in the errors.txt file")


	return fileExtensionArray[0]


def main(): 

	fileExtension = getFileType(str(sys.argv[1]))

	f = open("warnings.txt", "w")
	f.write("File Name: " + sys.argv[1] + "\n\n")
	f.close()

	variableNameLength.variableNameLengthChecker(fileExtension, sys.argv[1])



main()
