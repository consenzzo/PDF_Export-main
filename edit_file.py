from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QListWidget, QAbstractItemView, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, Qt, QSize, QByteArray, QEvent, Signal, QBuffer, QIODevice
from PySide6.QtGui import QPixmap, QIcon, QImage, QDrag, QAction, QTransform
from dict_validate import dict_validate
import check
import base64
from icon_button import icon_button


def delete_selected_page(self:Ui_Menu ,sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :

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
            QMessageBox.warning(self, 'Aviso', 'Nenhuma página selecionada para exclusão.')



def rotate_image_r(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        pixmap = self.display.pixmap()
        if not pixmap.isNull():
            image = pixmap.toImage()
            rotated_image = image.transformed(QTransform().rotate(90))
            self.display.setPixmap(QPixmap.fromImage(rotated_image))
        current_item = self.listWidget.currentItem()
        if current_item:
            current_icon = current_item.icon()
            # pixmap = current_icon.pixmap(current_item.icon())
            rotated_pixmap = QPixmap(pixmap.transformed(QTransform().rotate(90)))
            rotated_icon = QIcon(rotated_pixmap)
            current_item.setIcon(rotated_icon)
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            rotated_image.save(buffer, "PNG")  # Substitua "PNG" pelo formato desejado
            buffer.close()
            byte_array = byte_array.data()
          
            
        
        page_rotate = self.listWidget.currentRow() + 1
        rotate = self.icon_dict[page_rotate]["guidance"]
        self.icon_dict[page_rotate]["icon_bytes"] = byte_array
        rotate += 90
        if rotate == 360:
            self.icon_dict[page_rotate]["guidance"] = 0
        else:
            self.icon_dict[page_rotate]["guidance"] = rotate
        
        


def rotate_image_l(self:Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check,name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function == True :
        pixmap = self.display.pixmap()
        if not pixmap.isNull():
            image = pixmap.toImage()
            rotated_image = image.transformed(QTransform().rotate(-90))
            self.display.setPixmap(QPixmap.fromImage(rotated_image))
        current_item = self.listWidget.currentItem()
        if current_item:
            current_icon = current_item.icon()
            # pixmap = current_icon.pixmap(current_item.icon())
            rotated_pixmap = QPixmap(pixmap.transformed(QTransform().rotate(-90)))
            rotated_icon = QIcon(rotated_pixmap)
            current_item.setIcon(rotated_icon)
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            rotated_image.save(buffer, "PNG")  # Substitua "PNG" pelo formato desejado
            buffer.close()
            byte_array = byte_array.data()



        page_rotate = self.listWidget.currentRow() + 1
        rotate = self.icon_dict[page_rotate]["guidance"]
        self.icon_dict[page_rotate]["icon_bytes"] = byte_array
        rotate -= 90
        if rotate == -360:
            self.icon_dict[page_rotate]["guidance"] = 0
        else:
            self.icon_dict[page_rotate]["guidance"] = rotate
        
