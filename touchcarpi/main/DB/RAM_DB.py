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
#   Class name: RAM_DB.py
#   Description: This class creates some list and structures with info for the application. The DB class is
#   a singleton.
# *************************************************************************************************************

import os

from .MetaDataVLC import MetaDataVLC


class RAM_DB:
    """
    This class creates some list and structures with info for the application. The DB class is
    a singleton.
    """

    #Singleton pattern
    class __RAM_DB:
        def __init__(self):
            """
            Constructor of the class.
            """

            # List all the files in the desired format (MP3, WAV...)
            self.filesInFolder = []
            # List with the full path to all the files, for get the meta data
            self.pathFiles = []
            # Selected song of the list (the number is the index)
            self.selectionIndex = 0

            for (dirpath, dirnames, filenames) in os.walk("Music"):
                for x in filenames:
                    if x.endswith(".mp3"):
                        self.filesInFolder.append(x)
                        self.pathFiles.append(os.path.join(dirpath, x))

            metaDataVLC = MetaDataVLC(self.pathFiles)
            self.metaDataList = metaDataVLC.getMetaData

            self.currentMenu = "MainMenu"


        def getAudioDB(self):
            """
            Returns the AudioDB

            :return: Three lists of strings with all the data:
            """
            return (self.filesInFolder, self.pathFiles, self.metaDataList)

        def setSelection(self, selectionIndex):
            """
            Sets the current song's index.

            :param selectionIndex: Index of the song in the list
            """
            self.selectionIndex = selectionIndex

        def getSelection(self):
            """
            Returns the index of the current song.

            :return: Index of the current song.
            """
            return self.selectionIndex

        def getIndexByPath(self, pathFile):
            """
            Returns the index of the song in the list of songs by the path of the file.

            :param pathFile: Full path of the song.
            :return: Index of the song.
            """
            return self.pathFiles.index(pathFile)

        def getIndexByFile(self, fileInFolder):
            """
            Returns the index of the song in the list of songs by the file name.

            :param fileInFolder: File name of the song.
            :return: Index of the song.
            """
            return self.filesInFolder.index(fileInFolder)

        def getCurrentMenu(self):
            """
            Returns the current menu that the user is viewing.

            :return: String whith the name of the current menu.
            """
            return self.currentMenu

        def setCurrentMenu(self, menu):
            """
            Sets the current menu that the user is viewing.

            :param menu: String with the name of the menu.
            """
            self.currentMenu = menu

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not RAM_DB.instance:
            RAM_DB.instance = RAM_DB.__RAM_DB()

    def __getattr__(self, name):
        return getattr(self.instance, name)