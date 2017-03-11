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
#   Class name: Button_Back_SAM.py
#   Description: Concrete class of the "Back" button from the Select Audio Menu. This class is a
#   factory method of a PicButton.
# *************************************************************************************************************

from PyQt5.QtGui import *
from .PicButton import PicButton

class Button_Back_SAM():

    def __init__(self, controller):
        self.controller = controller

    def onClick(self):
        self.controller.changeToMenu("MainMenu")

    def createButton(self, sizeX, sizeY):
        button = PicButton(QPixmap("themes/default/img/options_mm.png"), QPixmap("themes/default/img/options_mm_pressed.png"), sizeX, sizeY, "Atrás", self.onClick)

        return button