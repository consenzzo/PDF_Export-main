from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QListWidget, QAbstractItemView, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtCore import Slot, Qt, QSize, QByteArray, QEvent, Signal, QIODevice
from PySide6.QtGui import QPixmap, QIcon, QImage, QDrag, QAction, QTransform,QPainter,QTextDocument
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
import fitz  # PyMuPDF
from menu2_ui import Ui_Menu
from dict_validate import dict_validate
import check
import os
import xlwings as xw
from pathlib import Path
from docx2pdf import convert
import io
from reportlab.pdfgen import canvas
from PIL import Image
from openpyxl import load_workbook
from icon_button import icon_button
import base64


def add_pages(self:Ui_Menu, sender):
        function_name = None
        if dict_validate[sender]["check"] is not None:
            name_check = dict_validate[sender]["check"]
            function_name = getattr(check,name_check)
            check_function = function_name(self)

        if dict_validate[sender]["check"] is None or check_function == True :
            excel_or_word = False
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFiles)
            file_dialog.setNameFilter("All (*.pdf *.png *.jpeg *.jpg *.xlsx *.xls *.docx , *.doc);;Arquivos PDF (*.pdf);;Imagens (*.png *.jpg *.jpeg);;Excel (*.xlsx *.xls);; Word (*.docx , *.doc)")

            file_dialog.setViewMode(QFileDialog.List)

            if file_dialog.exec():
                file_paths = file_dialog.selectedFiles()

                for file_path in file_paths:
                    original_file_path = file_path
                    if file_path.lower().endswith(('.xlsx', '.xls')):
                        file_excel =  excel_file(self, file_path)
                        file_path = file_excel
                        excel_or_word = True
                    elif file_path.lower().endswith(('.docx' , '.doc')):
                        file_word =  word_file(self, file_path)
                        file_path = file_word
                        excel_or_word = True

                    pdf_document = fitz.open(file_path)

                    for page_num in range(pdf_document.page_count):
                        page = pdf_document.load_page(page_num)
                        img_bytes = page.get_pixmap()
                        img_bytes = img_bytes.tobytes()
                        

                        item_data = {
                            "atual": str(len(self.icon_dict) + 1),
                            "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
                            "local":original_file_path,
                            "n_pag_original":page_num,
                            "guidance": 0,
                            "watermark":None,
                            "watermark_bytes":None,
                            "watermark_transparence":None,
                        }
                        self.icon_dict[len(self.icon_dict) + 1] = item_data

                        pixmap = QPixmap()
                        pixmap.loadFromData(img_bytes)

                        list_item = QListWidgetItem()
                        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
                        list_item.setIcon(QIcon(pixmap))
                        list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
                        self.listWidget.addItem(list_item)
                                           

                    pdf_document.close()
                    if excel_or_word == True:
                        os.remove(file_path)
                    excel_or_word = False

                total_page = len(self.icon_dict)
                self.n_pg_total.setText(f'/ {total_page}')


