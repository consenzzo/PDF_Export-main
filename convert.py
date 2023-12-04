from menu2_ui import Ui_Menu
import os
from pathlib import Path
import xlwings as xw
from PyPDF2 import PdfMerger
from docx2pdf import convert
import base64

def excel_to_pdf(self: Ui_Menu, file_path):
    with xw.App() as app:
        app.visible = False
        book = app.books.open(file_path)
        pdf_paths = []  # Lista para armazenar os caminhos dos arquivos PDF
        output_path = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}_sheet.pdf")
        for sheet_index, sheet in enumerate(book.sheets):
            # Construir o caminho para o arquivo PDF
            pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}_sheet{sheet_index}.pdf")
            pdf_path = Path(pdf_file)

            # Salvar a planilha atual como um arquivo PDF
            sheet.to_pdf(path=pdf_path, show=False)

            # Adicionar o caminho do arquivo PDF à lista
            pdf_paths.append(pdf_path)

        merger = PdfMerger()

        for pdf in pdf_paths:
            merger.append(pdf)


        merger.write(output_path)
        merger.close()

        code_base64 = pdf_to_base64(output_path)

        for pdf in pdf_paths:
            os.remove(pdf)
        os.remove(output_path)

    return code_base64


    
def word_to_pdf(self: Ui_Menu , file_path):
    pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
    convert(file_path , pdf_file)
    code_base64 = pdf_to_base64(pdf_file)
    os.remove(pdf_file)
    return code_base64


def pdf_to_base64(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        # Lê os bytes do arquivo PDF
        pdf_bytes = pdf_file.read()
        
        # Codifica os bytes para base64
        codigo_base64 = base64.b64encode(pdf_bytes)
        
    return codigo_base64


def base64_to_pdf(codigo_path, file_path):
    # with open(codigo_path, 'rb') as codigo_file:
    #     # Lê o código base64 do arquivo
    codigo_base64 = codigo_path
    local_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}temp_new_file.pdf")
    
    # Decodifica o código base64 para bytes
    pdf_bytes = base64.b64decode(codigo_base64)
    
    # Cria um novo arquivo PDF
    with open(local_file, 'wb') as new_pdf_file:
        new_pdf_file.write(pdf_bytes)
    
    return local_file
        