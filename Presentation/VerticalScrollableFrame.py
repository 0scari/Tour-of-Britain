from tkinter import *
from tkinter import ttk

# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable _mainFrame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable _mainFrame
    * Construct and pack/place/grid normally
    * This _mainFrame only allows vertical scrolling
    """
    def __init__(self, parent, height = None, width = None, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a self.__canvas object and a vertical scrollbar for scrolling it
        self.__vscrollbar = Scrollbar(self, orient=VERTICAL)
        self.__vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.__canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=self.__vscrollbar.set)
        self.__canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.__vscrollbar.config(command=self.__canvas.yview)

        # reset the view
        self.__canvas.xview_moveto(0)
        self.__canvas.yview_moveto(0)

        # create a _mainFrame inside the self.__canvas which will be scrolled with it
        self.interior = interior = Frame(self.__canvas)
        interior_id = self.__canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        self.__canvas.config(height=height)
        # track changes to the self.__canvas and _mainFrame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner _mainFrame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            self.__canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != self.__canvas.winfo_width():
                # update the self.__canvas's width to fit the inner _mainFrame
                self.__canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != self.__canvas.winfo_width():
                # update the inner _mainFrame's width to fill the self.__canvas
                self.__canvas.itemconfigure(interior_id, width=self.__canvas.winfo_width())
        self.__canvas.bind('<Configure>', _configure_canvas)
        
    def destruct(self):
        self.__canvas.pack_forget()
        self.__vscrollbar.pack_forget()
