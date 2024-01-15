from menu2_ui import Ui_Menu
from PySide6.QtWidgets import  QFileDialog, QDialog, QMessageBox, QApplication
import fitz
from convert import base64_to_pdf, pdf_to_word, pdf_to_excel, pdf_to_png, pdf_to_jpg
import os
from PIL import Image
import zipfile
from add_file import add_pages


def save_file_pdf(self:Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
        if save_path:
            
            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))

            doc_saida = fitz.open()
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()
            
                    
                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            doc_saida.save(save_path)
            doc_saida.close()
            self.wait_text.setText('')

def save_file_word(self:Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Word", "", "Word Files (*.docx)")
        if save_path:
            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            doc_saida = fitz.open()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()
            
                    
                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            doc_saida.save('temp_pdf_export_to_word.pdf')
            doc_saida.close()

            pdf_to_word(self,'temp_pdf_export_to_word.pdf',save_path)
            os.remove('temp_pdf_export_to_word.pdf')
            self.wait_text.setText('')


def save_file_excel(self:Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Excel", "", "Excel Files (*.xlsx)")
        if save_path:
            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            doc_saida = fitz.open()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()
            
                    
                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            doc_saida.save('temp_pdf_export_to_excel.pdf')
            doc_saida.close()
            pdf_to_excel(self,'temp_pdf_export_to_excel.pdf',save_path)
            os.remove('temp_pdf_export_to_excel.pdf')
            self.wait_text.setText('')

def save_file_png(self:Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Imagem", "", "Image Files (*.png)")
        if save_path:
            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            doc_saida = fitz.open()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()
            
                    
                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            doc_saida.save('temp_pdf_export_to_excel.pdf')
            doc_saida.close()
            pdf_to_png(self,'temp_pdf_export_to_excel.pdf',save_path)
            os.remove('temp_pdf_export_to_excel.pdf')
            self.wait_text.setText('')

def save_file_jpg(self:Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo Imagem", "", "Image Files (*.jpeg)")
        if save_path:
            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            doc_saida = fitz.open()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()
            
                    
                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            doc_saida.save('temp_pdf_export_to_excel.pdf')
            doc_saida.close()
            pdf_to_jpg(self,'temp_pdf_export_to_excel.pdf',save_path)
            os.remove('temp_pdf_export_to_excel.pdf')
            self.wait_text.setText('')


def zip_file(self: Ui_Menu):
    if not self.listWidget.count():
        file_paths = add_pages(self)
    if self.listWidget.count():
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar ZIP", "", "ZIP Files (*.zip)")
        if save_path:
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))
            self.wait_text.setText('Aguarde')
            QApplication.processEvents()
            doc_saida = fitz.open()
            for page_number, page_data in sorted_pages:
                base64_to_file = base64_to_pdf(page_data["base64_pdf"], 'temp_pdf_export_base64_to_pdf.pdf')
                doc_entrada = fitz.open()

                doc_saida.insert_pdf(fitz.open(base64_to_file))

                doc_entrada.close()
                os.remove(base64_to_file)

            temp_pdf_path = 'temp_pdf_zip_export_pdf.pdf'
            doc_saida.save(temp_pdf_path)
            doc_saida.close()  # Agora, fechamos o documento após salvá-lo

            # Salvar o arquivo ZIP diretamente com o PDF
            with zipfile.ZipFile(save_path, 'w') as zipf:
                zipf.write(temp_pdf_path, os.path.basename(temp_pdf_path))

            os.remove(temp_pdf_path)
            self.wait_text.setText('')
            QMessageBox.information(self, "Sucesso", "Arquivo compactado com sucesso!")