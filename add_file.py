from menu2_ui import Ui_Menu
from dialog import search_file
from convert import excel_to_pdf, word_to_pdf, base64_to_pdf
from display import render_img_byte
import fitz  # PyMuPDF
import os

def add_pages(self:Ui_Menu):
    file_paths = search_file(self)

    for file_path in file_paths:
        original_file_path = file_path

        if file_path.lower().endswith(('.xlsx', '.xls')):
            base_64 =  excel_to_pdf(self, file_path)
            
        elif file_path.lower().endswith(('.docx' , '.doc')):
            base_64 =  word_to_pdf(self, file_path)

        # else:
        #     file_path = [original_file_path]

        pdf = base64_to_pdf(base_64, file_path)

        # for file_path_dir in file_path:

        pdf_document = fitz.open(pdf)

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            img_bytes = page.get_pixmap()
            img_bytes = img_bytes.tobytes()
            
            item_data = {
                "atual": str(len(self.icon_dict) + 1),
                "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
                # "local":original_file_path,
                "base64_pdf": base_64,
                "n_pag_original":page_num,
                "rotate": 0,
                "local_watermark":None,
                "watermark_bytes":None,
                "watermark_transparence":None,
            }
            self.icon_dict[len(self.icon_dict) + 1] = item_data

            pixmap = render_img_byte(self,img_bytes)
                            

        pdf_document.close()
        os.remove(pdf)
                

    #     if excel_or_word == True:
    #         for n_file in file_path:
    #             os.remove(n_file)
    #         excel_or_word = False

    # total_page = len(self.icon_dict)
    # self.n_pg_total.setText(f'/ {total_page}')
############################################################################
# def add_pages(self:Ui_Menu):
#     file_paths = search_file(self)
#     excel_or_word = False
#     for file_path in file_paths:
#         original_file_path = file_path
#         if file_path.lower().endswith(('.xlsx', '.xls')):
#             file_excel =  excel_to_pdf(self, file_path)
#             file_path = file_excel
#             excel_or_word = True
#         elif file_path.lower().endswith(('.docx' , '.doc')):
#             file_word =  word_to_pdf(self, file_path)
#             file_path = file_word
#             excel_or_word = True
#         else:
#             file_path = [original_file_path]

#         for file_path_dir in file_path:

#             pdf_document = fitz.open(file_path_dir)

#             for page_num in range(pdf_document.page_count):
#                 page = pdf_document.load_page(page_num)
#                 img_bytes = page.get_pixmap()
#                 img_bytes = img_bytes.tobytes()
                
#                 item_data = {
#                     "atual": str(len(self.icon_dict) + 1),
#                     "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
#                     # "local":original_file_path,
#                     "base64_pdf": base64_pdf,
#                     "n_pag_original":page_num,
#                     "rotate": 0,
#                     "local_watermark":None,
#                     "watermark_bytes":None,
#                     "watermark_transparence":None,
#                 }
#                 self.icon_dict[len(self.icon_dict) + 1] = item_data

#                 pixmap = render_img_byte(self,img_bytes)
                                

#                 pdf_document.close()
                

#         if excel_or_word == True:
#             for n_file in file_path:
#                 os.remove(n_file)
#             excel_or_word = False

#     total_page = len(self.icon_dict)
#     self.n_pg_total.setText(f'/ {total_page}')