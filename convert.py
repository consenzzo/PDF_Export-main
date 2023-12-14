from menu2_ui import Ui_Menu
import os
from pathlib import Path
import xlwings as xw
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from docx2pdf import convert
import base64
from PIL import Image
from reportlab.pdfgen import canvas
import fitz  # PyMuPDF
from pdf2docx import Converter

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

        # code_base64 = pdf_to_base64(output_path)

        for pdf in pdf_paths:
            os.remove(pdf)
        # os.remove(output_path)

    return output_path


    
def word_to_pdf(self: Ui_Menu , file_path):
    pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
    convert(file_path , pdf_file)
    # code_base64 = pdf_to_base64(pdf_file)
    # os.remove(pdf_file)
    return pdf_file


def pdf_to_base64(pdf_path, page_number):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        page = pdf_reader.pages[page_number]

        # Converte a página em um novo arquivo PDF temporário
        temp_pdf_path = os.path.join(os.path.dirname(pdf_path), f"{os.path.splitext(os.path.basename(pdf_path))[0]}temp_file_pdf_export.pdf")
        temp_pdf_writer = PdfWriter()
        temp_pdf_writer.add_page(page)

        with open(temp_pdf_path, 'wb') as temp_pdf_file:
            temp_pdf_writer.write(temp_pdf_file)

        # Lê os bytes do novo arquivo PDF temporário
        with open(temp_pdf_path, 'rb') as temp_pdf_file:
            pdf_bytes = temp_pdf_file.read()

        # Codifica os bytes para base64
        base64_page = base64.b64encode(pdf_bytes)
        os.remove(temp_pdf_path)
        return base64_page



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
        

def img_to_pdf(self: Ui_Menu, file_path):
    imagem = Image.open(file_path)
    pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
    largura, altura = imagem.size

    # Criação de um objeto PDF
    pdf = canvas.Canvas(pdf_file, pagesize=(largura, altura))


    # Adiciona a imagem ao PDF
    pdf.drawInlineImage(file_path, 0, 0, largura, altura)

    # Salva o PDF
    pdf.save()
    
    # code_base64 = pdf_to_base64(pdf_file)
    # os.remove(pdf_file)
    return pdf_file



def scale_image(self: Ui_Menu, file_path, max_width, max_height):
    try:
        # Defina o tamanho máximo em pixels para uma página A4 (210mm x 297mm a 300 DPI)
        img = Image.open(file_path)
        width, height = img.size

        # Verifique se a imagem precisa ser redimensionada
        if width > max_width or height > max_height:
            # Calcule a nova escala mantendo a proporção
            scale = min(max_width / width, max_height / height)
            new_width = int(width * scale)
            new_height = int(height * scale)

            # Redimensione a imagem
            # img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img = img.resize((new_width, new_height), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else 3)
            name_img = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}_SCALE_.png")
            # Salve a nova imagem redimensionada
            # scaled_path = f"{file_path}_scaled_"
            scaled_path = name_img
            img.save(scaled_path)

            return scaled_path
        else:
            return False
    except Exception as e:
        print(f"Error scaling image: {e}")
        return None
    


def pdf_to_word(self: Ui_Menu, pdf_file , local_save_pg):
    cv = Converter(pdf_file)
    docx_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}.docx")
    print(docx_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()