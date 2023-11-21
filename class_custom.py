from PySide6.QtWidgets import QLabel,QApplication, QMainWindow, QListWidgetItem, QWidget, QListWidget, QAbstractItemView
from PySide6.QtCore import Qt, Signal,Slot,QSize, QMimeData, QByteArray, QDataStream, QIODevice
from PySide6.QtGui import QPixmap, QIcon, QImage, QDrag, QDragEnterEvent
import sys
import fitz  # PyMuPDF

class CustomLabel(QLabel):
    clicked = Signal()  # Sinal personalizado

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emitir sinal personalizado quando clicado


class CustomListWidget(QListWidget):
    # item_dragged = Signal(int)
    dropped = Signal(int, int)

    def __init__(self,object):
        super().__init__()
        self.icon_dict = {}  # Dicionário para armazenar informações de ícones
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.itemPressed.connect(self.capture_dragged_item)
        
        
        

    def capture_dragged_item(self, item):
        self.dragged_row = self.row(item)
        # self.item_dragged.emit(self.dragged_row)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        super().dropEvent(event)
        index = self.indexAt(event.pos())
        row_dropped = index.row()
        if hasattr(self, 'dragged_row'):
            initial = self.dragged_row + 1
            final = row_dropped + 1
            if initial != final:
                self.dropped.emit(initial, final)

    def dragMoveEvent(self, event):
        event.accept()

    def dragLeaveEvent(self, event):
        pass