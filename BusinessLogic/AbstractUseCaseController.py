#!/usr/bin/python
#-*- coding: utf-8 -*-
import importlib
from abc import ABC, abstractmethod


class AbstractUseCaseController(ABC):
    @abstractmethod
    def _validateInput(self, input, fullValidation = True):
        pass

    @abstractmethod
    def _inputValidation(self, input, fullValidation):
        pass

    @abstractmethod
    def _constructDataModel(self, data):
        pass

    def initDutyUI(self, window):
        # get class __name substring without final "Controller" part"
        # e.g. authController => auth
        dutyName = self.__class__.__name__[:-10]
        dutyUI_Name = dutyName + "UI"

        module = importlib.import_module('Presentation.' + dutyUI_Name)
        UI_Class = getattr(module, dutyUI_Name)
        return UI_Class(self, window)