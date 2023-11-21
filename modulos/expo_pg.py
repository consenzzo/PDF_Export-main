import fitz
import os
from PySide6.QtWidgets import QInputDialog
from dict_function import list_expo_pg_Button, dict_function
from pages import page_print
from verification import n_page_max
from message import show_success_message
from menu2_ui import Ui_Menu

def expo_pg_Button(main_widget: Ui_Menu, pdf_file , local_save_pg):
    items = dict_function['expo_pg_Button']['items']
    item, ok = QInputDialog.getItem(main_widget, "PDF_Export",
                                "As páginas devem ser em: ", list(items.keys()), 0, False)
    # print(list_expo_pg_Button)
    if ok and item:
        escolha = items.get(item)
        # print(escolha)
        if escolha == 'separado':
            separado(main_widget, pdf_file , local_save_pg)
        elif escolha == 'unico':
            unico(main_widget, pdf_file , local_save_pg)
        else:
                print("Escolha inválida")



def separado(main_widget: Ui_Menu, pdf_file , local_save_pg):
    
    pages = page_print(main_widget)
    maior = max(pages)
    pdf_document = n_page_max(pdf_file , maior)
    


    for n_page in pages:
        # Abra o arquivo PDF de entrada
        pdf_document = fitz.open(pdf_file)

        # Crie um novo documento PDF de saída
        output_pdf = fitz.open()

        # Adicione a página desejada ao novo documento
        output_pdf.insert_pdf(pdf_document, from_page=n_page-1, to_page=n_page-1)

        # Salve o novo documento PDF
        output_pdf_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}_page_{n_page}.pdf")
        output_pdf.save(output_pdf_file)

        # Feche ambos os documentos
        pdf_document.close()
        output_pdf.close()

        print(f"Página {n_page} exportada como '{os.path.splitext(os.path.basename(local_save_pg))[0]}_page_{n_page}.pdf'")
    show_success_message(main_widget)



def unico(main_widget: Ui_Menu, pdf_file , local_save_pg):
    
    pages = page_print(main_widget)
    maior = max(pages)
    pdf_document = n_page_max(pdf_file , maior)
    
    # Abra o arquivo PDF de entrada
    pdf_document = fitz.open(pdf_file)
    # Crie um novo documento PDF de saída
    output_pdf = fitz.open()
    rename = str('')

    for n_page in pages:
        
        # Adicione a página desejada ao novo documento
        output_pdf.insert_pdf(pdf_document, from_page=n_page-1, to_page=n_page-1)
        rename += f"_{n_page}"

    # Salve o novo documento PDF
    output_pdf_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}_page_{rename}.pdf")
    output_pdf.save(output_pdf_file)
    # Feche ambos os documentos
    pdf_document.close()
    output_pdf.close()
    print(f"Página {rename} exportada como '{os.path.splitext(os.path.basename(local_save_pg))[0]}_page_{rename}.pdf'")
    show_success_message(main_widget)