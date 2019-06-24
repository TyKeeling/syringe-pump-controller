
from time import sleep

import Pumpy_lite as Pl
import readtext


SYR0 = 0
SYR1 = 1
SYR2 = 2 
SYR3 = 3
numSyr = readtext.numSyr


def runAll():
    if numSyr >= 1:
        pump0.write('CLV')
        pump0.read()
        sleep(0.01)
        pump0.write('RUN')
        pump0.read()
    if numSyr >= 2:
        pump1.write('CLV')
        pump1.read()
        sleep(0.01)
        pump1.write('RUN')
        pump1.read()
    if numSyr >= 3:
        pump2.write('CLV')
        pump2.read()
        sleep(0.01)
        pump2.write('RUN')
        pump2.read()
    if numSyr >= 4:
        pump3.write('CLV')
        pump3.read()
        sleep(0.01)
        pump3.write('RUN')
        pump3.read()

def revAll():
    if numSyr >= 1:
        pump0.write('CLVW')
        pump0.read()
        sleep(0.01)
        pump0.write('RUNW')
        pump0.read()
    if numSyr >= 2:
        pump1.write('CLVW')
        pump1.read()
        sleep(0.01)
        pump1.write('RUNW')
        pump1.read()
    if numSyr >= 3:
        pump2.write('CLVW')
        pump2.read()
        sleep(0.01)
        pump2.write('RUNW')
        pump2.read()
    if numSyr >= 4:
        pump3.write('CLVW')
        pump3.read()
        sleep(0.01)
        pump3.write('RUNW')
        pump3.read()

def stopAll():
        if numSyr >= 1:
            pump0.write('STP')
            pump0.read()
        if numSyr >= 2:
            pump1.write('STP')
            pump1.read()
        if numSyr >= 3:
            pump2.write('STP')
            pump2.read()
        if numSyr >= 4:
            pump3.write('STP')
            pump3.read()

#defining units based on text file
if readtext.units == 1:
    infuseRate_S = "MLM "
    infuseVol_S = "MLT "
    withdrawlRate_S = "MLMW "
    withdrawlVol_S = "MLTW "
else:
    infuseRate_S = "ULM "
    infuseVol_S = "ULT "
    withdrawlRate_S = "ULMW "
    withdrawlVol_S = "ULTW "

print "Welcome to the Pump Controller Software. Please wait while the pumps initialize..."

#initiating chain 
chain = Pl.Chain('/dev/ttyUSB0')
sleep(0.1)

#pump0 setup
if int(readtext.numSyr) >= 1:
    
    #address, diameter
    pump0 = Pl.Pump(chain, address=0)
    sleep(0.01)
    pump0.address = str(readtext.address[SYR0])
    sleep(0.01)
    pump0.write('MMD ' + readtext.syrDia[SYR0])
    pump0.read()
    sleep(0.01)
    pump0.write('DIA')
    pump0.read()
    sleep(0.01)
    
    #forward speed and target volume 
    pump0.write(infuseRate_S + readtext.infuseRate[SYR0])
    pump0.read()
    sleep(0.01)
    pump0.write('CLV')
    pump0.read()
    sleep(0.01)
    pump0.write(infuseVol_S + readtext.infuseVol[SYR0])
    pump0.read()
    sleep(0.01)

    #reverse speed and target volume 
    pump0.write(withdrawlRate_S + readtext.withdrawlRate[SYR0])
    pump0.read()
    sleep(0.01)
    pump0.write('CLVW')
    pump0.read()
    sleep(0.01)
    pump0.write(withdrawlVol_S + readtext.withdrawlVol[SYR0])
    pump0.read()
    sleep(0.01)

    print "Pump 1/%d initialized..." %numSyr


#pump1 setup
if int(readtext.numSyr) >= 2:
    
    #address, diameter
    pump1 = Pl.Pump(chain, address=0)
    sleep(0.01)
    pump1.address = str(readtext.address[SYR1])
    sleep(0.01)
    pump1.write('MMD ' + readtext.syrDia[SYR1])
    pump1.read()
    sleep(0.01)
    pump1.write('DIA')
    pump1.read()
    sleep(0.01)

    #forward speed and target volume 
    pump1.write(infuseRate_S + readtext.infuseRate[SYR1])
    pump1.read()
    sleep(0.01)
    pump1.write('CLV')
    pump1.read()
    sleep(0.01)
    pump1.write(infuseVol_S + readtext.infuseVol[SYR1])
    pump1.read()
    sleep(0.01)

    #reverse speed and target volume 
    pump1.write(withdrawlRate_S + readtext.withdrawlRate[SYR1])
    pump1.read()
    sleep(0.01)
    pump1.write('CLVW')
    pump1.read()
    sleep(0.01)
    pump1.write(withdrawlVol_S + readtext.withdrawlVol[SYR1])
    pump1.read()
    sleep(0.01)

    print "Pump 2/%d initialized..." %numSyr


