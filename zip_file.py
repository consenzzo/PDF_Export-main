from menu2_ui import Ui_Menu
from dict_validate import dict_validate
import check
import zipfile
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
import fitz  # PyMuPDF
import os
import tempfile


def zip_file(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check, name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function:
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar ZIP", "", "ZIP Files (*.zip)")
        if save_path:
            # Criar um arquivo temporário para salvar o PDF
            temp_pdf_path = tempfile.NamedTemporaryFile(delete=False, prefix=os.path.splitext(save_path)[0] , suffix=".pdf").name
            new_pdf = fitz.open()  # Criar um novo documento PDF

            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))

            for page_number, page_data in sorted_pages:
                original_file_path = page_data["local"]  # Caminho do arquivo original
                original_page_number = int(page_data["n_pag_original"])  # Número da página original
                position = page_data["guidance"]

                pdf_document = fitz.open(original_file_path)
                
                # Obter a página desejada do documento original
                page = pdf_document.load_page(original_page_number )  # Subtrai 1 porque os índices começam em 0
                
                if position != 0:
                    # Rotacionar a página
                    page.set_rotation(position)

                # Copiar a página original para o novo documento
                new_pdf.insert_pdf(pdf_document, from_page=original_page_number, to_page=original_page_number)

                pdf_document.close()

            # Salvar o PDF temporário
            new_pdf.save(temp_pdf_path)
            new_pdf.close()

            # Adicionar o PDF temporário ao arquivo zip
            with zipfile.ZipFile(save_path, 'w') as zipf:
                zipf.write(temp_pdf_path, arcname=os.path.basename(temp_pdf_path))

            # Remover o PDF temporário após adicioná-lo ao zip
            os.remove(temp_pdf_path)

            QMessageBox.information(self, "Sucesso", "Arquivo compactado com sucesso!")


