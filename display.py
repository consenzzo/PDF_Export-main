from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QListWidgetItem , QMessageBox
from PySide6.QtGui import QPixmap, QIcon, QImage
from PySide6.QtCore import QSize, Qt, QByteArray
from icon_button import icon_button
import base64

def render_img_byte(self:Ui_Menu,img_bytes):
    pixmap = QPixmap()
    pixmap.loadFromData(img_bytes)

    list_item = QListWidgetItem()
    pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
    list_item.setIcon(QIcon(pixmap))
    list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
    return list_item
    



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
            
def close_file(self:Ui_Menu):
 
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
