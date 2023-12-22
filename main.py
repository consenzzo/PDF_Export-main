from menu2_ui import Ui_Menu
import sys
import base64
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QMouseEvent
from icon_button import icon_button
from add_file import add_pages
from display import display_image, close_file
from edit_file import delete_selected_page, rotate_image_r, rotate_image_l, move_page_up, move_page_down, on_dropped, add_watermark,remove_watermark,add_footer,remove_n_page
from navigation import next_page, back_page, go_to_page, zoom_in, zoom_out, zoom_slider_changed
from save_file import save_file_pdf, save_file_word,save_file_excel, save_file_png,save_file_jpg
from password import remove_password, password_pdf

class MyWidget(QWidget, Ui_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.icon_dict = {}
        

        for label_name, icon_data in icon_button.items():
            base64_image = icon_data["base64_data"]
            image_data = base64.b64decode(base64_image)
            # Cria um QPixmap a partir da imagem decodificada
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            icon = QIcon(pixmap)
            # Obtém o QLabel pelo nome e define o ícone
            label = getattr(self, label_name)  # Obtém o QLabel pelo nome
            label.setPixmap(pixmap)
            


        self.add_pg.clicked.connect(lambda: add_pages(self))
        self.listWidget.currentRowChanged.connect(lambda: display_image(self))
        self.delete_pg.clicked.connect(lambda: delete_selected_page(self))
        self.delete_page_menu.clicked.connect(lambda: delete_selected_page(self))
        self.next_pg.clicked.connect(lambda: next_page(self))
        self.back_pg.clicked.connect(lambda: back_page(self))
        self.n_pg_edit.editingFinished.connect(lambda: go_to_page(self))
        self.up_pg.clicked.connect(lambda: move_page_up(self))
        self.down_pg.clicked.connect(lambda: move_page_down(self))
        self.listWidget.dropped.connect(lambda initial, final: on_dropped(self, initial, final))
        self.save_file.clicked.connect(lambda: save_file_pdf(self))
        self.save_to_pdf.clicked.connect(lambda: save_file_pdf(self))
        self.close_file.clicked.connect(lambda: close_file(self))
        self.rotate_rigth.clicked.connect(lambda: rotate_image_r(self))
        self.rotate_left.clicked.connect(lambda: rotate_image_l(self))
        self.zoom_in.clicked.connect(lambda: zoom_in(self))
        self.zoom_out.clicked.connect(lambda: zoom_out(self))
        self.horizontalSlider.valueChanged.connect(lambda value : zoom_slider_changed(self, value))
        # self.to_divide_file.clicked.connect(lambda: to_divide_file(self,"to_divide_file"))
        # self.zip_file.clicked.connect(lambda: zip_file(self,"zip_file"))
        self.add_new_file.clicked.connect(lambda: add_pages(self))
        self.add_m_d_agua.clicked.connect(lambda: add_watermark(self))
        self.delete_m_d_agua.clicked.connect(lambda: remove_watermark(self))
        self.add_n_pg.clicked.connect(lambda: add_footer(self))
        self.delete_n_pg.clicked.connect(lambda: remove_n_page(self))
        self.pdf_to_word.clicked.connect(lambda: save_file_word(self))
        self.pdf_to_excel.clicked.connect(lambda: save_file_excel(self))
        self.expo_Img_Button_png.clicked.connect(lambda: save_file_png(self))
        self.expo_Img_Button_jpg.clicked.connect(lambda: save_file_jpg(self))
        self.remove_password.clicked.connect(lambda: remove_password(self))
        self.add_password.clicked.connect(lambda: password_pdf(self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    
    