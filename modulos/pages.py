from menu2_ui import Ui_Menu



def page_print(main_widget: Ui_Menu):

    if main_widget.pages_radioButton.isChecked():
        input_str = str(main_widget.pages_Edit.text())  # Sua string de input
        valores = input_str.split("-")
        valores = [valor.strip() for valor in valores]
        numeros = [int(valor) for valor in valores if valor.isdigit()]
        return [*numeros]
    if main_widget.de_ate_radioButton.isChecked():

        numeros = []  # Inicializa uma lista vazia para armazenar os números
        if main_widget.de_ate_radioButton.isChecked():
            n_maior = max(int(main_widget.de_Edit.text()), int(main_widget.ate_Edit.text()))
            n_menor = min(int(main_widget.de_Edit.text()), int(main_widget.ate_Edit.text()))
            for n in range(n_menor, n_maior+1):
            # for n in range(int(self.de_Edit.text()), int(self.ate_Edit.text())+1):
                    numeros.append(n)
        return numeros