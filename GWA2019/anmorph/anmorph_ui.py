# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GWA2019/anmorph/anmorph_ui.ui',
# licensing of 'GWA2019/anmorph/anmorph_ui.ui' applies.
#
# Created: Wed Mar 20 21:34:38 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lvw_words = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvw_words.sizePolicy().hasHeightForWidth())
        self.lvw_words.setSizePolicy(sizePolicy)
        self.lvw_words.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lvw_words.setFont(font)
        self.lvw_words.setObjectName("lvw_words")
        self.horizontalLayout_6.addWidget(self.lvw_words)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_note = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_note.sizePolicy().hasHeightForWidth())
        self.line_note.setSizePolicy(sizePolicy)
        self.line_note.setMinimumSize(QtCore.QSize(0, 36))
        self.line_note.setObjectName("line_note")
        self.horizontalLayout_2.addWidget(self.line_note)
        self.lab_pos = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_pos.sizePolicy().hasHeightForWidth())
        self.lab_pos.setSizePolicy(sizePolicy)
        self.lab_pos.setMinimumSize(QtCore.QSize(48, 36))
        self.lab_pos.setMaximumSize(QtCore.QSize(64, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lab_pos.setFont(font)
        self.lab_pos.setObjectName("lab_pos")
        self.horizontalLayout_2.addWidget(self.lab_pos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.hbox_targets = QtWidgets.QHBoxLayout()
        self.hbox_targets.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.hbox_targets.setObjectName("hbox_targets")
        self.lab_target_base = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_target_base.sizePolicy().hasHeightForWidth())
        self.lab_target_base.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.lab_target_base.setFont(font)
        self.lab_target_base.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_target_base.setObjectName("lab_target_base")
        self.hbox_targets.addWidget(self.lab_target_base)
        self.verticalLayout_2.addLayout(self.hbox_targets)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lab_question1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_question1.sizePolicy().hasHeightForWidth())
        self.lab_question1.setSizePolicy(sizePolicy)
        self.lab_question1.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_question1.setFont(font)
        self.lab_question1.setObjectName("lab_question1")
        self.horizontalLayout.addWidget(self.lab_question1)
        self.btn_item1_no = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_item1_no.sizePolicy().hasHeightForWidth())
        self.btn_item1_no.setSizePolicy(sizePolicy)
        self.btn_item1_no.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item1_no.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item1_no.setFlat(False)
        self.btn_item1_no.setObjectName("btn_item1_no")
        self.horizontalLayout.addWidget(self.btn_item1_no)
        self.btn_item1_na = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_item1_na.sizePolicy().hasHeightForWidth())
        self.btn_item1_na.setSizePolicy(sizePolicy)
        self.btn_item1_na.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item1_na.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item1_na.setObjectName("btn_item1_na")
        self.horizontalLayout.addWidget(self.btn_item1_na)
        self.btn_item1_yes = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_item1_yes.sizePolicy().hasHeightForWidth())
        self.btn_item1_yes.setSizePolicy(sizePolicy)
        self.btn_item1_yes.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item1_yes.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item1_yes.setObjectName("btn_item1_yes")
        self.horizontalLayout.addWidget(self.btn_item1_yes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lab_question2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_question2.sizePolicy().hasHeightForWidth())
        self.lab_question2.setSizePolicy(sizePolicy)
        self.lab_question2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_question2.setFont(font)
        self.lab_question2.setObjectName("lab_question2")
        self.horizontalLayout_3.addWidget(self.lab_question2)
        self.btn_item2_no = QtWidgets.QPushButton(self.centralwidget)
        self.btn_item2_no.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item2_no.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item2_no.setObjectName("btn_item2_no")
        self.horizontalLayout_3.addWidget(self.btn_item2_no)
        self.btn_item2_na = QtWidgets.QPushButton(self.centralwidget)
        self.btn_item2_na.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item2_na.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item2_na.setObjectName("btn_item2_na")
        self.horizontalLayout_3.addWidget(self.btn_item2_na)
        self.btn_item2_yes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_item2_yes.setMinimumSize(QtCore.QSize(60, 48))
        self.btn_item2_yes.setMaximumSize(QtCore.QSize(80, 48))
        self.btn_item2_yes.setObjectName("btn_item2_yes")
        self.horizontalLayout_3.addWidget(self.btn_item2_yes)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_na = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_na.sizePolicy().hasHeightForWidth())
        self.btn_na.setSizePolicy(sizePolicy)
        self.btn_na.setMinimumSize(QtCore.QSize(250, 0))
        self.btn_na.setMaximumSize(QtCore.QSize(260, 16777215))
        self.btn_na.setObjectName("btn_na")
        self.horizontalLayout_4.addWidget(self.btn_na)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btn_prev_entry = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev_entry.sizePolicy().hasHeightForWidth())
        self.btn_prev_entry.setSizePolicy(sizePolicy)
        self.btn_prev_entry.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_prev_entry.setObjectName("btn_prev_entry")
        self.horizontalLayout_7.addWidget(self.btn_prev_entry)
        self.btn_next_entry = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_entry.sizePolicy().hasHeightForWidth())
        self.btn_next_entry.setSizePolicy(sizePolicy)
        self.btn_next_entry.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_next_entry.setObjectName("btn_next_entry")
        self.horizontalLayout_7.addWidget(self.btn_next_entry)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Anmorph", None, -1))
        self.lab_pos.setText(QtWidgets.QApplication.translate("MainWindow", "POS", None, -1))
        self.lab_target_base.setText(QtWidgets.QApplication.translate("MainWindow", "文", None, -1))
        self.lab_question1.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel11111", None, -1))
        self.btn_item1_no.setText(QtWidgets.QApplication.translate("MainWindow", "否", None, -1))
        self.btn_item1_na.setText(QtWidgets.QApplication.translate("MainWindow", "？", None, -1))
        self.btn_item1_yes.setText(QtWidgets.QApplication.translate("MainWindow", "是", None, -1))
        self.lab_question2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.btn_item2_no.setText(QtWidgets.QApplication.translate("MainWindow", "否", None, -1))
        self.btn_item2_na.setText(QtWidgets.QApplication.translate("MainWindow", "？", None, -1))
        self.btn_item2_yes.setText(QtWidgets.QApplication.translate("MainWindow", "是", None, -1))
        self.btn_na.setText(QtWidgets.QApplication.translate("MainWindow", "不適用", None, -1))
        self.btn_prev_entry.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.btn_next_entry.setText(QtWidgets.QApplication.translate("MainWindow", ">>", None, -1))

