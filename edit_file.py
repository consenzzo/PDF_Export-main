from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QIcon
import base64
from icon_button import icon_button

def delete_selected_page(self:Ui_Menu):
    selected_row = self.listWidget.currentRow()

    if selected_row >= 0:
        
        confirmation = QMessageBox.question(
            self, 'Confirmar Exclusão',
            'Tem certeza de que deseja excluir esta página?',
            QMessageBox.Yes | QMessageBox.No
        )
        

        if confirmation == QMessageBox.Yes:
            # Remover a página selecionada do QListWidget
            self.listWidget.takeItem(selected_row)

            # Remover a página correspondente do dicionário de ícones
            for page, data in list(self.icon_dict.items()):
                if int(data["atual"]) == selected_row + 1:
                    del self.icon_dict[page]
                    break  # Saímos do loop assim que a página for encontrada e removida

            # Atualizar os números das páginas restantes
            for page, data in self.icon_dict.items():
                if int(data["atual"]) > selected_row + 1:
                    data["atual"] = str(int(data["atual"]) - 1)

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
                self.listWidget.setCurrentRow(selected_row - 1)
            
    else:
        QMessageBox.warning(self, 'Aviso', 'Nenhuma página selecionada para exclusão.')