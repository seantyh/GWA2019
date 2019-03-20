# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal

class QHoverLabel(QLabel):
    label_clicked = Signal(str)
    def __init__(self):
        QLabel.__init__(self)                
    
    def enterEvent(self, ev):
        self.setStyleSheet("color: blue")

    def leaveEvent(self, ev):
        self.setStyleSheet("color: black")
    
    def mousePressEvent(self, ev):
        self.label_clicked.emit(self.text())
