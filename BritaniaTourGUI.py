#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *

class BritaniaTourGUI:
    def __init__(self, sysController, duties):
        self.dutyUIs = None
        self.window = Tk()
        self.tabFrame = None
        self.activeDutyUI = None
        self.sysController = sysController

        self.window.geometry("1000x610")
        self.window.configure(bg='white')
        self.window.title('Tour of Britain')
        self.window.mainloop()

        self.displayMenuOptions(duties)

    def displayMenuOptions(self, duties):
        pass

    def displayDutyUI(self, dutyControllerName):
        pass

    def refreshTabPanel(self, dutyControllerName):
        pass

    def setActiveDutyUI(self, IDutyUI):
        pass

