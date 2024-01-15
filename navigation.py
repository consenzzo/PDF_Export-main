from menu2_ui import Ui_Menu
from PySide6.QtCore import QByteArray, QSize, Qt
from PySide6.QtGui import QPixmap, QImage

def next_page(self:Ui_Menu):
    if self.listWidget.currentRow() < self.listWidget.count() - 1:
        current_row = self.listWidget.currentRow()
        self.listWidget.setCurrentRow(current_row + 1)

def back_page(self:Ui_Menu):
    if self.listWidget.currentRow() > 0:
        current_row = self.listWidget.currentRow()
        self.listWidget.setCurrentRow(current_row - 1)

def go_to_page(self:Ui_Menu):
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


def zoom_in(self:Ui_Menu):
    slider_value = self.horizontalSlider.value()
    slider_value += 5
    if slider_value > 50:
        slider_value = 50
    self.horizontalSlider.setValue(slider_value)


def zoom_out(self:Ui_Menu):
    slider_value = self.horizontalSlider.value()
    slider_value -= 5
    if slider_value < 12:
        slider_value = 12
    self.horizontalSlider.setValue(slider_value)
        

        

def zoom_slider_changed(self:Ui_Menu, value):
    if not self.listWidget.count():
        pass
    else:
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