from menu2_ui import Ui_Menu
from dialog import search_file
from convert import excel_to_pdf, word_to_pdf, scale_image, img_to_pdf, pdf_to_base64
from display import render_img_byte
import fitz  # PyMuPDF
import os

def add_pages(self:Ui_Menu):
    file_paths = search_file(self)

    for file_path in file_paths:
        original_file_path = file_path

        if file_path.lower().endswith(('.xlsx', '.xls')):
            pdf =  excel_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)
            
        elif file_path.lower().endswith(('.docx' , '.doc')):
            pdf =  word_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)

        elif file_path.lower().endswith(('.png', '.jpeg', '.jpg')):
            scaled_path = scale_image(self, file_path, 2480, 3508)
            if scaled_path:
                file_path = scaled_path
            pdf =  img_to_pdf(self, file_path)
            add_page_dict(self,pdf)
            os.remove(pdf)
            if scaled_path:
                os.remove(scaled_path)
        else:
            pdf =  file_path
            add_page_dict(self,pdf)

    total_page = len(self.icon_dict)
    self.n_pg_total.setText(f'/ {total_page}')


                
def add_page_dict(self:Ui_Menu, pdf):
    pdf_document = fitz.open(pdf)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        img_bytes = page.get_pixmap()
        img_bytes = img_bytes.tobytes()
        base_64 = pdf_to_base64(pdf, page_num)


        
        item_data = {
            "atual": str(len(self.icon_dict) + 1),
            "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
            # "local":original_file_path,
            "base64_pdf": base_64,
            # "n_pag_original":page_num,
            "rotate": 0,
            # "local_watermark":None,
            "watermark_base64_pdf":None,
            # "watermark_transparence":None,
            
        }
        self.icon_dict[len(self.icon_dict) + 1] = item_data

        pixmap_list = render_img_byte(self,img_bytes)
        self.listWidget.addItem(pixmap_list)
                        

    pdf_document.close()