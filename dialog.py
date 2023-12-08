from menu2_ui import Ui_Menu
from PySide6.QtWidgets import  QFileDialog, QDialog


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
    

def search_watermark(self:Ui_Menu):
    try:
        # Abrir um diálogo para selecionar a imagem da marca d'água
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # Defina o modo para selecionar um arquivo existente
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg)")
        
        if file_dialog.exec_() == QDialog.Accepted:
            # Obter a lista de arquivos selecionados (deve ser apenas um, já que o modo é ExistingFile)
            selected_files = file_dialog.selectedFiles()

            # Retornar o primeiro arquivo da lista (ou None se a lista estiver vazia)
            return selected_files[0] if selected_files else None
        else:
            return None

    except Exception as e:
        print(f"Erro ao selecionar a imagem de marca d'água: {e}")
        return None