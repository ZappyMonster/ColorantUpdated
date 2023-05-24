import configparser
import sys
import time
import serial
import serial.tools.list_ports
import numpy as np

from mss import mss
from termcolor import colored

class Mouse:    
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0
        self.serial_port.port = self.find_serial_port()
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[Error]', 'red'), colored('Colorant is already open or Arduino is being used by another app. Close Colorant & other apps before retrying.', 'white'))
            print(colored('Exiting...', 'red'))
            time.sleep(10)
            sys.exit()

    def find_serial_port(self):
        com_port = Settings().get('Settings', 'COM-PORT')
        port = next((port for port in serial.tools.list_ports.comports() if com_port in port.description), None)
        if port is not None:
            return port.device
        else:
            print(colored('[Error]', 'red'), colored(f'Unable to detect your specified Arduino ( {com_port} ). Please check its connection & the COM port setting in \nsettings.ini file then try again.', 'white'))
            print(colored('Exiting...', 'red'))
            time.sleep(10)
            sys.exit()

    def move(self, x, y):
        self.serial_port.write(f'MOVE{x},{y}\n'.encode())

class Settings:
    def __init__(self, config_file='settings.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)

    def get_float(self, section, key):
        return self.config.getfloat(section, key)

    def get_boolean(self, section, key):
        return self.config.getboolean(section, key)

    def set(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))

    def get_float_list(self, section, key):
        string_value = self.config.get(section, key)
        values_as_strings = string_value.strip('[]').split(',')
        return [float(value) for value in values_as_strings]

class Capture:
    def __init__(self, x, y, xfov, yfov):
        self.mss = mss()
        self.monitor = {'top': y, 'left': x, 'width': xfov, 'height': yfov}
        self.xfov = xfov
        self.yfov = yfov

    def get_screen(self):
        screenshot = self.mss.grab(self.monitor)
        return np.array(screenshot)
