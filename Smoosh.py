from krita import *

import .tools

class SmooshExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
    
    def setup(self):
        pass
    
    def createActions(self, window):
        tools.registerTools(window)

Krita.instance().addExtension(SmooshExtension(Krita.instance()))