#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from GUI_NotificationHandler import GUI_NotificationHandler


class BritaniaTourGUI:
    def __init__(self, sysController, duties):
        self.dutyUIs = {}
        self.window = Tk()
        self.tabFrame = None
        self.menuFrame = None
        self.activeDutyUI = None
        self.__height = 610
        self.__width  = 1000
        self.__newTabButton = None
        self.sysController = sysController

        self.__setUpWindow()

        self.__setUpMenuFrame()
        self.__setUpTabFrame()
        self.displayMenuOptions(duties)

        self.__setDutyUIs(duties)

    def __del__(self):
        GUI_NotificationHandler.unsetGUI()

    def returnSelf(self):
        print("dbg")
        return self

    def __setDutyUIs(self, duties):
        for i in range(len(duties["cntrlr"])):
            self.dutyUIs[duties["cntrlr"][i]] = []

    def __setUpWindow(self):
        self.window.geometry("%sx%s" % (self.__width, self.__height))
        self.window.configure(bg='white')
        self.window.title('Tour of Britain')
        self.window.resizable(width=FALSE, height=FALSE)

    def __setUpMenuFrame(self):
        self.menuFrame = Frame(self.window, bg="red", height=self.__height, width=self.__width * 0.2)
        self.menuFrame.pack_propagate(False)
        self.menuFrame.pack(side=LEFT)

    def __setUpTabFrame(self):
        self.tabFrame = Frame(self.window, bg="#7fc7ff", height=self.__height * 0.05, width=self.__width * 0.8)
        self.tabFrame.pack_propagate(False)
        self.tabFrame.pack(side=TOP)

        self.__newTabButton = Button(self.tabFrame, text="+",  \
                                     command=lambda: self.__addDutyUI_Tab()).pack(side=RIGHT)

    def displayMenuOptions(self, duties):
        for i in range(len(duties["cntrlr"])):
            Button(self.menuFrame, background='green', text = duties["labels"][i], \
                   command=lambda cntrlr = duties["cntrlr"][i]: \
                       self.displayDutyUIs(cntrlr)).pack(fill=X, side=TOP, padx=5, pady=3)

    def displayDutyUIs(self, dutyControllerName):
        print(dutyControllerName)
        if not self.dutyUIs[dutyControllerName]:
            dutyContrlr = self.sysController.initDutyController(dutyControllerName)
            self.activeDutyUI = dutyContrlr.initDutyUI(self.window)
            self.dutyUIs[dutyControllerName].append(self.activeDutyUI)
            self.refreshTabPanel(dutyControllerName)
        else:
            self.__setActiveDutyUI(self.dutyUIs[dutyControllerName][0])

    def refreshTabPanel(self, dutyControllerName):
        self.tabFrame.destroy()
        self.__setUpTabFrame()
        for i in range(len(self.dutyUIs[dutyControllerName])):
            Button(self.tabFrame, text=str(i), \
                command=lambda uiIndx=i:
                    self.__setActiveDutyUI(self.dutyUIs[dutyControllerName][uiIndx])).\
                pack(side=LEFT)

    def __setActiveDutyUI(self, dutyUI):
        self.activeDutyUI.hide()
        self.activeDutyUI = dutyUI
        self.activeDutyUI.appear(BOTTOM)

    def raiseErrorMessg(self, header, body):
        messagebox.showerror(header, body)

    def raiseWarningMessg(self, header, body):
        messagebox.showwarning(header, body)

    def raiseInfoMessg(self, header, body):
        messagebox.showinfo(header, body)

    def startGui(self):
        self.window.mainloop()

    def __addDutyUI_Tab(self):
        dutyName = self.activeDutyUI.getDutyName()
        print("Duty name", dutyName)
        newDutyUI = self.activeDutyUI.replicate(self.window)
        self.dutyUIs[dutyName].append(newDutyUI)
        Button(self.tabFrame, text=str(len(self.dutyUIs[dutyName]) -1), \
            command=lambda dutyUI = newDutyUI:
                self.__setActiveDutyUI(dutyUI)). \
            pack(side=LEFT)
