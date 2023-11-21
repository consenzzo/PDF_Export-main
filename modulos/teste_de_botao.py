import base64
import os
import json
dict_icon = {}

def encode_image_to_base64(file_path):
    with open(file_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')  # Converte bytes para string

def convert_directory_to_base64(directory):
    with open(os.path.join(directory, 'base64_files.txt'), 'w') as output_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.png'):  # Verifica se o arquivo é um PNG
                    file_path = os.path.join(root, file)
                    base64_data = encode_image_to_base64(file_path)
                    output_file.write(f"{file} = {base64_data}\n\n\n")
                    file_name, file_extension = os.path.splitext(file)
                    dict_temp = {
                                "base64_data":base64_data,
                                
                                   }
                    dict_icon[file_name] = dict_temp

def write_dict_to_file(directory):
    with open(os.path.join(directory,'base64_files_dict.txt'), 'w') as file:
        json.dump(dict_icon, file, indent=4)
    
    

# Substitua 'caminho/do/diretorio' pelo caminho do diretório que deseja percorrer
directory_path = r"C:\Users\gusta\OneDrive\Área de Trabalho\botoes"

convert_directory_to_base64(directory_path)
write_dict_to_file(directory_path)