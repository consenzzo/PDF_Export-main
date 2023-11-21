from PySide6.QtWidgets import  QMessageBox, QToolBox, QCommandLinkButton
from menu2_ui import Ui_Menu
from dict_function import dict_function

def show_error_lacks_value(main_widget: Ui_Menu, msg , style_sheet, *args):
    # Crie uma caixa de mensagem de erro
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setWindowTitle("Erro : Escolha incompleta")
    error_box.setText(msg)
    error_box.setStandardButtons(QMessageBox.Ok)
    error_box.exec_()
    original(main_widget, style_sheet, *args)

    return False
    
    


# Função para exibir uma mensagem de sucesso
def show_success_message(main_widget: Ui_Menu):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Operação concluída com êxito!")
    msg.setWindowTitle("Sucesso")
    initialize(main_widget)
    msg.exec()


def original(main_widget: Ui_Menu, style_sheet, *args):
    for arg in args:
        element = getattr(main_widget,arg)
        element.setStyleSheet(style_sheet)



def initialize(main_widget: Ui_Menu):
    main_widget.buttons_dict = None
    main_widget.nome_funcao = None
    main_widget.lineEdit.setText('')
    main_widget.lineEdit.setPlaceholderText('Aguardando arquivo')
    button_names = []
    menu = main_widget.findChild(QToolBox, 'toolBox')
    button_names = [
        widget.objectName() for widget in menu.findChildren(QCommandLinkButton)
    ]
    for button_name in button_names:
        main_widget.findChild(QCommandLinkButton, button_name).setChecked(False)
    main_widget.de_Edit.setText('')
    main_widget.ate_Edit.setText('')
    main_widget.pages_Edit.setText('')
