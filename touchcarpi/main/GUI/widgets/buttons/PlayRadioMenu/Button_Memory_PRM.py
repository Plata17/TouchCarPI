#*************************************************************************************************************
#  ________  ________  ___  ___  ________  ___  ___  ________  ________  ________  ________  ___
# |\___   ___\\   __  \|\  \|\  \|\   ____\|\  \|\  \|\   ____\|\   __  \|\   __  \|\   __  \|\  \
# \|___ \  \_\ \  \|\  \ \  \\\  \ \  \___|\ \  \\\  \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \
#      \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \   __  \ \  \    \ \   __  \ \   _  _\ \   ____\ \  \
#       \ \  \ \ \  \\\  \ \  \\\  \ \  \____\ \  \ \  \ \  \____\ \  \ \  \ \  \\  \\ \  \___|\ \  \
#        \ \__\ \ \_______\ \_______\ \_______\ \__\ \__\ \_______\ \__\ \__\ \__\\ _\\ \__\    \ \__\
#         \|__|  \|_______|\|_______|\|_______|\|__|\|__|\|_______|\|__|\|__|\|__|\|__|\|__|     \|__|
#
# *************************************************************************************************************
#   Author: Rafael Fernández Flores (@Plata17 at GitHub)
#   Class name: Button_Memory_PRM.py
#   Description: Concrete class of the "Memory" button from the Play Radio Menu. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from ..PicButton import PicButton
from DB.RAM_DB import RAM_DB
from model.AudioController import AudioController

class Button_Memory_PRM():

    def __init__(self, buttonId):
        self.buttonId = buttonId
        self.db = RAM_DB()
        self.radioChannels = self.db.getRadioChannels()
        self.audioController = AudioController()

    def onClick(self, isLongClick = False):
        if(self.audioController.getGUICoolDown() == False and isLongClick == False):
            self.audioController.startGUICoolDown(1)
            # If there's an entry in the XML with memorized channel, we assign it to this button/memory bank
            if(self.radioChannels[self.buttonId] != None):
                self.audioController.setCurrentFMFrequency(self.radioChannels[self.buttonId][0])
        elif ((self.audioController.getGUICoolDown() == False and isLongClick == True)):
            # On long click, we memorize the current radio channel to this memory bank :)
            self.db.setRadioChannel(self.buttonId, self.audioController.getCurrentFMFrequency(), self.audioController.getCurrentFMStationName())
            self.radioChannels = self.db.getRadioChannels()
            self.audioController.updateRadioObservers()



    def createButton(self, sizeX, sizeY):
        button = PicButton(QPixmap("themes/default/img/MemoryButton.png"), QPixmap("themes/default/img/MemoryButton_Pressed.png"), sizeX, sizeY, str(self.buttonId), self.onClick)

        return button