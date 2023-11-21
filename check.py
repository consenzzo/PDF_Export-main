from menu2_ui import Ui_Menu
from message import pages_not_selected, not_page_file
from icon_button import icon_button
import base64
from PySide6.QtGui import QPixmap, QIcon

def select_items_listWidget(self:Ui_Menu):
    if self.listWidget.currentRow() == -1:
        return pages_not_selected(self)
    else:
        return True

def count_row_listWidget(self:Ui_Menu):
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
                    return not_page_file(self)
    else:
         return True