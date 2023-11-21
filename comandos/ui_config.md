# TODOS OS COMANDOS ABAIXO ESTÃO OBSOLETOS, ESTÁ SENDO TUDO CONFIGURADO NO MÓDULO MAIN


# Configurações a serem inseridas no arquivo .ui nas atualizações: #

self.limpar_Button.clicked.connect(self.lineEdit.clear)
self.expo_Img_Button.clicked.connect(lambda: self.expo_pg_Button.setChecked(False))
self.expo_pg_Button.clicked.connect(lambda: self.expo_Img_Button.setChecked(False))
self.de_Edit.textEdited.connect(lambda text: self.de_ate_radioButton.setChecked(bool(text)))
self.ate_Edit.textEdited.connect(lambda text: self.de_ate_radioButton.setChecked(bool(text)))
self.pages_Edit.textEdited.connect(lambda text: self.pages_radioButton.setChecked(bool(text)))
# Conectar a função lambda diretamente ao textEdited para a validação
self.de_Edit.textChanged.connect(self.validate_input)
self.ate_Edit.textChanged.connect(self.validate_input)
self.pages_Edit.textChanged.connect(self.validate_input_hifen)



# No final
def validate_input(self, text):
        # Esta função será chamada quando o texto mudar em qualquer um dos QLineEdits
        # Remove qualquer caractere que não seja um dígito
        cleaned_text = ''.join(filter(str.isdigit, text))
        # Define o texto limpo de volta no QLineEdit atual
        sender = self.sender()  # Obtém o QLineEdit atual
        sender.setText(cleaned_text)

def validate_input_hifen(self, text):
    # Esta função será chamada quando o texto mudar em qualquer um dos QLineEdits
    # Remove qualquer caractere que não seja um dígito ou o caractere "-"
    cleaned_text = ''.join(filter(lambda char: char.isdigit() or char == '-', text))
    # Define o texto limpo de volta no QLineEdit atual
    sender = self.sender()  # Obtém o QLineEdit atual
    sender.setText(cleaned_text)