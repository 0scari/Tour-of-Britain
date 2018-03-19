#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from GUI_NotificationHandler import GUI_NotificationHandler
from tkinter import ttk


class BritaniaTourGUI(Frame):
    def __init__(self, sysController, duties):
        self.__window = Tk()
        self.__window.update()
        Frame.__init__(self, self.__window)
        self.__style = ttk.Style()
        self.__style.theme_use("default")
        self.__tabFrame = None
        self.__menuFrame = None
        self.__activeDutyUI = None
        self.__height = 610
        self.__width  = 1000
        self.__newTabButton = None
        self.__sysController = sysController
        self.__useCaseUIs = {}
        self.__setUpWindow()
        self.__setUpMenuFrame()
        self.__setUpTabFrame()
        self.__displayMenuOptions(duties)
        self.__setDutyUIs(duties)
        GUI_NotificationHandler.setGui(self)

    def __del__(self):
        GUI_NotificationHandler.unsetGUI()

    def __setDutyUIs(self, duties):
        for i in range(len(duties["cntrlr"])):
            self.__useCaseUIs[duties["cntrlr"][i]] = []

    def __setUpWindow(self):
        self.__window.geometry("%sx%s" % (self.__width, self.__height))
        self.__window.configure(bg='white')
        self.__window.title('Tour of Britain')
        self.__window.resizable(width=FALSE, height=FALSE)

    def __setUpMenuFrame(self):
        self.__menuFrame = Frame(self.__window, bg="#F0F0F0", height=self.__height, width=self.__width * 0.2)
        self.__menuFrame.pack_propagate(False)
        self.__menuFrame.pack(side=LEFT)
        # set up label with picture
        photo = PhotoImage(file=r"menuText200x55.gif")
        label = Label(self.__menuFrame, image=photo, width=200, height=38)
        label.pack(side=TOP, fill=X, pady=0)
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        #  set up on-click event
        label.bind("<Button-1>", lambda event: self.__activeDutyUI.hide())

    def __setUpTabFrame(self):
        self.__tabFrame = Frame(self.__window, bg="#DEDEDE", height=self.__height * 0.05, width=self.__width * 0.8)
        self.__tabFrame.pack_propagate(False)
        self.__tabFrame.pack(side=TOP)
        # set up label with picture
        photo = PhotoImage(file=r"newTabx29.gif")
        label = Label(self.__tabFrame, image=photo, width=29, height=29, )
        label.pack(side=RIGHT)
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        # set up on-click event
        label.bind("<Button-1>", lambda event: self.__addDutyUI_Tab())

    def __displayMenuOptions(self, duties):

        for i in range(len(duties["cntrlr"])):
            ttk.Button(self.__menuFrame, text = duties["labels"][i], \
                       command=lambda cntrlr = duties["cntrlr"][i]: \
                       self.__displayUseCaseUIs(cntrlr)).pack(fill=X, side=TOP, padx=5, pady=3)

    def __displayUseCaseUIs(self, useCaseControllerName):
        self.label.pack_forget()
        # if an entry in the list of the Use Case UIs with the given controller __name exists
        if len(self.__useCaseUIs[useCaseControllerName]) == 0:
            dutyContrlr = self.__sysController.initDutyController(useCaseControllerName)
            if dutyContrlr:
                self.__activeDutyUI = dutyContrlr.initDutyUI(self.__window)
                self.__useCaseUIs[useCaseControllerName].append(self.__activeDutyUI)
                self.__refreshTabPanel(useCaseControllerName)
        else: # Else, pick the first one
            self.__setActiveUseCaseUI(self.__useCaseUIs[useCaseControllerName][0])

    def __refreshTabPanel(self, dutyControllerName):
        self.__tabFrame.destroy()
        self.__setUpTabFrame()
        for i in range(len(self.__useCaseUIs[dutyControllerName])):
            ttk.Button(self.__tabFrame, command=lambda uiIndx=i, text=str(i + 1):
                    self.__setActiveUseCaseUI(self.__useCaseUIs[dutyControllerName][uiIndx])).\
                pack(side=LEFT)

    def __setActiveUseCaseUI(self, dutyUI):
        self.__activeDutyUI.hide()
        self.__activeDutyUI = dutyUI
        self.__activeDutyUI.appear(BOTTOM)

    def startGui(self):
        # set up label with picture
        photo = PhotoImage(file=r"bus.gif")
        self.label = Label(self.__window, image=photo, width=500, height=400, )
        self.label.pack(pady=(50,0))
        self.label.config(bg='systemTransparent')
        self.label.image = photo  # keep a reference!
        self.__window.mainloop()

    def raiseErrorMessg(self, header, body):
        messagebox.showerror(header, body)

    def raiseWarningMessg(self, header, body):
        messagebox.showwarning(header, body)

    def raiseInfoMessg(self, header, body):
        messagebox.showinfo(header, body)

    def raiseDialog(self, header, body):
        result = messagebox.askquestion(header, body, icon='warning')
        if result == 'yes':
            return True
        else:
            return False

    def __addDutyUI_Tab(self):
        dutyName = self.__activeDutyUI.getDutyName()
        newDutyUI = self.__activeDutyUI.replicate(self.__window)
        self.__useCaseUIs[dutyName].append(newDutyUI)
        ttk.Button(self.__tabFrame, \
                   command=lambda dutyUI = newDutyUI:
                self.__setActiveUseCaseUI(dutyUI)). \
            pack(side=LEFT)
