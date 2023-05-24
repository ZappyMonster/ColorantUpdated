import os
import sys
import time
import pyautogui
import ctypes

from termcolor import colored
from colorant import Colorant
from other import Settings

class Main:
    os.system('color')
    KEY_NAMES = {
        0x01: "L-Mouse Button", 0x02: "R-Mouse Button", 0x04: "MButton", 0x05: "X1 Mouse Button", 
        0x06: "X2 Mouse Button", 0x08: "Backspace", 0x09: "Tab", 0x0D: "Enter", 0x10: "Shift", 
        0x11: "Ctrl", 0x12: "Alt", 0x14: "CapsLock", 0x1B: "Esc", 0x20: "Spacebar", 0x25: "Left", 
        0x26: "Up", 0x27: "Right", 0x28: "Down", 0x30: "0", 0x31: "1", 0x32: "2", 0x33: "3", 
        0x34: "4", 0x35: "5", 0x36: "6", 0x37: "7", 0x38: "8", 0x39: "9", 0x41: "A", 0x42: "B", 
        0x43: "C", 0x44: "D", 0x45: "E", 0x46: "F", 0x47: "G", 0x48: "H", 0x49: "I", 0x4A: "J", 
        0x4B: "K", 0x4C: "L", 0x4D: "M", 0x4E: "N", 0x4F: "O", 0x50: "P", 0x51: "Q", 0x52: "R", 
        0x53: "S", 0x54: "T", 0x55: "U", 0x56: "V", 0x57: "W", 0x58: "X", 0x59: "Y", 0x5A: "Z", 
        0x70: "F1", 0x71: "F2", 0x72: "F3", 0x73: "F4", 0x74: "F5", 0x75: "F6", 
        0x76: "F7", 0x77: "F8", 0x78: "F9", 0x79: "F10", 0x7A: "F11", 0x7B: "F12"}

    def __init__(self):
        self.settings = Settings()
        self.monitor = pyautogui.size()
        self.CENTER_X, self.CENTER_Y = self.monitor.width // 2, self.monitor.height // 2
        self.XFOV = self.settings.get_int('Settings', 'X-FOV')
        self.YFOV = self.settings.get_int('Settings', 'Y-FOV')
        self.colorant = Colorant(
            self.CENTER_X - self.XFOV // 2, self.CENTER_Y - self.YFOV // 2,
            self.XFOV, self.YFOV)
    
    def cmd(self, width, height):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
            style &= ~0x00040000
            style &= ~0x00010000
            ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)
        STD_OUTPUT_HANDLE_ID = ctypes.c_ulong(0xFFFFFFF5)
        windll = ctypes.windll.kernel32
        handle = windll.GetStdHandle(STD_OUTPUT_HANDLE_ID)
        rect = ctypes.wintypes.SMALL_RECT(0, 0, width - 1, height - 1)
        windll.SetConsoleScreenBufferSize(handle, ctypes.wintypes._COORD(width, height))
        windll.SetConsoleWindowInfo(handle, ctypes.c_int(True), ctypes.pointer(rect))

    def print_logo(self):
        os.system(f"title Colorant")
        print(colored('''
                                     ▄▄·       ▄▄▌        ▄▄▄   ▄▄▄·  ▐ ▄ ▄▄▄▄▄
                                    ▐█ ▌▪▪     ██•  ▪     ▀▄ █·▐█ ▀█ •█▌▐█•██  
                                    ██ ▄▄ ▄█▀▄ ██▪   ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ▐█▐▐▌ ▐█.▪
                                    ▐███▌▐█▌.▐▌▐█▌▐▌▐█▌.▐▌▐█•█▌▐█ ▪▐▌██▐█▌ ▐█▌·
                                    ·▀▀▀  ▀█▄▀▪.▀▀▀  ▀█▄▀▪.▀  ▀ ▀  ▀ ▀▀ █▪ ▀▀▀
                                    
                                                Github Free Version\n''', 'cyan'))

    def print_info(self):
        try:
            print(colored('[', 'dark_grey') + colored('Your KeyBinds', 'cyan') + colored(']', 'dark_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' Hold {self.KEY_NAMES[self.colorant.AIMBOT_KEY]}', 'light_grey') + colored(' → Aimbot', 'light_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' Press {self.KEY_NAMES[self.colorant.TOGGLE_KEY]}', 'light_grey') + colored(' → Toggle ON/OFF', 'light_grey'))
            print()
            print(colored('[', 'dark_grey') + colored('Information', 'cyan') + colored(']', 'dark_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' This is a free open source aimbot made for educational purposes, if someone trying to sell this for you\n11/10 you are being scammed.', 'light_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' Colorant uses hsv color detection and some sort of screen capturing tool to interact with the specified\ncolors on the screen, without modifying game memory or files.', 'light_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' Last update → 23 MAY 2023.', 'light_grey'))
            print(colored('[', 'dark_grey') + colored('●', 'light_grey') + colored(']', 'dark_grey') +
                  colored(f' Find us here: {colored("https://github.com/hafyzwithawhy/Colorant", "cyan", attrs=["underline"])}', 'light_grey'))
            print()
        except:
            os.system('cls')
            print(colored('[Error]', 'red'), colored('Invalid value found in settings.ini', 'white'))
            time.sleep(10)
            sys.exit()

    def run(self):
        self.cmd(125,30)
        self.print_logo()
        self.print_info()
        self.colorant.listen()

if __name__ == '__main__':
    Main().run()
