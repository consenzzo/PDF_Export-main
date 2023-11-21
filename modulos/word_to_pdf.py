from docx2pdf import convert
import os
from menu2_ui import Ui_Menu
from message import show_success_message

def word_to_pdf(main_widget: Ui_Menu, word_file , local_save_pg):
    pdf_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}.pdf")
    print(pdf_file)
    convert(word_file , pdf_file)
    

    show_success_message(main_widget)