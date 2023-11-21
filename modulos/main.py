from menu2_ui import Ui_Menu
from dialog import search_file, local_save
from expo_img import expo_Img_Button
from expo_pg import expo_pg_Button
from dict_function import dict_function
from validate import validate_option
from pdf_to_word import pdf_to_word
from pdf_to_excel import pdf_to_excel
from word_to_pdf import word_to_pdf
from excel_to_pdf import excel_to_pdf
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QGroupBox, QCommandLinkButton, QToolBox
import sys



buttons_dict = None
nome_funcao = None
class MyWidget(QWidget, Ui_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        

        #RadioButton fica checked automático ao editar a LineEdit
        self.de_Edit.textEdited.connect(lambda text: self.de_ate_radioButton.setChecked(bool(text)))
        self.ate_Edit.textEdited.connect(lambda text: self.de_ate_radioButton.setChecked(bool(text)))
        self.pages_Edit.textEdited.connect(lambda text: self.pages_radioButton.setChecked(bool(text)))

        #Botão Limpar
        self.limpar_Button.clicked.connect(self.lineEdit.clear)

        #Botões ao serem marcados irão desmarcar outros
        self.expo_Img_Button.clicked.connect(self.clearToolBoxButtons)
        self.expo_pg_Button.clicked.connect(self.clearToolBoxButtons)
        self.pdf_to_word.clicked.connect(self.clearToolBoxButtons)
        self.pdf_to_excel.clicked.connect(self.clearToolBoxButtons)
        self.word_to_pdf.clicked.connect(self.clearToolBoxButtons)
        self.excel_to_pdf.clicked.connect(self.clearToolBoxButtons)

        #Validador dos campos onde o usuário informa os números das páginas
        self.de_Edit.textChanged.connect(self.validate_input)
        self.ate_Edit.textChanged.connect(self.validate_input)
        self.pages_Edit.textChanged.connect(self.validate_input_hifen)



        # self.buscar_Button.clicked.connect(lambda: search_file(self))
        self.buscar_Button.clicked.connect(self.validate_button)
        self.expo_Img_Button.clicked.connect(self.validate_button)
        self.expo_pg_Button.clicked.connect(self.validate_button)
        self.confirm_Button.clicked.connect(self.validate_button)
        self.de_ate_radioButton.clicked.connect(self.validate_button)
        self.pages_radioButton.clicked.connect(self.validate_button)
        self.pdf_to_word.clicked.connect(self.validate_button)
        self.pdf_to_excel.clicked.connect(self.validate_button)
        self.word_to_pdf.clicked.connect(self.validate_button)
        self.excel_to_pdf.clicked.connect(self.validate_button)
        
        


    def validate_button(self):
        validation = validate_option(self)
        if validation:
            global buttons_dict
            global nome_funcao
            sender_button = self.sender()
            button_name = sender_button.objectName()
            if dict_function[button_name]['context_menu'] == 'toolBox':
            # buttons_dict[button_name] = button_name
                nome_funcao = dict_function[button_name]['function']
                buttons_dict = button_name
            if validation == 10:
                self.continue_func()



    def continue_func(self):
        # try:
            descript = dict_function[buttons_dict]['description']
            extension = dict_function[buttons_dict]['extension']
            # print(descript)
            funcao = getattr(sys.modules[__name__], nome_funcao)
            pdf_file, local_save_file = local_save(self , descript, extension)
            funcao(self , pdf_file , local_save_file)
        # except AttributeError:
        #     print(f"A função '{nome_funcao}' não existe")
        # except IndexError as e:
        #     print(f"Erro: {e}")
    

    def clearToolBoxButtons(self):
        button_names = []
        name_button = self.sender().objectName()
        menu = dict_function[name_button]['context_menu']
        menu = self.findChild(QToolBox, menu)
        button_names = [
            widget.objectName() for widget in menu.findChildren(QCommandLinkButton)
        ]
        for button_name in button_names:
            if button_name == name_button:
                ...
            else:
                self.findChild(QCommandLinkButton, button_name).setChecked(False)


    def validate_input(self, text):
        if text != '':
            validation = validate_option(self)
            if not validation:
                self.ate_Edit.clear()
                self.de_Edit.clear()
                return 
        # Remove qualquer caractere que não seja um dígito
        cleaned_text = ''.join(filter(str.isdigit, text))
        sender = self.sender()
        sender.setText(cleaned_text)


    def validate_input_hifen(self, text):
        if text != '':
            validation = validate_option(self)
            if not validation:
                self.pages_Edit.clear()
                return
        # Remove qualquer caractere que não seja um dígito ou o caractere "-"
        cleaned_text = ''.join(filter(lambda char: char.isdigit() or char == '-', text))
        sender = self.sender()  
        sender.setText(cleaned_text)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
    
