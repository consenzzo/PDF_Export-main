from menu2_ui import Ui_Menu
from dict_function import dict_function
from message import show_error_lacks_value
from PySide6.QtWidgets import QCommandLinkButton, QToolBox, QLineEdit
from dialog import search_file
import sys

def validate_option(main_widget: Ui_Menu):
    sender_button = main_widget.sender()
    name = sender_button.objectName()
    list_validate = dict_function[name]['validate']
    for item in list_validate:
        func = getattr(sys.modules[__name__], item)
        result, msg, style_sheet, *args = func(main_widget, name)
        if result:
            return result
        else:
            return show_error_lacks_value(main_widget , msg , style_sheet, *args)
    




def toolBox_one_checked_item(main_widget: Ui_Menu, *args):
    button_names = [
        widget.objectName() for widget in main_widget.toolBox.findChildren(QCommandLinkButton)
    ]
    checked_count = 0
    for button_name in button_names:
        button = main_widget.findChild(QCommandLinkButton, button_name)
        if button.isChecked():
            checked_count += 1
            search_dialog = dict_function[button_name]['search_dialog']
        else:
            ...
    if checked_count >= 1:
        search_file(main_widget, search_dialog)
        return True, None , None
    else:
        style_sheet = main_widget.toolBox.styleSheet()
        main_widget.toolBox.setStyleSheet(style_sheet + 'border: 2px solid red;')
        return False, 'Escolha uma opção no menu para buscar o arquivo desejado', style_sheet, 'toolBox'


def replace_lineEdit(main_widget: Ui_Menu, name):
    if main_widget.page.isVisible():
        main_widget.page_n_pages.setVisible(True)
    if main_widget.page_2.isVisible():
        main_widget.page_n_pages.setVisible(False)
    main_widget.lineEdit.setPlaceholderText(dict_function[name]['lineEdit'])
    return True, None, None


def validate_confirm_Button(main_widget: Ui_Menu, *args):
    if main_widget.page_n_pages.isVisible():
        if not main_widget.de_ate_radioButton.isChecked() and not main_widget.pages_radioButton.isChecked():
            style_sheet = main_widget.de_ate_radioButton.styleSheet()
            main_widget.de_ate_radioButton.setStyleSheet(style_sheet + 'border: 2px solid red;')
            main_widget.pages_radioButton.setStyleSheet(style_sheet + 'border: 2px solid red;')
            return False, 'Escolha uma opção de página', style_sheet, 'de_ate_radioButton', 'pages_radioButton'
        if main_widget.de_ate_radioButton.isChecked():
            if main_widget.de_Edit.text()=='' or main_widget.de_Edit.text()=='0' or main_widget.ate_Edit.text() == '' or main_widget.ate_Edit.text() == '0':
                style_sheet = main_widget.de_Edit.styleSheet()
                main_widget.de_Edit.setStyleSheet(style_sheet + 'border: 2px solid red;')
                main_widget.ate_Edit.setStyleSheet(style_sheet + 'border: 2px solid red;')
                return False, 'Informe as páginas', style_sheet, 'de_Edit', 'ate_Edit'
            else:
                return 10, None , None
        if main_widget.pages_radioButton.isChecked():
            if main_widget.pages_Edit.text() != '':
                input_str = str(main_widget.pages_Edit.text())  # Sua string de input
                valores = input_str.split("-")
                valores = [valor.strip() for valor in valores]
                if '0' in valores:
                    style_sheet = main_widget.pages_Edit.styleSheet()
                    main_widget.pages_Edit.setStyleSheet(style_sheet + 'border: 2px solid red;')
                    return False, 'Erro ao informar o número da página 0', style_sheet, 'pages_Edit'
            if main_widget.pages_Edit.text()=='':
                style_sheet = main_widget.pages_Edit.styleSheet()
                main_widget.pages_Edit.setStyleSheet(style_sheet + 'border: 2px solid red;')
                return False, 'Informe as páginas', style_sheet, 'pages_Edit'
            else:
                return 10, None , None
    else :
        return 10, None , None


def validate_select_file(main_widget: Ui_Menu, *args):
    if main_widget.lineEdit.text() == '':
        
        style_sheet = main_widget.lineEdit.styleSheet()
        main_widget.lineEdit.setStyleSheet(style_sheet + 'border: 2px solid red;')
        return False , 'Nenhum arquivo selecionado', style_sheet, 'lineEdit'
    else:
        return True, None , None