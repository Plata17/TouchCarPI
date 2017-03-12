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
#   Class name: AudioController.py
#   Description: This class has the responsibility of
# *************************************************************************************************************


from model.AudioFile import AudioFile
from model.AudioStatus import AudioStatus
from DB.RAM_DB import RAM_DB


class AudioController:

    class __AudioController:


        def __init__(self):
            self.db = RAM_DB()
            (self.fileName, self.pathFiles) = self.db.getAudioDB()
            self.path = self.pathFiles[self.db.getSelection()]
            self.audioObject = AudioFile()
            if(self.audioObject.getStatus() == AudioStatus.NOFILE):
                self.audioObject.playAudio(self.path)
            self.observers = []

        ###############################################################################
        #OBSERVER PATTERN
        ###############################################################################
        def register(self, observer):
            if not observer in self.observers:
                self.observers.append(observer)

        def unregister(self, observer):
            if observer in self.observers:
                self.observers.remove(observer)

        def unregister_all(self):
            if self.observers:
                del self.observers[:]

        def update_observers(self, *args, **kwargs):
            for observer in self.observers:
                observer.update(*args, **kwargs)

        ###############################################################################

        def getAudioObject(self):
            return self.audioObject

        def loadAudio(self):
            self.path = self.pathFiles[self.db.getSelection()]
            if (self.audioObject.getStatus() == AudioStatus.NOFILE):
                self.audioObject.playAudio(self.path)
            else:
                self.audioObject.stopAudio()
                self.audioObject.playAudio(self.path)
            self.update_observers(self.path, test = "HW")

        def nextTrack(self):
            self.audioObject.stopAudio()
            if (self.db.getSelection()+1 <  len(self.pathFiles)):
                self.db.setSelection(self.db.getSelection()+1)
            else:
                self.db.setSelection(0)
            self.loadAudio()


        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not AudioController.instance:
            AudioController.instance = AudioController.__AudioController()

    def __getattr__(self, name):
        return getattr(self.instance, name)