# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu2_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCommandLinkButton,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidgetItem,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QToolBox, QVBoxLayout, QWidget)

from class_custom import (CustomLabel, CustomListWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(1480, 830)
        Menu.setStyleSheet(u"background-color: rgb(0, 142, 255);")
        self.gridLayout_2 = QGridLayout(Menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.toolBox = QToolBox(Menu)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QSize(210, 500))
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setStyleSheet(u"background-color: rgb(0, 142, 255); color: rgb(255, 255, 255); font: 700 14pt \"Yu Gothic UI\";")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 210, 690))
        self.page.setMinimumSize(QSize(0, 40))
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalGroupBox = QGroupBox(self.page)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        sizePolicy.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy)
        self.verticalGroupBox.setMinimumSize(QSize(210, 0))
        self.verticalGroupBox.setStyleSheet(u"background-color: rgb(255, 255, 255); color: rgb(0, 142, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_new_file = QCommandLinkButton(self.verticalGroupBox)
        self.add_new_file.setObjectName(u"add_new_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_new_file.sizePolicy().hasHeightForWidth())
        self.add_new_file.setSizePolicy(sizePolicy1)
        self.add_new_file.setMinimumSize(QSize(198, 0))
        self.add_new_file.setMaximumSize(QSize(16777215, 50))
        self.add_new_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_new_file.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.add_new_file.setCheckable(False)
        self.add_new_file.setChecked(False)

        self.verticalLayout_2.addWidget(self.add_new_file)

        self.add_m_d_agua = QCommandLinkButton(self.verticalGroupBox)
        self.add_m_d_agua.setObjectName(u"add_m_d_agua")
        sizePolicy1.setHeightForWidth(self.add_m_d_agua.sizePolicy().hasHeightForWidth())
        self.add_m_d_agua.setSizePolicy(sizePolicy1)
        self.add_m_d_agua.setMinimumSize(QSize(198, 0))
        self.add_m_d_agua.setMaximumSize(QSize(16777215, 50))
        self.add_m_d_agua.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_m_d_agua.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.add_m_d_agua.setCheckable(False)

        self.verticalLayout_2.addWidget(self.add_m_d_agua)

        self.add_n_pg = QCommandLinkButton(self.verticalGroupBox)
        self.add_n_pg.setObjectName(u"add_n_pg")
        sizePolicy1.setHeightForWidth(self.add_n_pg.sizePolicy().hasHeightForWidth())
        self.add_n_pg.setSizePolicy(sizePolicy1)
        self.add_n_pg.setMinimumSize(QSize(198, 0))
        self.add_n_pg.setMaximumSize(QSize(16777215, 50))
        self.add_n_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_n_pg.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.add_n_pg.setCheckable(False)

        self.verticalLayout_2.addWidget(self.add_n_pg)

        self.delete_page_menu = QCommandLinkButton(self.verticalGroupBox)
        self.delete_page_menu.setObjectName(u"delete_page_menu")
        sizePolicy1.setHeightForWidth(self.delete_page_menu.sizePolicy().hasHeightForWidth())
        self.delete_page_menu.setSizePolicy(sizePolicy1)
        self.delete_page_menu.setMinimumSize(QSize(198, 0))
        self.delete_page_menu.setMaximumSize(QSize(16777215, 50))
        self.delete_page_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_page_menu.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.delete_page_menu.setCheckable(False)

        self.verticalLayout_2.addWidget(self.delete_page_menu)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout.addWidget(self.verticalGroupBox)

        self.toolBox.addItem(self.page, u"Editar")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 210, 690))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy2)
        self.verticalGroupBox_2 = QGroupBox(self.page_2)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalGroupBox_2.setGeometry(QRect(0, 0, 210, 681))
        sizePolicy2.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy2)
        self.verticalGroupBox_2.setMinimumSize(QSize(210, 0))
        self.verticalGroupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255); color: rgb(0, 142, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pdf_to_word = QCommandLinkButton(self.verticalGroupBox_2)
        self.pdf_to_word.setObjectName(u"pdf_to_word")
        sizePolicy1.setHeightForWidth(self.pdf_to_word.sizePolicy().hasHeightForWidth())
        self.pdf_to_word.setSizePolicy(sizePolicy1)
        self.pdf_to_word.setMinimumSize(QSize(198, 0))
        self.pdf_to_word.setMaximumSize(QSize(16777215, 50))
        self.pdf_to_word.setCursor(QCursor(Qt.PointingHandCursor))
        self.pdf_to_word.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.pdf_to_word.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pdf_to_word)

        self.pdf_to_excel = QCommandLinkButton(self.verticalGroupBox_2)
        self.pdf_to_excel.setObjectName(u"pdf_to_excel")
        sizePolicy1.setHeightForWidth(self.pdf_to_excel.sizePolicy().hasHeightForWidth())
        self.pdf_to_excel.setSizePolicy(sizePolicy1)
        self.pdf_to_excel.setMinimumSize(QSize(198, 0))
        self.pdf_to_excel.setMaximumSize(QSize(16777215, 50))
        self.pdf_to_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pdf_to_excel.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.pdf_to_excel.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pdf_to_excel)

        self.expo_Img_Button_png = QCommandLinkButton(self.verticalGroupBox_2)
        self.expo_Img_Button_png.setObjectName(u"expo_Img_Button_png")
        sizePolicy1.setHeightForWidth(self.expo_Img_Button_png.sizePolicy().hasHeightForWidth())
        self.expo_Img_Button_png.setSizePolicy(sizePolicy1)
        self.expo_Img_Button_png.setMinimumSize(QSize(198, 0))
        self.expo_Img_Button_png.setMaximumSize(QSize(16777215, 50))
        self.expo_Img_Button_png.setCursor(QCursor(Qt.PointingHandCursor))
        self.expo_Img_Button_png.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.expo_Img_Button_png.setCheckable(True)

        self.verticalLayout_4.addWidget(self.expo_Img_Button_png)

        self.expo_Img_Button_jpg = QCommandLinkButton(self.verticalGroupBox_2)
        self.expo_Img_Button_jpg.setObjectName(u"expo_Img_Button_jpg")
        sizePolicy1.setHeightForWidth(self.expo_Img_Button_jpg.sizePolicy().hasHeightForWidth())
        self.expo_Img_Button_jpg.setSizePolicy(sizePolicy1)
        self.expo_Img_Button_jpg.setMinimumSize(QSize(198, 0))
        self.expo_Img_Button_jpg.setMaximumSize(QSize(16777215, 50))
        self.expo_Img_Button_jpg.setCursor(QCursor(Qt.PointingHandCursor))
        self.expo_Img_Button_jpg.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.expo_Img_Button_jpg.setCheckable(True)

        self.verticalLayout_4.addWidget(self.expo_Img_Button_jpg)

        self.word_to_pdf = QCommandLinkButton(self.verticalGroupBox_2)
        self.word_to_pdf.setObjectName(u"word_to_pdf")
        sizePolicy1.setHeightForWidth(self.word_to_pdf.sizePolicy().hasHeightForWidth())
        self.word_to_pdf.setSizePolicy(sizePolicy1)
        self.word_to_pdf.setMinimumSize(QSize(198, 0))
        self.word_to_pdf.setMaximumSize(QSize(16777215, 50))
        self.word_to_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.word_to_pdf.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.word_to_pdf.setCheckable(True)

        self.verticalLayout_4.addWidget(self.word_to_pdf)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Converter Arquivo")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 210, 690))
        self.verticalGroupBox_3 = QGroupBox(self.page_3)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        self.verticalGroupBox_3.setGeometry(QRect(0, 0, 210, 641))
        sizePolicy.setHeightForWidth(self.verticalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_3.setSizePolicy(sizePolicy)
        self.verticalGroupBox_3.setMinimumSize(QSize(210, 0))
        self.verticalGroupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255); color: rgb(0, 142, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_password = QCommandLinkButton(self.verticalGroupBox_3)
        self.add_password.setObjectName(u"add_password")
        sizePolicy1.setHeightForWidth(self.add_password.sizePolicy().hasHeightForWidth())
        self.add_password.setSizePolicy(sizePolicy1)
        self.add_password.setMinimumSize(QSize(198, 0))
        self.add_password.setMaximumSize(QSize(16777215, 50))
        self.add_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_password.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.add_password.setCheckable(True)

        self.verticalLayout_3.addWidget(self.add_password)

        self.remove_password = QCommandLinkButton(self.verticalGroupBox_3)
        self.remove_password.setObjectName(u"remove_password")
        sizePolicy1.setHeightForWidth(self.remove_password.sizePolicy().hasHeightForWidth())
        self.remove_password.setSizePolicy(sizePolicy1)
        self.remove_password.setMinimumSize(QSize(198, 0))
        self.remove_password.setMaximumSize(QSize(16777215, 50))
        self.remove_password.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_password.setStyleSheet(u"QCommandLinkButton {font: 11pt \"Segoe UI\"; } QCommandLinkButton:checked {background-color: rgb(0, 166, 237);color: white; }")
        self.remove_password.setCheckable(True)

        self.verticalLayout_3.addWidget(self.remove_password)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_3, u"Seguran\u00e7a")

        self.gridLayout_5.addWidget(self.toolBox, 0, 0, 1, 1)

        self.frame = QFrame(Menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 600))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.back_pg = CustomLabel(self.frame)
        self.back_pg.setObjectName(u"back_pg")
        self.back_pg.setMinimumSize(QSize(30, 30))
        self.back_pg.setMaximumSize(QSize(30, 30))
        self.back_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_pg.setTextFormat(Qt.AutoText)
        self.back_pg.setScaledContents(True)
        self.back_pg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.back_pg)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.n_pg_edit = QLineEdit(self.frame)
        self.n_pg_edit.setObjectName(u"n_pg_edit")
        self.n_pg_edit.setMinimumSize(QSize(50, 0))
        self.n_pg_edit.setMaximumSize(QSize(50, 16777215))
        self.n_pg_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.n_pg_edit)

        self.n_pg_total = QLabel(self.frame)
        self.n_pg_total.setObjectName(u"n_pg_total")
        self.n_pg_total.setMinimumSize(QSize(50, 30))
        self.n_pg_total.setMaximumSize(QSize(50, 30))
        self.n_pg_total.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.n_pg_total)

        self.next_pg = CustomLabel(self.frame)
        self.next_pg.setObjectName(u"next_pg")
        self.next_pg.setMinimumSize(QSize(30, 30))
        self.next_pg.setMaximumSize(QSize(30, 30))
        self.next_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_pg.setTextFormat(Qt.AutoText)
        self.next_pg.setScaledContents(True)
        self.next_pg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.next_pg)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.line_11 = QFrame(self.frame)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_11)

        self.rotate_left = CustomLabel(self.frame)
        self.rotate_left.setObjectName(u"rotate_left")
        self.rotate_left.setMinimumSize(QSize(30, 30))
        self.rotate_left.setMaximumSize(QSize(30, 30))
        self.rotate_left.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotate_left.setTextFormat(Qt.AutoText)
        self.rotate_left.setScaledContents(True)
        self.rotate_left.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.rotate_left)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.label_rotate = QLabel(self.frame)
        self.label_rotate.setObjectName(u"label_rotate")

        self.horizontalLayout_2.addWidget(self.label_rotate)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.rotate_rigth = CustomLabel(self.frame)
        self.rotate_rigth.setObjectName(u"rotate_rigth")
        self.rotate_rigth.setMinimumSize(QSize(30, 30))
        self.rotate_rigth.setMaximumSize(QSize(30, 30))
        self.rotate_rigth.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotate_rigth.setTextFormat(Qt.AutoText)
        self.rotate_rigth.setScaledContents(True)
        self.rotate_rigth.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.rotate_rigth)

        self.line_12 = QFrame(self.frame)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_12)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.zoom_out = CustomLabel(self.frame)
        self.zoom_out.setObjectName(u"zoom_out")
        self.zoom_out.setMinimumSize(QSize(30, 30))
        self.zoom_out.setMaximumSize(QSize(30, 30))
        self.zoom_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoom_out.setTextFormat(Qt.AutoText)
        self.zoom_out.setScaledContents(True)
        self.zoom_out.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.zoom_out)

        self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy3)
        self.horizontalSlider.setMinimumSize(QSize(135, 0))
        self.horizontalSlider.setMaximumSize(QSize(135, 16777215))
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setMinimum(12)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setSliderPosition(31)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.horizontalSlider)

        self.zoom_in = CustomLabel(self.frame)
        self.zoom_in.setObjectName(u"zoom_in")
        self.zoom_in.setMinimumSize(QSize(30, 30))
        self.zoom_in.setMaximumSize(QSize(30, 30))
        self.zoom_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.zoom_in.setTextFormat(Qt.AutoText)
        self.zoom_in.setScaledContents(True)
        self.zoom_in.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.zoom_in)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_8, 1, 3, 1, 1)

        self.scrollArea_2 = QScrollArea(self.frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(260, 0))
        self.scrollArea_2.setMaximumSize(QSize(260, 16777215))
        self.scrollArea_2.setStyleSheet(u"border-top: 0 px;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 258, 622))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.up_pg = CustomLabel(self.scrollAreaWidgetContents_2)
        self.up_pg.setObjectName(u"up_pg")
        self.up_pg.setMinimumSize(QSize(30, 30))
        self.up_pg.setMaximumSize(QSize(30, 30))
        self.up_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_pg.setTextFormat(Qt.AutoText)
        self.up_pg.setScaledContents(True)
        self.up_pg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.up_pg)

        self.down_pg = CustomLabel(self.scrollAreaWidgetContents_2)
        self.down_pg.setObjectName(u"down_pg")
        self.down_pg.setMinimumSize(QSize(30, 30))
        self.down_pg.setMaximumSize(QSize(30, 30))
        self.down_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.down_pg.setTextFormat(Qt.AutoText)
        self.down_pg.setScaledContents(True)
        self.down_pg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.down_pg)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_9.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.listWidget = CustomListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setMaximumSize(QSize(200, 16777215))
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.setStyleSheet(u"border: 0px; ")
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setIconSize(QSize(300, 200))
        self.listWidget.setTextElideMode(Qt.ElideMiddle)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setItemAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.listWidget, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 1, 3, 1)

        self.line_9 = QFrame(self.frame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_9, 0, 2, 1, 1)

        self.line_10 = QFrame(self.frame)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_10, 2, 2, 1, 1)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setMinimumSize(QSize(600, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 600))
        self.scrollArea.setStyleSheet(u"border: 0px;")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 948, 619))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy4)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.display = QLabel(self.scrollAreaWidgetContents)
        self.display.setObjectName(u"display")
        sizePolicy4.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy4)
        self.display.setMinimumSize(QSize(590, 590))
        self.display.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.display, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 2, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_6, 3, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalWidget = QWidget(self.frame)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"background-color: rgb(0, 142, 255);")
        self.gridLayout_7 = QGridLayout(self.verticalWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 5)
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 142, 255); font: 700 60pt \"Segoe UI Variable Display\";")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 3, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.verticalWidget, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.add_pg = CustomLabel(self.frame)
        self.add_pg.setObjectName(u"add_pg")
        self.add_pg.setMinimumSize(QSize(40, 40))
        self.add_pg.setMaximumSize(QSize(40, 40))
        self.add_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_pg.setTextFormat(Qt.AutoText)
        self.add_pg.setScaledContents(True)
        self.add_pg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.add_pg)

        self.delete_pg = CustomLabel(self.frame)
        self.delete_pg.setObjectName(u"delete_pg")
        self.delete_pg.setMinimumSize(QSize(40, 40))
        self.delete_pg.setMaximumSize(QSize(40, 40))
        self.delete_pg.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_pg.setTextFormat(Qt.AutoText)
        self.delete_pg.setScaledContents(True)
        self.delete_pg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.delete_pg)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.zip_file = CustomLabel(self.frame)
        self.zip_file.setObjectName(u"zip_file")
        self.zip_file.setMinimumSize(QSize(30, 30))
        self.zip_file.setMaximumSize(QSize(30, 30))
        self.zip_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.zip_file.setTextFormat(Qt.AutoText)
        self.zip_file.setScaledContents(True)
        self.zip_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.zip_file)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.to_divide_file = CustomLabel(self.frame)
        self.to_divide_file.setObjectName(u"to_divide_file")
        self.to_divide_file.setMinimumSize(QSize(30, 30))
        self.to_divide_file.setMaximumSize(QSize(30, 30))
        self.to_divide_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.to_divide_file.setTextFormat(Qt.AutoText)
        self.to_divide_file.setScaledContents(True)
        self.to_divide_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.to_divide_file)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.save_file = CustomLabel(self.frame)
        self.save_file.setObjectName(u"save_file")
        self.save_file.setMinimumSize(QSize(30, 30))
        self.save_file.setMaximumSize(QSize(30, 30))
        self.save_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_file.setTextFormat(Qt.AutoText)
        self.save_file.setScaledContents(True)
        self.save_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.save_file)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.close_file = CustomLabel(self.frame)
        self.close_file.setObjectName(u"close_file")
        self.close_file.setMinimumSize(QSize(30, 30))
        self.close_file.setMaximumSize(QSize(30, 30))
        self.close_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_file.setTextFormat(Qt.AutoText)
        self.close_file.setScaledContents(True)
        self.close_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.close_file)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 2, 0, 1, 2)


        self.verticalLayout_10.addLayout(self.gridLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.retranslateUi(Menu)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Menu", None))
        Menu.setWindowFilePath("")
        self.add_new_file.setText(QCoreApplication.translate("Menu", u"Adicionar Documentos", None))
        self.add_m_d_agua.setText(QCoreApplication.translate("Menu", u"Adicionar Marca D'\u00e1gua", None))
        self.add_n_pg.setText(QCoreApplication.translate("Menu", u"Adicionar N\u00ba de P\u00e1gina", None))
        self.delete_page_menu.setText(QCoreApplication.translate("Menu", u"Remover P\u00e1ginas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Menu", u"Editar", None))
        self.pdf_to_word.setText(QCoreApplication.translate("Menu", u"Converter para  Word", None))
        self.pdf_to_excel.setText(QCoreApplication.translate("Menu", u"Converter para  Excel", None))
        self.expo_Img_Button_png.setText(QCoreApplication.translate("Menu", u"Converter para PNG", None))
        self.expo_Img_Button_jpg.setText(QCoreApplication.translate("Menu", u"Converter para  JPEG", None))
        self.word_to_pdf.setText(QCoreApplication.translate("Menu", u"Converter para PDF", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Menu", u"Converter Arquivo", None))
        self.add_password.setText(QCoreApplication.translate("Menu", u"Proteger PDF", None))
        self.remove_password.setText(QCoreApplication.translate("Menu", u"Desbloquear PDF", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Menu", u"Seguran\u00e7a", None))
#if QT_CONFIG(tooltip)
        self.back_pg.setToolTip(QCoreApplication.translate("Menu", u"P\u00e1gina anterior", None))
#endif // QT_CONFIG(tooltip)
        self.back_pg.setText(QCoreApplication.translate("Menu", u"back_pg", None))
        self.n_pg_total.setText(QCoreApplication.translate("Menu", u"/ 0", None))
#if QT_CONFIG(tooltip)
        self.next_pg.setToolTip(QCoreApplication.translate("Menu", u"Pr\u00f3xima p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
        self.next_pg.setText(QCoreApplication.translate("Menu", u"next_pg", None))
#if QT_CONFIG(tooltip)
        self.rotate_left.setToolTip(QCoreApplication.translate("Menu", u"Girar 90\u00ba esquerda", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_left.setText(QCoreApplication.translate("Menu", u"rotate_left", None))
        self.label_rotate.setText(QCoreApplication.translate("Menu", u"Rotacionar", None))
#if QT_CONFIG(tooltip)
        self.rotate_rigth.setToolTip(QCoreApplication.translate("Menu", u"Girar 90\u00ba direita", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_rigth.setText(QCoreApplication.translate("Menu", u"rotate_rigth", None))
#if QT_CONFIG(tooltip)
        self.zoom_out.setToolTip(QCoreApplication.translate("Menu", u"Zoom -", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_out.setText(QCoreApplication.translate("Menu", u"zoom_out", None))
#if QT_CONFIG(tooltip)
        self.zoom_in.setToolTip(QCoreApplication.translate("Menu", u"Zoom +", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_in.setText(QCoreApplication.translate("Menu", u"zoom_in", None))
#if QT_CONFIG(tooltip)
        self.up_pg.setToolTip(QCoreApplication.translate("Menu", u"Movar para cima", None))
#endif // QT_CONFIG(tooltip)
        self.up_pg.setText(QCoreApplication.translate("Menu", u"up_pg", None))
#if QT_CONFIG(tooltip)
        self.down_pg.setToolTip(QCoreApplication.translate("Menu", u"Mover para baixo", None))
#endif // QT_CONFIG(tooltip)
        self.down_pg.setText(QCoreApplication.translate("Menu", u"down_pg", None))
        self.display.setText("")
        self.label.setText(QCoreApplication.translate("Menu", u"PDF_Export", None))
#if QT_CONFIG(tooltip)
        self.add_pg.setToolTip(QCoreApplication.translate("Menu", u"Adicionar arquivo", None))
#endif // QT_CONFIG(tooltip)
        self.add_pg.setText(QCoreApplication.translate("Menu", u"add_pg", None))
#if QT_CONFIG(tooltip)
        self.delete_pg.setToolTip(QCoreApplication.translate("Menu", u"Deletar p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
        self.delete_pg.setText(QCoreApplication.translate("Menu", u"delete_pg", None))
#if QT_CONFIG(tooltip)
        self.zip_file.setToolTip(QCoreApplication.translate("Menu", u"Compactar", None))
#endif // QT_CONFIG(tooltip)
        self.zip_file.setText(QCoreApplication.translate("Menu", u"zip_file", None))
#if QT_CONFIG(tooltip)
        self.to_divide_file.setToolTip(QCoreApplication.translate("Menu", u"Dividir documento", None))
#endif // QT_CONFIG(tooltip)
        self.to_divide_file.setText(QCoreApplication.translate("Menu", u"to_divide_file", None))
#if QT_CONFIG(tooltip)
        self.save_file.setToolTip(QCoreApplication.translate("Menu", u"Salvar", None))
#endif // QT_CONFIG(tooltip)
        self.save_file.setText(QCoreApplication.translate("Menu", u"save_file", None))
#if QT_CONFIG(tooltip)
        self.close_file.setToolTip(QCoreApplication.translate("Menu", u"Fechar documento", None))
#endif // QT_CONFIG(tooltip)
        self.close_file.setText(QCoreApplication.translate("Menu", u"close_file", None))
    # retranslateUi