#pump2 setup                           
if int(readtext.numSyr) >= 3:

    #address, diameter
    pump2 = Pl.Pump(chain, address=0)
    sleep(0.01)
    pump2.address = str(readtext.address[SYR2])
    sleep(0.01)
    pump2.write('MMD ' + readtext.syrDia[SYR2])
    pump2.read()
    sleep(0.01)
    pump2.write('DIA')
    pump2.read()
    sleep(0.01)

    #forward speed and target volume 
    pump2.write(infuseRate_S + readtext.infuseRate[SYR2])
    pump2.read()
    sleep(0.01)
    pump2.write('CLV')
    pump2.read()
    sleep(0.01)
    pump2.write(infuseVol_S + readtext.infuseVol[SYR2])
    pump2.read()
    sleep(0.01)

    #reverse speed and target volume 
    pump2.write(withdrawlRate_S + readtext.withdrawlRate[SYR2])
    pump2.read()
    sleep(0.01)
    pump2.write('CLVW')
    pump2.read()
    sleep(0.01)
    pump2.write(withdrawlVol_S + readtext.withdrawlVol[SYR2])
    pump2.read()
    sleep(0.01)

    print "Pump 3/%d initialized..." %numSyr


#pump3 setup                           
if int(readtext.numSyr) >= 4:

    #address, diameter
    pump3 = Pl.Pump(chain, address=0)
    sleep(0.01)
    pump3.address = str(readtext.address[SYR3])
    sleep(0.01)
    pump3.write('MMD ' + readtext.syrDia[SYR3])
    pump3.read()
    sleep(0.01)
    pump3.write('DIA')
    pump3.read()
    sleep(0.01)

    #forward speed and target volume 
    pump3.write(infuseRate_S + readtext.infuseRate[SYR3])
    pump3.read()
    sleep(0.01)
    pump3.write('CLV')
    pump3.read()
    sleep(0.01)
    pump3.write(infuseVol_S + readtext.infuseVol[SYR3])
    pump3.read()
    sleep(0.01)

    #reverse speed and target volume 
    pump3.write(withdrawlRate_S + readtext.withdrawlRate[SYR3])
    pump3.read()
    sleep(0.01)
    pump3.write('CLVW')
    pump3.read()
    sleep(0.01)
    pump3.write(withdrawlVol_S + readtext.withdrawlVol[SYR3])
    pump3.read()
    sleep(0.01)

    print "Pump 4/%d initialized..." %numSyr


ongoing = True

while ongoing:
    response = raw_input("Enter Command. Try 'help' For more information:\n").strip()
 
    if response == 'run' or response == 'r':
        runAll()
        if numSyr == 1:
            print "Running 1 Pump..."
        else:
            print "Running %d Pumps..." %numSyr
    
    elif response == 'stop' or response == 'stp' or response == 's':
        print "Stopping... please wait..."
        stopAll()
        if numSyr == 1:
            print "Pump is now stopped..."
        else:
            print "Pumps are now stopped..."
    
    elif response == 'reverse' or response == 'rev' or response == 'b':
        revAll()
        if numSyr == 1:
            print "Pump running in reverse..."
        else:
            print "Pumps are running in reverse..."
    
    elif response == 'help':
        print "\n\n\nThis program is designed to control Harvard Apparatus Pumps. \nParameters are defined in the 'syringe_setup.txt' file found in this directory."
        print "\nThis program responds to the following phrases:"
        print "\trun (r)     - runs the pumps.\n\tstop (s)    - stops the pumps."
        print "\treverse (b) - reverses the pumps.\n\texit       - quits the program.\n"
        print "If a limit switch is hit, stop the pump (s) then reset and try your command."
        print "For a reason yet to be understood, one must enter the reverse command twice after hitting the limit switch.\n" 

    elif response == 'exit':
        print "Closing the program..."
        ongoing = False

    else:
        print "I'm sorry, I don't understand that. Please try again."
