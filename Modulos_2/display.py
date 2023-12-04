from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QListWidget, QAbstractItemView, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, Qt, QSize, QByteArray, QEvent, Signal
from PySide6.QtGui import QPixmap, QIcon, QImage, QDrag, QAction, QTransform
import check
from dict_validate import dict_validate
from icon_button import icon_button
import base64
import os
from convert import excel_file , word_file
import fitz  # PyMuPDF


def display_image(self:Ui_Menu, sender):
        function_name = None
        if dict_validate[sender]["check"] is not None:
            name_check = dict_validate[sender]["check"]
            function_name = getattr(check,name_check)
            check_function = function_name(self)

        if dict_validate[sender]["check"] is None or check_function == True :
            selected_row = self.listWidget.currentRow()
            
            if selected_row >= 0:
                for page, data in self.icon_dict.items():
                    current = data['atual']
                    if int(current) == selected_row + 1:
                        image_bytes = self.icon_dict[page]['icon_bytes']
                        byte_array = QByteArray(image_bytes)
                        image = QImage()
                        image.loadFromData(byte_array)
                        pixmap = QPixmap(image)

                        self.display.setPixmap(pixmap)
                        self.n_pg_edit.setText(current)
                        self.horizontalSlider.setValue(31)
                        self.scrollAreaWidgetContents.setMinimumSize(QSize(pixmap.size()))
                        return

def load_pages(self, files:list):
    for file_path in files:
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


def next_page(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        if self.listWidget.currentRow() < self.listWidget.count() - 1:
            current_row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(current_row + 1)

def back_page(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        if self.listWidget.currentRow() > 0:
            current_row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(current_row - 1)

def go_to_page(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        numb = self.n_pg_edit.text()
        total_page = self.listWidget.count() - 1
        text_lineEdit = self.listWidget.currentRow()

        if numb.isdigit():
            page_number = int(numb) - 1
            if page_number < 0 or page_number > total_page:
                text_lineEdit +=1
                self.n_pg_edit.setText(str(text_lineEdit))
            else:
                self.listWidget.setCurrentRow(page_number)
        else:
            text_lineEdit +=1
            self.n_pg_edit.setText(str(text_lineEdit))


def move_page_up(self:Ui_Menu):
    initial_position = self.listWidget.currentRow()
    if initial_position == 0:
        pass
    else:
        initial_position += 1
        final_position = initial_position - 1
        move_page(self, initial_position, final_position)



def move_page_down(self:Ui_Menu):
    initial_position = self.listWidget.currentRow()
    if initial_position == self.listWidget.count() - 1:
        pass
    else:
        initial_position += 1
        final_position = initial_position + 1
        move_page(self, initial_position, final_position)



def move_page(self:Ui_Menu, initial_position, final_position):

    if initial_position != final_position:
        for page, data in self.icon_dict.items():
            current_position = int(data["atual"])

            if current_position == initial_position:
                data["atual"] = str(final_position)
            elif initial_position < final_position:
                if initial_position < current_position <= final_position:
                    data["atual"] = str(current_position - 1)
            else:
                if final_position <= current_position < initial_position:
                    data["atual"] = str(current_position + 1)

        sort_list_widget(self, final_position)

def sort_list_widget(self:Ui_Menu, final_position):
    # Limpe a listWidget
    self.listWidget.setCurrentRow(-1)
    self.listWidget.clear()
    
    new_dict = dict(sorted(self.icon_dict.items(), key=lambda x: x[1]['atual']))

    for page, data in new_dict.items():
        pixmap = QPixmap()
        pixmap.loadFromData(data["icon_bytes"])
        list_item = QListWidgetItem()
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        list_item.setIcon(QIcon(pixmap))
        list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
        self.listWidget.addItem(list_item)
    self.listWidget.setCurrentRow(final_position-1)

@Slot(int, int)
def on_dropped(self:Ui_Menu, initial, final):
    # print(f"Item da linha {initial} foi arrastado para linha {final}")
    move_page(self, initial, final)
                

def close_file(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
            
        confirmation = QMessageBox.question(
            self, 'Finalizar',
            'Tem certeza de que deseja fechar este documento?',
            QMessageBox.Yes | QMessageBox.No
        )
        

        if confirmation == QMessageBox.Yes:
            # Remover a página selecionada do QListWidget
            
            
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
            
    else:
        ...

def zoom_in(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        slider_value = self.horizontalSlider.value()
        slider_value += 5
        if slider_value > 50:
            slider_value = 50
        self.horizontalSlider.setValue(slider_value)


def zoom_out(self:Ui_Menu, sender):
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        slider_value = self.horizontalSlider.value()
        slider_value -= 5
        if slider_value < 12:
            slider_value = 12
        self.horizontalSlider.setValue(slider_value)
        

        

def zoom_slider_changed(self:Ui_Menu, value, sender):
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        zoom_factor = (value / 25.0)
        update_zoom(self, zoom_factor)

def update_zoom(self:Ui_Menu, zoom_factor):
        selected_row = self.listWidget.currentRow()
        for page, data in self.icon_dict.items():
            current = data['atual']
            if int(current) == selected_row + 1:
                image_bytes = self.icon_dict[page]['icon_bytes']
                byte_array = QByteArray(image_bytes)
                image = QImage()
                image.loadFromData(byte_array)
                pixmap = QPixmap(image)
        
        
        new_width = pixmap.width() * zoom_factor
        new_height = pixmap.height() * zoom_factor
        new_pixmap = pixmap.scaled(new_width, new_height, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.display.setPixmap(new_pixmap)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(new_pixmap.size()))