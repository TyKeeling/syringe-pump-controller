FILE = "syringe_setup.txt"

def getVal(file, searchTerm):
    currentFile = open(file, 'r')
    for line in currentFile:
        if searchTerm in line:
            val = int(line.split(": ")[1])
    currentFile.close()    
    return val

def getStr(file, searchTerm):
    currentFile = open(file, 'r')
    for line in currentFile:
        if searchTerm in line:
            string = next(currentFile).strip('\n').strip(' ').split("   ")
    currentFile.close()
    return string


numSyr = getVal(FILE, "Number of")
units = getVal(FILE, "Units")

address = getStr(FILE, "Address")
syrDia = getStr(FILE, "Internal Diameter")
infuseRate = getStr(FILE, "Infuse Rate")
infuseVol = getStr(FILE, "Target Infuse Volume")
withdrawlRate = getStr(FILE, "Withdrawl Rate")
withdrawlVol = getStr(FILE, "Target Withdrawl Volume")
