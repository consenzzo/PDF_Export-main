from PySide6.QtWidgets import  QMessageBox, QToolBox, QCommandLinkButton
from menu2_ui import Ui_Menu

def pages_not_selected(self: Ui_Menu):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Nenhuma página selecionada!")
    msg.setWindowTitle("Aviso")
    msg.exec()
    return False


def not_page_file(self: Ui_Menu):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Documento não existente")
    msg.setWindowTitle("Aviso")
    msg.exec()
    return False