from menu2_ui import Ui_Menu
from dict_validate import dict_validate
import check
import zipfile
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
import fitz  # PyMuPDF
import os
import tempfile
from dialog import image2pdf, excel_to_pdf, word_to_pdf
import io
from PIL import Image

def zip_file(self: Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check, name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function:
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar ZIP", "", "ZIP Files (*.zip)")
        if save_path:

            new_pdf = fitz.open()  # Criar um novo documento PDF

            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))

            for page_number, page_data in sorted_pages:
                original_file_path = page_data["local"]  # Caminho do arquivo original
                original_page_number = int(page_data["n_pag_original"])  # Número da página original
                position = page_data["guidance"]

                if os.path.exists(original_file_path):
                    # Se não for um PDF, verificar outras extensões
                    pdf_document = None
                    for ext in [".pdf", ".png", ".jpeg", "*.jpg", ".xlsx", ".xls", ".docx", ".doc"]:
                        alternative_path = os.path.splitext(original_file_path)[0] + ext
                        if os.path.exists(alternative_path):

                            if ext in (".pdf"):
                                pdf_document = fitz.open(original_file_path)
                                continue

                            elif ext in (".png", ".jpeg", "*.jpg"):
                                img = Image.open(original_file_path)
                                pdf_document = fitz.open()
                                temp_pdf_paths = image2pdf(img)
                                pdf_document.insert_pdf(fitz.open(temp_pdf_paths))
                                os.remove(temp_pdf_paths)
                                continue

                            elif ext in (".xlsx", ".xls"):
                                temp_pdf_paths = excel_to_pdf(alternative_path)
                                pdf_document = fitz.open(temp_pdf_paths)
                                continue

                            elif ext in (".docx", ".doc"):
                                temp_pdf_paths = word_to_pdf(alternative_path)
                                pdf_document = fitz.open(temp_pdf_paths)
                                continue

                else:
                    # Obter bytes da imagem do dicionário
                    img_bytes = page_data["icon_bytes"]
                    img = Image.open(io.BytesIO(img_bytes))
                    pdf_document = fitz.open()
                    temp_pdf_paths = image2pdf(img)
                    pdf_document.insert_pdf(fitz.open(temp_pdf_paths))
                    os.remove(temp_pdf_paths)

                # Obter a página desejada do documento original
                page = pdf_document.load_page(original_page_number)  # Subtrai 1 porque os índices começam em 0

                if position != 0:
                    # Rotacionar a página
                    page.set_rotation(position)

                # Copiar a página original para o novo documento
                new_pdf.insert_pdf(pdf_document, from_page=original_page_number, to_page=original_page_number)

                pdf_document.close()
                try:
                    os.remove(temp_pdf_paths)
                except:
                    pass

            # Salvar o arquivo ZIP diretamente com o PDF
            with zipfile.ZipFile(save_path, 'w') as zipf:
                zipf.writestr(os.path.basename(save_path.replace(".zip", ".pdf")), new_pdf.write())

            new_pdf.close()



            QMessageBox.information(self, "Sucesso", "Arquivo compactado com sucesso!")


