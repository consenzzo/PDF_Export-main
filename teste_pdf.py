import PyPDF2
import base64

def salvar_pdf_como_codigo(pdf_path, codigo_path):
    with open(pdf_path, 'rb') as pdf_file:
        # Lê os bytes do arquivo PDF
        pdf_bytes = pdf_file.read()
        
        # Codifica os bytes para base64
        codigo_base64 = base64.b64encode(pdf_bytes)
        
        # Salva o código em um arquivo
        with open(codigo_path, 'wb') as codigo_file:
            codigo_file.write(codigo_base64)

def criar_pdf_a_partir_do_codigo(codigo_path, novo_pdf_path):
    # with open(codigo_path, 'rb') as codigo_file:
    #     # Lê o código base64 do arquivo
    codigo_base64 = codigo_path
    
    # Decodifica o código base64 para bytes
    pdf_bytes = base64.b64decode(codigo_base64)
    
    # Cria um novo arquivo PDF
    with open(novo_pdf_path, 'wb') as novo_pdf_file:
        novo_pdf_file.write(pdf_bytes)

# Exemplo de uso
pdf_path = r"C:\Users\gusta\OneDrive\Área de Trabalho\123testando.pdf"
novo_pdf_path = r"C:\Users\gusta\OneDrive\Área de Trabalho\NOVO.pdf"

# Salva o PDF como código
# salvar_pdf_como_codigo(pdf_path, codigo_path)

# Cria um novo PDF a partir do código
criar_pdf_a_partir_do_codigo(codigo_path, novo_pdf_path)