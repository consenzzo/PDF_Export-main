from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtGui import QPixmap, QIcon, QImage
from PySide6.QtCore import QSize, Qt, QByteArray

def render_img_byte(self:Ui_Menu,img_bytes):
    pixmap = QPixmap()
    pixmap.loadFromData(img_bytes)

    list_item = QListWidgetItem()
    pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
    list_item.setIcon(QIcon(pixmap))
    list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
    self.listWidget.addItem(list_item)



def display_image(self:Ui_Menu):
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