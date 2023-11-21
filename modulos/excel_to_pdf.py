from menu2_ui import Ui_Menu
from message import show_success_message
import xlwings as xw
from pathlib import Path
import os
def excel_to_pdf(main_widget: Ui_Menu, excel_file, local_save_pg):

    
    with xw.App() as app:
        # user will not even see the excel opening up
        app.visible = False
        book = app.books.open(excel_file)
        sheet = book.sheets[0]
        # sheet.page_setup.print_area = '$A$1:$Q$66'
        

        # Construct path for pdf file
        current_work_dir = os.getcwd()
        pdf_file = os.path.join(os.path.dirname(local_save_pg), f"{os.path.splitext(os.path.basename(local_save_pg))[0]}.pdf")
        # pdf_file_name = "pdf_workbook_printout.pdf"
        pdf_path = Path(pdf_file)

        # Save excel workbook as pdf and showing it
        sheet.to_pdf(path=pdf_path, show=False)

        show_success_message(main_widget)