def save_file(self: Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check, name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function:
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
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
                    for ext in [".pdf",".png", ".jpeg" , "*.jpg", ".xlsx", ".xls", ".docx", ".doc"]:
                        alternative_path = os.path.splitext(original_file_path)[0] + ext
                        if os.path.exists(alternative_path):

                            if ext in (".pdf"):
                                pdf_document = fitz.open(original_file_path)
                                break

                            elif ext in (".png", ".jpeg", "*.jpg"):
                                img = Image.open(original_file_path)
                                pdf_document = fitz.open()
                                temp_pdf_paths = image2pdf(img)
                                pdf_document.insert_pdf(fitz.open(temp_pdf_paths))
                                os.remove(temp_pdf_paths)
                                break


                            elif ext in ( ".xlsx", ".xls"):
                                temp_pdf_paths = excel_to_pdf(alternative_path)
                                pdf_document = fitz.open(temp_pdf_paths)
                                break
                                
                                

                            elif ext in (".docx", ".doc"):
                                temp_pdf_paths = word_to_pdf(alternative_path)
                                pdf_document = fitz.open(temp_pdf_paths)
                                break

                    
                else:
                    # Obter bytes da imagem do dicionário
                    img_bytes = page_data["icon_bytes"]
                    img = Image.open(io.BytesIO(img_bytes))
                    pdf_document = fitz.open()
                    temp_pdf_paths = image2pdf(img)
                    pdf_document.insert_pdf(fitz.open(temp_pdf_paths))
                    os.remove(temp_pdf_paths)


                
                # Obter a página desejada do documento original
                page = pdf_document.load_page(original_page_number )
                
                if position != 0:
                    # Rotacionar a página
                    page.set_rotation(position)

                watermark_path = page_data.get("watermark")
                if watermark_path:
                    if os.path.exists(watermark_path):
                        watermark_bytes = page_data.get("watermark_bytes")
                        # Adicionar a marca d'água ao PDF
                        if watermark_bytes:
                            watermark_img = Image.open(io.BytesIO(watermark_bytes))
                            watermark_pdf = fitz.open()
                            watermark_pdf.insert_pdf(fitz.open(image2pdf(watermark_img)))
                        else:
                            # Se não houver bytes da marca d'água, pode ser uma imagem externa
                            watermark_pdf = fitz.open(watermark_path)

                        pdf_document = apply_watermark_to_save(page, watermark_pdf, page_data.get("watermark_transparence"))

                #         # Copiar a página original para o novo documento
                # new_pdf.insert_pdf(pdf_document, from_page=original_page_number)

                # # Fechar o documento de marca d'água
                # watermark_pdf.close()

                # Copiar a página original para o novo documento
                new_pdf.insert_pdf(pdf_document, from_page=original_page_number, to_page=original_page_number)

                pdf_document.close()
                try:
                    os.remove(temp_pdf_paths)
                except:
                    pass
                

            new_pdf.save(save_path)
            new_pdf.close()
            QMessageBox.information(self, "Sucesso", "PDF salvo com sucesso!")
            self.listWidget.clear()

            # Remover a página correspondente do dicionário de ícones
            self.icon_dict.clear()

            total_page = len(self.icon_dict)
            self.n_pg_total.setText(f'/ {total_page}')
            item_row = self.listWidget.count()
            if item_row == 0:
                    for label_name, icon_data in icon_button.items():
                        if label_name == "display":
                            base64_image = icon_data["base64_data"]
                            image_data = base64.b64decode(base64_image)
                            # Cria um QPixmap a partir da imagem decodificada
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                            icon = QIcon(pixmap)
                            # Obtém o QLabel pelo nome e define o ícone
                            label = getattr(self, label_name)  # Obtém o QLabel pelo nome
                            label.setPixmap(pixmap)
                            self.n_pg_edit.setText("")
            refresh_save(self,save_path)

def apply_watermark_to_save(pdf_page, watermark_path, transparency=0.5):
    # Abrir o documento da marca d'água
    watermark_document = fitz.open(watermark_path)

    # Se o documento da marca d'água contiver apenas uma página, use-a diretamente
    if watermark_document.page_count == 1:
        watermark_page = watermark_document[0]
    else:
        # Se houver várias páginas, crie uma nova página única mesclando todas elas
        watermark_page = watermark_document.new_page(width=pdf_page.rect.width, height=pdf_page.rect.height)
        for page_num in range(watermark_document.page_count):
            page = watermark_document.load_page(page_num)
            # Desenhar o conteúdo da página no contexto da nova página
            watermark_page.insert_image((0, 0, watermark_page.rect.width, watermark_page.rect.height), pixmap=page.get_pixmap())

    # Criar uma nova página para mesclar a página original e a marca d'água
    new_page = pdf_page.duplicate()

    # Configurar a transparência da marca d'água
    new_page.set_opacity(transparency)

    # Desenhar o conteúdo da marca d'água na nova página
    new_page.insert_image((0, 0, new_page.rect.width, new_page.rect.height), pixmap=watermark_page.get_pixmap())

    # Fechar o documento da marca d'água
    watermark_document.close()

    return new_page






def add_image_to_pdf(image_file, pdf_document):
    # Converte a imagem para um formato que pode ser inserido no documento PDF
    byte_array = QByteArray()
    buffer = QIODevice(byte_array)

    # Cria uma imagem a partir dos bytes
    img = QImage(image_file)
    pixmap = QPixmap.fromImage(img)

    # Adiciona a imagem ao documento PDF
    pdf_document.insert_image(0, 0, pixmap)

    # Limpa o buffer
    buffer.close()

def to_divide_file(self:Ui_Menu,sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check, name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function:
        save_path, _ = QFileDialog.getSaveFileName(self, "Salvar PDF", "", "PDF Files (*.pdf)")
        base_name = os.path.splitext(save_path)[0]
        if save_path:
            page_number_max, ok = QInputDialog.getInt(self, 'Número da Página', 'Dividir documento da página 1 até:', 1, 1, 999, 1)
            new_pdf_01 = fitz.open()  # Criar um novo documento PDF
            new_pdf_02 = fitz.open()

            # Ordenar o dicionário com base no número da página da aplicação
            sorted_pages = sorted(self.icon_dict.items(), key=lambda x: int(x[1]["atual"]))

            for page_number, page_data in sorted_pages:
                original_file_path = page_data.get("local")  # Caminho do arquivo original
                icon_bytes = page_data.get("icon_bytes")  # Bytes da imagem

                if os.path.exists(original_file_path):
                     # Se não for um PDF, verificar outras extensões
                    pdf_document = None
                    for ext in [".pdf",".png", ".jpeg", "*.jpg", ".xlsx", ".xls", ".docx", ".doc"]:
                        alternative_path = os.path.splitext(original_file_path)[0] + ext
                        if os.path.exists(alternative_path):

                            if ext in (".pdf"):
                                pdf_document = fitz.open(original_file_path)
                                continue

                            elif ext in (".png", ".jpeg", "*.jpg"):
                                img = Image.open(original_file_path)
                                pdf_document = fitz.open()
                                temp_pdf_paths = image2pdf(img)
                                pdf_document = fitz.open(temp_pdf_paths)
                                
                                continue


                            elif ext in ( ".xlsx", ".xls"):
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
                    pdf_document = fitz.open(temp_pdf_paths)
                    os.remove(temp_pdf_paths)

                if page_number <= page_number_max:
                    # Adiciona a página ao novo documento PDF 01
                    new_pdf_01.insert_pdf(pdf_document, from_page=0, to_page=0)
                else:
                    # Adiciona a página ao novo documento PDF 02
                    new_pdf_02.insert_pdf(pdf_document, from_page=0, to_page=0)

                pdf_document.close()
                try:
                    os.remove(temp_pdf_paths)
                except:
                    pass

            new_pdf_01.save(f'{base_name}_pag1_{page_number_max}.pdf')
            new_pdf_01.close()
            new_pdf_02.save(f'{base_name}_pag{page_number_max+1}_{page_number}.pdf')
            new_pdf_02.close()

            QMessageBox.information(self, "Sucesso", "PDF salvo com sucesso!")


def excel_file(self : Ui_Menu, file_path):
    with xw.App() as app:
        # user will not even see the excel opening up
        app.visible = False
        book = app.books.open(file_path)
        sheet = book.sheets[0]
        # sheet.page_setup.print_area = '$A$1:$Q$66'
        
        # Construct path for pdf file
        current_work_dir = os.getcwd()
        pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
        # pdf_file_name = "pdf_workbook_printout.pdf"
        pdf_path = Path(pdf_file)

        # Save excel workbook as pdf and showing it
        sheet.to_pdf(path=pdf_path, show=False)

        return pdf_path


def word_file(self: Ui_Menu , file_path):
    pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
    convert(file_path , pdf_file)
    return pdf_file


def image2pdf(img):
    pdf_path = "temp.pdf"
    img.save(pdf_path, "PDF", resolution=100.0)
    return pdf_path

def excel_to_pdf(file_path):
     with xw.App() as app:
        # user will not even see the excel opening up
        app.visible = False
        book = app.books.open(file_path)
        sheet = book.sheets[0]
        # sheet.page_setup.print_area = '$A$1:$Q$66'
        
        # Construct path for pdf file
        current_work_dir = os.getcwd()
        pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
        # pdf_file_name = "pdf_workbook_printout.pdf"
        pdf_path = Path(pdf_file)

        # Save excel workbook as pdf and showing it
        sheet.to_pdf(path=pdf_path, show=False)

        return pdf_path
     

def word_to_pdf( file_path):
    pdf_file = os.path.join(os.path.dirname(file_path), f"{os.path.splitext(os.path.basename(file_path))[0]}.pdf")
    convert(file_path , pdf_file)
    return pdf_file


def refresh_save(self:Ui_Menu,save_path):
    file_path = save_path
    excel_or_word = False

    original_file_path = file_path
    if file_path.lower().endswith(('.xlsx', '.xls')):
        file_excel =  excel_file(self, file_path)
        file_path = file_excel
        excel_or_word = True
    elif file_path.lower().endswith(('.docx' , '.doc')):
        file_word =  word_file(self, file_path)
        file_path = file_word
        excel_or_word = True

    pdf_document = fitz.open(file_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        img_bytes = page.get_pixmap()
        img_bytes = img_bytes.tobytes()
        

        item_data = {
            "atual": str(len(self.icon_dict) + 1),
            "icon_bytes": img_bytes,  # Bytes do ícone para armazenar
            "local":original_file_path,
            "n_pag_original":page_num,
            "guidance": 0
        }
        self.icon_dict[len(self.icon_dict) + 1] = item_data

        pixmap = QPixmap()
        pixmap.loadFromData(img_bytes)

        list_item = QListWidgetItem()
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        list_item.setIcon(QIcon(pixmap))
        list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
        self.listWidget.addItem(list_item)
                            

    pdf_document.close()
    if excel_or_word == True:
        os.remove(file_path)
    excel_or_word = False

    total_page = len(self.icon_dict)
    self.n_pg_total.setText(f'/ {total_page}')