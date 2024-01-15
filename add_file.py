from menu2_ui import Ui_Menu
from dialog import search_file
from convert import excel_to_pdf, word_to_pdf, scale_image, img_to_pdf, pdf_to_base64
from display import render_img_byte
import fitz  # PyMuPDF
import os
import PyPDF2
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication


def add_pages(self:Ui_Menu):
    file_paths = search_file(self)
    self.wait_text.setText('Aguarde')
    QApplication.processEvents()
    for file_path in file_paths:
        original_file_path = file_path

        if file_path.lower().endswith(('.xlsx', '.xls')):
            pdf =  excel_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)
            
        elif file_path.lower().endswith(('.docx' , '.doc')):
            pdf =  word_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)

        elif file_path.lower().endswith(('.png', '.jpeg', '.jpg')):
            scaled_path = scale_image(self, file_path, 2480, 3508)
            if scaled_path:
                file_path = scaled_path
            pdf =  img_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)
            if scaled_path:
                os.remove(scaled_path)
        else:
            pdf =  file_path
            pdf_password = False
            with open(file_path, 'rb') as arquivo_entrada:
                leitor = PyPDF2.PdfReader(arquivo_entrada)
                if leitor.is_encrypted:
                    while pdf_password == False:
                        senha, ok_pressed = QtWidgets.QInputDialog.getText(self, 'Senha', 'Digite a senha do PDF:', QtWidgets.QLineEdit.Password)
                        if ok_pressed:
                            if leitor.decrypt(senha):
                                escritor = PyPDF2.PdfWriter()
                                # Adiciona todas as páginas ao novo arquivo
                                for num_pagina in range(len(leitor.pages)):
                                    pagina = leitor.pages[num_pagina]
                                    escritor.add_page(pagina)

                                # Salva o novo arquivo desbloqueado
                                with open('temp_pdf_export_password_copy_safe.pdf', 'wb') as arquivo_saida:
                                    escritor.write(arquivo_saida)
                                pdf = 'temp_pdf_export_password_copy_safe.pdf'
                                add_page_dict(self,pdf)
                                os.remove('temp_pdf_export_password_copy_safe.pdf')
                                pdf_password = True
                        else:
                            pdf_password = True
                else:
                    add_page_dict(self,pdf)



    total_page = len(self.icon_dict)
    self.n_pg_total.setText(f'/ {total_page}')
    self.wait_text.setText('')

                
def add_page_dict(self:Ui_Menu, pdf):
    pdf_document = fitz.open(pdf)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        img_bytes = page.get_pixmap()
        img_bytes = img_bytes.tobytes()
        base_64 = pdf_to_base64(pdf, page_num)


        
        item_data = {
            "atual": str(len(self.icon_dict) + 1),
            "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
            # "local":original_file_path,
            "base64_pdf": base_64,
            # "n_pag_original":page_num,
            "rotate": 0,
            # "local_watermark":None,
            "watermark_base64_pdf":None,
            # "watermark_transparence":None,
            
        }
        if self.icon_dict:
            max_id = max(self.icon_dict)
            
        else:
            max_id = 0
            
        self.icon_dict[max_id + 1] = item_data

        pixmap_list = render_img_byte(self,img_bytes)
        self.listWidget.addItem(pixmap_list)
                        

    pdf_document.close()