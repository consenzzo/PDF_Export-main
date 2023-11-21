from pdf2docx import Converter
import os
from menu2_ui import Ui_Menu
from message import show_success_message

def pdf_to_word(main_widget: Ui_Menu, pdf_file , local_save_pg):
    cv = Converter(pdf_file)
    docx_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}.docx")
    print(docx_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

    show_success_message(main_widget)