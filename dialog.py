from menu2_ui import Ui_Menu
from PySide6.QtWidgets import  QFileDialog


def search_file(self:Ui_Menu):
    try:
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("All (*.pdf *.png *.jpeg *.jpg *.xlsx *.xls *.docx , *.doc);;Arquivos PDF (*.pdf);;Imagens (*.png *.jpg *.jpeg);;Excel (*.xlsx *.xls);; Word (*.docx , *.doc)")

        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec_():
            
            file_paths = file_dialog.selectedFiles()


            return file_paths
        else:

            return []
    except Exception as e:

        return []