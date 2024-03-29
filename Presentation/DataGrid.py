from tkinter import *
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame
from GUI_NotificationHandler import GUI_NotificationHandler


class DataGrid:
    def __init__(self, parent, height=None, width=None):
        self.__frame = VerticalScrolledFrame(parent, height)
        self.__dataSet = []
        self.__labels = None
        self.__updateRecordCallback = None
        self.__deletionRecordCallback = None

    def setDataSet(self, dataSet):
        for object in dataSet:
            self.__dataSet.append(object)
        self.__labels = list(dataSet[0].dataToDict())  # get dict keys representing field labels
        self.__prepGrid()
        return self

    def setUpdateCallback(self, callback):
        if callable(callback):
            self.__updateRecordCallback = callback
        else:
            # Exception to programmer
            raise Exception("DataGrid: update callback not callable")

    def setDeletionCallback(self, callback):
        if callable(callback):
            self.__deletionRecordCallback = callback
        else:
            # Exception to programmer
            raise Exception("DataGrid: deletion callback not callable")

    def pack(self, side):
        if self.__updateRecordCallback == None \
         or self.__deletionRecordCallback == None:
            raise Exception("DataGrid: deletion or updating callback is not set")
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
                if field == "id" or field == "createdBy":
                    entries[field] = Entry(self.__frame.interior, width=10)
                else:
                    entries[field] = Entry(self.__frame.interior)
                entries[field].insert(END, data[field])
                entries[field].config(state=DISABLED)
                entries[field].grid(row=i + 1, column=columnNr)
                self.__frame.interior.grid_columnconfigure(columnNr, weight=1)
                columnNr += 1
            editBttn = Button(self.__frame.interior, text="edit")
            editBttn.grid(row=i + 1, column=len(data) + 1)
            delBttn = self.__prepDeleteButton(i)
            delBttn.grid(row=i + 1, column=len(data) + 2)
            editBttn.bind('<Button-1>', (
                lambda event, entries=entries, buttn1=editBttn, row=i + 1, col=len(data) + 2, buttn2=delBttn:
                [self.__editRecordCallback(event, buttn1, entries),
                 self.__switchDeletionButtonState(delBttn, col, row)]))

    def __editRecordCallback(self, event, button, entries):
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

    def __prepDeleteButton(self, dataItemIndex):
        # set up label with picture
        photo = PhotoImage(file=r"bin.gif")
        label = Label(self.__frame.interior, image=photo, width=20, height=20, )
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        #  set up on-click event
        label.bind("<Button-1>", lambda event: self.__deletionProcedure(dataItemIndex))
        return label

    def __switchDeletionButtonState(self, button, col, row):
        if button.winfo_ismapped():
            button.grid_forget()
        else:
            button.grid(row=row, column=col, columnspan=1)

    def refresh(self, dataSet = None):
        if dataSet:
            self.__dataSet = dataSet
        print(self.__frame.interior.grid_slaves())
        self.__frame.interior.grid_propagate(False)
        for item in self.__frame.interior.grid_slaves():
            item.grid_forget()
        self.__prepGrid()

    def destruct(self):
        self.__frame.destruct()

    def __deletionProcedure(self, dataItemIndex):
        customerId = self.__dataSet[dataItemIndex].getData()["id"]
        deleted = self.__deletionRecordCallback(customerId)
        if deleted:
            print("deleted")
            del self.__dataSet[dataItemIndex]
            self.refresh()
