import fitz
import os
from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QPushButton
from message import show_error_lacks_value


def n_page_max(pdf_file , max_page):
    #Verifique se o arquivo PDF existe
        if os.path.exists(pdf_file):
            # Abra o arquivo PDF
            pdf_document = fitz.open(pdf_file)
            n_total = len(pdf_document)

            # Verifique se o número da página é válido
            if  max_page <= n_total:
                # print(len(pdf_document))
                # print(max_page)
                return pdf_document
            else:
                
                raise ValueError("O número da página é maior do que o número total de páginas no PDF")
            

# def go_to_confirm(main_widget: Ui_Menu):
#     options =  is_any_button_checked(main_widget.gridGroupBox_5)
#     pages = go_to_page_print(main_widget)
#     file = go_to_line_edit(main_widget)
#     list_conference = [options,pages,file]
#     if False in list_conference:
#         show_error_lacks_value(main_widget)
#         return False
#     else:
#         ...

     
# Função para verificar se algum botão do grupo está marcado
# def is_any_button_checked(gridGroupBox):
#     # Percorre todos os widgets dentro do grupo
#     for widget in gridGroupBox.findChildren(QPushButton):
#         # Verifica se o botão de rádio está marcado
#         if widget.isChecked():
#             return True  # Pelo menos um botão está marcado
#     return False  # Nenhum botão está marcado

# # Função para verificar se algum botão do grupo está marcado
# def go_to_page_print(main_widget: Ui_Menu):
#     if main_widget.de_ate_radioButton.isChecked():
#         if int(main_widget.de_Edit.text()) > 0 and int(main_widget.ate_Edit.text()) > 0:
#             return True
#         else:
#             return False
#     elif main_widget.pages_radioButton.isChecked():
#         if main_widget.pages_Edit.text() != '':
#             input_str = str(main_widget.pages_Edit.text())  # Sua string de input
#             valores = input_str.split("-")
#             valores = [valor.strip() for valor in valores]
#             if '0' in valores:
#                 main_widget.pages_Edit.setText('')
#                 return False
#             return True
#         else:
#             return False
#     else:
#         return False

# def go_to_line_edit(main_widget: Ui_Menu):
#     if main_widget.lineEdit.text() != '':
#         return True
#     else:
#         return False
