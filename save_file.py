from menu2_ui import Ui_Menu
from PySide6.QtWidgets import  QFileDialog, QDialog
import fitz
from convert import base64_to_pdf
import os

def save_file_pdf(self:Ui_Menu):
    save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
    if save_path:
        
        # Ordenar o dicionário com base no número da página da aplicação
        sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))

        doc_saida = fitz.open()
        for page_number, page_data in sorted_pages:
            base64_to_file = base64_to_pdf(page_data["base64_pdf"],'temp_pdf_export_base64_to_pdf.pdf')
            doc_entrada = fitz.open()
        
                
            doc_saida.insert_pdf(fitz.open(base64_to_file))

            doc_entrada.close()
            os.remove(base64_to_file)

        doc_saida.save(save_path)
        doc_saida.close()
