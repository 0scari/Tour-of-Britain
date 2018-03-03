#!/usr/bin/python
#-*- coding: utf-8 -*-
import importlib
from abc import ABC, abstractmethod


class IDutyController(ABC):
    @abstractmethod
    def validateInput(self, input):
        pass

    @classmethod  # Late binding method
    def initDutyUI(cls, window):
        # get class name substring without final "Controller" part"
        # e.g. authController => auth
        dutyName = cls.__name__[:-10]
        dutyUI_Name = dutyName + "UI"

        module = importlib.import_module('Presentation.' + dutyUI_Name)
        UI_Class = getattr(module, dutyUI_Name)
        print(dutyUI_Name)