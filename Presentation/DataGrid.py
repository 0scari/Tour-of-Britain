from tkinter import *
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame


class DataGrid:
    def __init__(self, parent, height = None, width = None):
        self.__frame  = VerticalScrolledFrame(parent, height)
        self.__dataSet   = []
        self.__labels = None
        self.__updateRecordCallback = None

    def setDataSet(self, dataSet):
        for object in dataSet:
            self.__dataSet.append(object)
        self.__labels = list(dataSet[0].dataToDict()) # get dict keys representing field labels
        self.__prepGrid()
        return self

    def setUpdateCallback(self, callback):
        if callable(callback):
            self.__updateRecordCallback = callback
        else:
            # Exception to programmer
            raise Exception("DataGrid: update callback not callable")

    def pack(self, side):
        return self.__frame.pack(side=side)

    def __prepGrid(self):
        if self.__labels == None or self.__dataSet == None:
            # error to programmer:
            raise Exception("Data Grid: labels or data unset")
        for i in range(len(self.__labels)):
            Label(self.__frame.interior, text=self.__labels[i]).grid(row=0, column=i)
        for i in range(len(self.__dataSet)):
            entries = {}
            data = self.__dataSet[i].getData()
            columnNr = 0
            # print(data)
            for field in data:
                entries[field] = Entry(self.__frame.interior)
                entries[field].insert(END, data[field])
                entries[field].config(state=DISABLED)
                entries[field].grid(row=i+1, column=columnNr)
                self.__frame.interior.grid_columnconfigure(columnNr, weight=1)
                columnNr += 1
            editBttn = Button(self.__frame.interior, text="edit")
            editBttn.grid(row=i+1, column=len(data) + 1)
            delBttn  = self.__prepDeleteButton()
            delBttn.grid(row=i+1, column=len(data) + 2)
            editBttn.bind('<Button-1>', (
                lambda event, entries=entries, buttn1=editBttn, row=i+1, col=len(data)+2, buttn2=delBttn:
                    [self.__editRecordCallback(event, buttn1, entries),
                     self.__switchDeletionButtonState(delBttn, col, row)]))

    def __editRecordCallback(self, event,  button, entries):
        if button["text"] == "edit":
            button.config(text="done")
            for fieldKey in entries:
                if fieldKey != "id" and fieldKey != "createdBy":
                    entries[fieldKey].config(state=NORMAL)
        else:
            button.config(text="edit")
            data = {}
            for fieldKey in entries:
                data[fieldKey] = entries[fieldKey].get()
                entries[fieldKey].config(state=DISABLED)
            self.__updateRecordCallback(data)

    def __prepDeleteButton(self):
        # set up label with picture
        photo = PhotoImage(file=r"bin.gif")
        label = Label(self.__frame.interior, image=photo, width=20, height=20, )
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        #  set up on-click event
        # label.bind("<Button-1>", lambda event: self.__addDutyUI_Tab())
        return label

    def __switchDeletionButtonState(self, button, col, row):
        if button.winfo_ismapped():
            button.grid_forget()
        else:
            button.grid(row=row, column=col, columnspan=1)

    def destruct(self):
        self.__frame.destruct()