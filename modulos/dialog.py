from PySide6.QtWidgets import QFileDialog
from pathlib import Path
from menu2_ui import Ui_Menu
import os


def search_file(main_widget: Ui_Menu, search_dialog):
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    file_dialog = QFileDialog()
    desktop = Path.home() / "Desktop"
    file_name, _ = file_dialog.getOpenFileName(main_widget, "Selecionar Arquivo", str(desktop), search_dialog, options=options)
    
    if file_name:
        # print("Arquivo selecionado:", file_name)
        main_widget.lineEdit.setText(file_name)

def local_save(main_widget: Ui_Menu, descript, extension):

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Obtém o texto do campo de entrada de texto como nome padrão
        pdf_file = main_widget.lineEdit.text()
        local, ext = os.path.splitext(pdf_file)
        local = local + extension

        # Cria um diálogo de salvar arquivo
        save_dialog = QFileDialog(main_widget)
        save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        save_dialog.setFileMode(QFileDialog.AnyFile)
        save_dialog.setOptions(options)

        # Abre o diálogo e obtém o nome do arquivo a ser salvo com o nome padrão
        local_save_file, _ = save_dialog.getSaveFileName(main_widget, "Salvar Arquivo", local, descript)
        
        if not local_save_file:
        # O usuário pressionou "Cancelar" no diálogo de salvar arquivo
            raise IndexError("Operação de salvar arquivo cancelada")

        return (pdf_file, local_save_file)
        # main_widget.tipo_export(default_file_name,selected_file)
        
