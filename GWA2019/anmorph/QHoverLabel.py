# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QLabel

class QHoverLabel(QLabel):
    def __init__(self):
        QLabel.__init__(self)        
    
    def enterEvent(self, ev):
        self.setStyleSheet("color: blue")

    def leaveEvent(self, ev):
        self.setStyleSheet("color: black")