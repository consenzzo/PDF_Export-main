# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from teste_class import CustomListWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(978, 706)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(84, 16777215))

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(84, 16777215))

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(546, 0))
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 566, 631))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(546, 0))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.listWidget = CustomListWidget()
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(240, 0))
        self.listWidget.setMaximumSize(QSize(240, 16777215))
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setIconSize(QSize(300, 300))
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        self.pushButton_2.setIcon(icon)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_4.addWidget(self.pushButton_9)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 16777215))
        self.lineEdit.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border: 0px;")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 6, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"P\u00e1gina", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u2192", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u2190", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Zoom", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Add P\u00e1g.", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Delete P\u00e1g.", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Mover", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"CIMA \u2191", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"BAIXO \u2193", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"/ 0", None))
    # retranslateUi

