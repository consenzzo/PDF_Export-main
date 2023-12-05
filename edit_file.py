from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QIcon, QTransform
from PySide6.QtCore import QByteArray, QBuffer, QIODevice, QSize, Qt
import base64
from icon_button import icon_button
from convert import base64_to_pdf, pdf_to_base64
import fitz  # PyMuPDF
import os
from display import render_img_byte, display_image

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


def rotate_image_r(self:Ui_Menu):
    rotate_img(self, 90)


def rotate_image_l(self:Ui_Menu):
    rotate_img(self, -90)

def rotate_img(self:Ui_Menu, degrees):
    page_current = self.listWidget.currentRow() + 1
    current_item = self.listWidget.currentItem()
    for page, data in self.icon_dict.items():
        current = int(data['atual'])
        if current == page_current:
            base64 = self.icon_dict[page]["base64_pdf"]
            local_file = base64_to_pdf(base64,"temp_rotate_page.pdf")
            pdf_document = fitz.open(local_file)
            for pagina_index in range(pdf_document.page_count):
                pagina = pdf_document[pagina_index]
                current_angle = self.icon_dict[page]["rotate"]
                current_angle = (current_angle + degrees) % 360
                pagina.set_rotation(current_angle)
                self.icon_dict[page]["rotate"] = current_angle


            # Salva as alterações no novo arquivo PDF
            pdf_document.save("temp_rotate_page.pdf")
            new_page = pdf_document.load_page(pagina_index)
            img_bytes = new_page.get_pixmap()
            img_bytes = img_bytes.tobytes()

            # Fecha o arquivo PDF
            pdf_document.close()
            os.remove(local_file)

            new_base64 = pdf_to_base64("temp_rotate_page.pdf",0)
            os.remove("temp_rotate_page.pdf")
            self.icon_dict[page]["base64_pdf"] = new_base64
            self.icon_dict[page]["icon_bytes"] = img_bytes
            
            # Atualize diretamente o ícone do item atual na QListWidget
            pixmap = QPixmap()
            pixmap.loadFromData(img_bytes)
            pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
            current_item.setIcon(QIcon(pixmap))
            current_item.setSizeHint(QSize(pixmap.size()))
            display_image(self)





    # pixmap = self.display.pixmap()
    # if not pixmap.isNull():
    #     image = pixmap.toImage()
    #     rotated_image = image.transformed(QTransform().rotate(90))
    #     self.display.setPixmap(QPixmap.fromImage(rotated_image))
    # current_item = self.listWidget.currentItem()
    # if current_item:
    #     current_icon = current_item.icon()
    #     # pixmap = current_icon.pixmap(current_item.icon())
    #     rotated_pixmap = QPixmap(pixmap.transformed(QTransform().rotate(90)))
    #     rotated_icon = QIcon(rotated_pixmap)
    #     current_item.setIcon(rotated_icon)
    #     byte_array = QByteArray()
    #     buffer = QBuffer(byte_array)
    #     buffer.open(QIODevice.WriteOnly)
    #     rotated_image.save(buffer, "PNG")  # Substitua "PNG" pelo formato desejado
    #     buffer.close()
    #     byte_array = byte_array.data()
        
        
    
    # page_rotate = self.listWidget.currentRow() + 1
    # rotate = self.icon_dict[page_rotate]["guidance"]
    # self.icon_dict[page_rotate]["icon_bytes"] = byte_array
    # rotate += 90
    # if rotate == 360:
    #     self.icon_dict[page_rotate]["rotate"] = 0
    # else:
    #     self.icon_dict[page_rotate]["rotate"] = rotate
    
        



        