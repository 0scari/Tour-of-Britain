class GUI_NotificationHandler:
    __gui = None

    @staticmethod
    def setGui(gui):
        GUI_NotificationHandler.__gui = gui

    @staticmethod
    def raiseInfoMessg(header, body):
        if GUI_NotificationHandler.__gui:
            GUI_NotificationHandler.__gui.raiseInfoMessg(header, body)
        else:
            raise Exception("GUI not set")

    @staticmethod
    def raiseWarningMessg(header, body):
        if GUI_NotificationHandler.__gui:
            GUI_NotificationHandler.__gui.raiseWarningMessg(header, body)
        else:
            raise Exception("GUI not set")

    @staticmethod
    def raiseErrorMessg(header, body):
        if GUI_NotificationHandler.__gui:
            GUI_NotificationHandler.__gui.raiseErrorMessg(header, body)
        else:
            raise Exception("GUI not set")

    @staticmethod
    def unsetGUI():
        GUI_NotificationHandler.__gui = None