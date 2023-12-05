from menu2_ui import Ui_Menu
import sys
import base64
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QMouseEvent
from icon_button import icon_button
from add_file import add_pages
from display import display_image
from edit_file import delete_selected_page, rotate_image_r, rotate_image_l
from navigation import next_page, back_page, go_to_page, zoom_in, zoom_out, zoom_slider_changed



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
        self.next_pg.clicked.connect(lambda: next_page(self))
        self.back_pg.clicked.connect(lambda: back_page(self))
        self.n_pg_edit.editingFinished.connect(lambda: go_to_page(self))
        # self.up_pg.clicked.connect(lambda: move_page_up(self))
        # self.down_pg.clicked.connect(lambda: move_page_down(self))
        # self.listWidget.dropped.connect(lambda initial, final: on_dropped(self, initial, final))
        # self.save_file.clicked.connect(lambda: save_file(self,"save_file"))
        # self.close_file.clicked.connect(lambda: close_file(self,"close_file"))
        self.rotate_rigth.clicked.connect(lambda: rotate_image_r(self))
        self.rotate_left.clicked.connect(lambda: rotate_image_l(self))
        self.zoom_in.clicked.connect(lambda: zoom_in(self))
        self.zoom_out.clicked.connect(lambda: zoom_out(self))
        self.horizontalSlider.valueChanged.connect(lambda value : zoom_slider_changed(self, value))
        # self.to_divide_file.clicked.connect(lambda: to_divide_file(self,"to_divide_file"))
        # self.zip_file.clicked.connect(lambda: zip_file(self,"zip_file"))
        # self.add_new_file.clicked.connect(lambda: add_pages(self, "add_new_file"))
        # self.add_m_d_agua.clicked.connect(lambda: add_watermark(self, "add_m_d_agua"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    
    