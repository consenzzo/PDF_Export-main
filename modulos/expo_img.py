from menu2_ui import Ui_Menu
import os
import fitz
from pages import page_print
from verification import n_page_max
from message import show_success_message

# def expo_Img_Button(main_widget: Ui_Menu):
#     print('fUNCIONOU')


def expo_Img_Button(main_widget: Ui_Menu, pdf_file, local_save_img):

    pages = page_print(main_widget)
    
    maior = max(pages)
    pdf_document = n_page_max(pdf_file,maior)        

    for n_page in pages:
        page = pdf_document.load_page(n_page - 1)

        # Ajuste a resolução (dpi) da imagem exportada para 600 DPI
        image = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))

        # Nome do arquivo de imagem de saída (usando o mesmo diretório e nome do arquivo selecionado)
        output_image = os.path.join(os.path.dirname(local_save_img), f"{os.path.splitext(os.path.basename(local_save_img))[0]}_page_{n_page}.png")

        # Salve a imagem no mesmo local selecionado
        image.save(output_image, "png")

        print(f"Página {n_page} exportada como '{output_image}'")
    show_success_message(main_widget)