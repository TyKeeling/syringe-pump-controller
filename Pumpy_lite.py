from __future__ import print_function
import serial
import argparse
import logging

#You may need to disable serial from the raspi-config in order to use the USB
#Try ttyUSB0 if you only have one USB plugged in

class Chain(serial.Serial):
    """Create Chain object.

    Harvard syringe pumps are daisy chained together in a 'pump chain'
    off a single serial port. A pump address is set on each pump. You
    must first create a chain to which you then add Pump objects.

    Chain is a subclass of serial.Serial. Chain creates a serial.Serial
    instance with the required parameters, flushes input and output
    buffers (found during testing that this fixes a lot of problems) and
    logs creation of the Chain.
    """
    def __init__(self, port):
        serial.Serial.__init__(self,port=port, stopbits=serial.STOPBITS_TWO, parity=serial.PARITY_NONE, timeout=2)
        self.flushOutput()
        self.flushInput()
        logging.info('Chain created on %s',port)

class Pump:
    """Create Pump object for Harvard Pump 11.

    Argument:
        Chain: pump chain

    Optional arguments:
        address: pump address. Default is 0.
        name: used in logging. Default is Pump 11.
    """
    def __init__(self, chain, address=0, name='Pump 11', printing_text=True):
        self.name = name
        self.serialcon = chain
        self.address = '{0:02.0f}'.format(address)
        self.diameter = None
        self.flowrate = None
        self.targetvolume = None
        self.printing_text=printing_text

    def __repr__(self):
        string = ''
        for attr in self.__dict__:
            string += '%s: %s\n' % (attr,self.__dict__[attr])
        return string

    def write(self,command):
        self.serialcon.write(self.address + command + '\r')
        #response = self.serialcon.read(15)
        #print('The response from the pump was %s' %str(response))

    def read(self,bytes=5):
        response = self.serialcon.read(bytes)

        if len(response) == 0:
            raise PumpError('%s: no response to command' % self.name)
        else:
            return response


class PumpError(Exception):
    pass
