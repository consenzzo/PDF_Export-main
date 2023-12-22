from menu2_ui import Ui_Menu
from dialog import search_pdf_password_file
import PyPDF2
from PySide6 import QtWidgets
from PySide6.QtWidgets import  QFileDialog, QMessageBox

def remove_password(self:Ui_Menu):
    pdf_file = search_pdf_password_file(self)
    with open(pdf_file, 'rb') as arquivo_entrada:
        leitor = PyPDF2.PdfReader(arquivo_entrada)
        # Verifica se o PDF está protegido por senha
        if leitor.is_encrypted:
            while True:
                senha, ok_pressed = QtWidgets.QInputDialog.getText(self, 'Senha', 'Digite a senha do PDF:', QtWidgets.QLineEdit.Password)
                if not ok_pressed:
                    print('Operação cancelada pelo usuário.')
                    return
                if leitor.decrypt(senha):
                    save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
                    if save_path:
                        escritor = PyPDF2.PdfWriter()
                        # Adiciona todas as páginas ao novo arquivo
                        for num_pagina in range(len(leitor.pages)):
                            pagina = leitor.pages[num_pagina]
                            escritor.add_page(pagina)

                        # Salva o novo arquivo desbloqueado
                        with open(save_path, 'wb') as arquivo_saida:
                            escritor.write(arquivo_saida)
                        return
        else:
            QMessageBox.information(self, 'Informação', 'O PDF não está protegido por senha.')
            return

def password_pdf(self:Ui_Menu):
    pdf_file = search_pdf_password_file(self)
    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        if pdf_reader.is_encrypted:
            QMessageBox.information(self, 'Informação', 'O PDF já está protegido por senha.')
        else:
            save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
            if save_path:
                senha, ok_pressed = QtWidgets.QInputDialog.getText(self, 'Senha', 'Informe a senha desejada:', QtWidgets.QLineEdit.Password)
                if not ok_pressed:
                    print('Operação cancelada pelo usuário.')
                    return
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

                pdf_writer.encrypt(senha)

                with open(save_path, 'wb') as encrypted_pdf:
                    pdf_writer.write(encrypted_pdf)
                return QMessageBox.information(self, 'Informação', f'O PDF foi protegido com sucesso com a senha: {senha}')