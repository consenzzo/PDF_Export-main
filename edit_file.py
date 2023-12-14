from menu2_ui import Ui_Menu
from PySide6.QtWidgets import QMessageBox, QListWidgetItem
from PySide6.QtGui import QPixmap, QIcon, QTransform
from PySide6.QtCore import QByteArray, QBuffer, QIODevice, QSize, Qt, Slot
import base64
from icon_button import icon_button
from convert import base64_to_pdf, pdf_to_base64, img_to_pdf, scale_image, word_to_pdf, pdf_to_word
import fitz  # PyMuPDF
import os
from display import  display_image
from dialog import search_watermark
from pathlib import Path
from typing import Union, Literal, List
from decimal import Decimal
from PIL import Image, ImageEnhance
import math
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, generic
from reportlab.lib.colors import Color  # Adicionado para lidar com cores e transparência
import shutil


def delete_selected_page(self:Ui_Menu):
    selected_row = self.listWidget.currentRow()

    if selected_row >= 0:
        
        confirmation = QMessageBox.question(
            self, 'Confirmar Exclusão',
            'Tem certeza de que deseja excluir esta página?',
            QMessageBox.Yes | QMessageBox.No
        )
        

        if confirmation == QMessageBox.Yes:
            # Remover a página selecionada do QListWidget
            self.listWidget.takeItem(selected_row)

            # Remover a página correspondente do dicionário de ícones
            for page, data in list(self.icon_dict.items()):
                if int(data["atual"]) == selected_row + 1:
                    del self.icon_dict[page]
                    break  # Saímos do loop assim que a página for encontrada e removida

            # Atualizar os números das páginas restantes
            for page, data in self.icon_dict.items():
                if int(data["atual"]) > selected_row + 1:
                    data["atual"] = str(int(data["atual"]) - 1)

            total_page = len(self.icon_dict)
            self.n_pg_total.setText(f'/ {total_page}')
            item_row = self.listWidget.count()
            if item_row == 0:
                    for label_name, icon_data in icon_button.items():
                        if label_name == "display":
                            base64_image = icon_data["base64_data"]
                            image_data = base64.b64decode(base64_image)
                            # Cria um QPixmap a partir da imagem decodificada
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                            icon = QIcon(pixmap)
                            # Obtém o QLabel pelo nome e define o ícone
                            label = getattr(self, label_name)  # Obtém o QLabel pelo nome
                            label.setPixmap(pixmap)
                            self.n_pg_edit.setText("")
            else:
                self.listWidget.setCurrentRow(selected_row - 1)
            
    else:
        QMessageBox.warning(self, 'Aviso', 'Nenhuma página selecionada para exclusão.')


def rotate_image_r(self:Ui_Menu):
    rotate_img(self, 90)


def rotate_image_l(self:Ui_Menu):
    rotate_img(self, -90)

def rotate_img(self:Ui_Menu, degrees):
    page_current = self.listWidget.currentRow() + 1
    current_item = self.listWidget.currentItem()
    for page, data in self.icon_dict.items():
        current = int(data['atual'])
        if current == page_current:
            base64 = self.icon_dict[page]["base64_pdf"]
            local_file = base64_to_pdf(base64,"temp_rotate_page.pdf")
            pdf_document = fitz.open(local_file)
            for pagina_index in range(pdf_document.page_count):
                pagina = pdf_document[pagina_index]
                current_angle = self.icon_dict[page]["rotate"]
                current_angle = (current_angle + degrees) % 360
                pagina.set_rotation(current_angle)
                self.icon_dict[page]["rotate"] = current_angle


            # Salva as alterações no novo arquivo PDF
            pdf_document.save("temp_rotate_page.pdf")
            new_page = pdf_document.load_page(pagina_index)
            img_bytes = new_page.get_pixmap()
            img_bytes = img_bytes.tobytes()

            # Fecha o arquivo PDF
            pdf_document.close()
            os.remove(local_file)

            new_base64 = pdf_to_base64("temp_rotate_page.pdf",0)
            os.remove("temp_rotate_page.pdf")
            self.icon_dict[page]["base64_pdf"] = new_base64
            self.icon_dict[page]["icon_bytes"] = img_bytes
            
            # Atualize diretamente o ícone do item atual na QListWidget
            pixmap = QPixmap()
            pixmap.loadFromData(img_bytes)
            pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
            current_item.setIcon(QIcon(pixmap))
            current_item.setSizeHint(QSize(pixmap.size()))
            display_image(self)


def move_page_up(self:Ui_Menu):
    initial_position = self.listWidget.currentRow()
    if initial_position == 0:
        pass
    else:
        initial_position += 1
        final_position = initial_position - 1
        move_page(self, initial_position, final_position)



def move_page_down(self:Ui_Menu):
    initial_position = self.listWidget.currentRow()
    if initial_position == self.listWidget.count() - 1:
        pass
    else:
        initial_position += 1
        final_position = initial_position + 1
        move_page(self, initial_position, final_position)



def move_page(self:Ui_Menu, initial_position, final_position):

    if initial_position != final_position:
        for page, data in self.icon_dict.items():
            current_position = int(data["atual"])

            if current_position == initial_position:
                data["atual"] = str(final_position)
            elif initial_position < final_position:
                if initial_position < current_position <= final_position:
                    data["atual"] = str(current_position - 1)
            else:
                if final_position <= current_position < initial_position:
                    data["atual"] = str(current_position + 1)

        sort_list_widget(self, final_position)

def sort_list_widget(self:Ui_Menu, final_position):
    # Limpe a listWidget
    self.listWidget.setCurrentRow(-1)
    self.listWidget.clear()
    
    new_dict = dict(sorted(self.icon_dict.items(), key=lambda x: x[1]['atual']))

    for page, data in new_dict.items():
        pixmap = QPixmap()
        pixmap.loadFromData(data["icon_bytes"])
        list_item = QListWidgetItem()
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        list_item.setIcon(QIcon(pixmap))
        list_item.setSizeHint(QSize(pixmap.size()))  # Defina o tamanho desejado
        self.listWidget.addItem(list_item)
    self.listWidget.setCurrentRow(final_position-1)

@Slot(int, int)
def on_dropped(self:Ui_Menu, initial, final):
    # print(f"Item da linha {initial} foi arrastado para linha {final}")
    move_page(self, initial, final)



def add_watermark(self: Ui_Menu):

    watermark_path_search = search_watermark(self)


    for item_data in self.icon_dict.values():
        watermark_path = watermark_path_search
        self.listWidget.setCurrentRow(int(item_data["atual"]) - 1)
        current_item = self.listWidget.currentItem()
        base64_pdf = item_data["base64_pdf"]
        local_pdf = base64_to_pdf(base64_pdf,watermark_path)
        pdf_document = fitz.open(local_pdf)
        page_pdf = pdf_document[0]
        current_width_pt, current_height_pt = page_pdf.rect.width, page_pdf.rect.height
        pdf_document.close()
        size_watermark = scale_image(self, watermark_path, current_width_pt, current_height_pt)
        if size_watermark:
            watermark_path = size_watermark
        watermark_path_white_clear = os.path.join(os.path.dirname(watermark_path), f"{os.path.splitext(os.path.basename(watermark_path))[0]}temp_WATERMARK_clear_.png")
        watermark_path = remover_fundo_branco(watermark_path,watermark_path_white_clear)
        watermark_pdf = create_watermark_pdf(watermark_path)
        base64_watermark = pdf_to_base64(watermark_pdf,0)
        item_data["watermark_base64_pdf"] = base64_watermark
        # os.remove(local_img_pdf)
        watermark(local_pdf,watermark_pdf,'pdf_opacity_temp.pdf','ALL')
        os.remove(local_pdf)
        os.remove(watermark_path_white_clear)
        os.remove(watermark_pdf)
        try:
            os.remove(size_watermark)
        except:
            pass
        new_pdf = pdf_to_base64('pdf_opacity_temp.pdf',0)
        self.icon_dict[int(item_data["atual"])]["base64_pdf"] = new_pdf

        # Salva as alterações no novo arquivo PDF
        pdf_document = fitz.open('pdf_opacity_temp.pdf')
        new_page = pdf_document.load_page(0)
        img_bytes = new_page.get_pixmap()
        img_bytes = img_bytes.tobytes()

        # Fecha o arquivo PDF
        pdf_document.close()

        self.icon_dict[int(item_data["atual"])]["icon_bytes"] = img_bytes
        
        # Atualize diretamente o ícone do item atual na QListWidget
        pixmap = QPixmap()
        pixmap.loadFromData(img_bytes)
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        
        current_item.setIcon(QIcon(pixmap))
        current_item.setSizeHint(QSize(pixmap.size()))
        os.remove('pdf_opacity_temp.pdf')
        display_image(self)





def create_watermark_pdf(watermark_image_path):

    # Criar PDF da marca d'água
    watermark_pdf_path = os.path.join(os.path.dirname(watermark_image_path), f"{os.path.splitext(os.path.basename(watermark_image_path))[0]}_WATERMARK_.pdf")
    c = canvas.Canvas(watermark_pdf_path)

    # Definir o valor alfa para transparência (0 é totalmente transparente, 1 é totalmente opaco)
    valor_alfa = 0.5  # Ajuste esse valor conforme necessário
    branco_transparente = Color(1, 1, 1, alpha=valor_alfa)

    # Desenhar a imagem com transparência
    c.setFillColor(branco_transparente)
    c.drawImage(watermark_image_path, 170, 300, 250, 250, mask='auto')

    c.save()

    return watermark_pdf_path

        
def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    reader_stamp = PdfReader(stamp_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()

    for index in page_indices:
        content_page = reader.pages[index]
        stamp_page = reader_stamp.pages[index]

        

        # Load the stamp PDF for each page
        reader_stamp = PdfReader(stamp_pdf)

         # Use o tamanho total da folha como referência
        content_width = float(content_page.mediabox[2] - content_page.mediabox[0])
        content_height = float(content_page.mediabox[3] - content_page.mediabox[1])


        stamp_width = float(stamp_page.mediabox[2] - stamp_page.mediabox[0])
        stamp_height = float(stamp_page.mediabox[3] - stamp_page.mediabox[1])


        print(f'content_width: {content_width} / content_height: {content_height}')
        print(f'stamp_width: {stamp_width}  /  stamp_height: {stamp_height}')

        proporcao_content = (content_width, content_height)
        largura_stamp, altura_stamp = stamp_width, stamp_height
        # escala_1 = calcular_escala(proporcao_content, largura_stamp, altura_stamp)
        # print(f"A escala necessária é: {escala_1}")

                
        image_page = reader_stamp.pages[0]
        # image_page.scale_by(escala_1)
        


        # largura_content, altura_content = content_width, content_height
        # largura_stamp, altura_stamp = stamp_width * escala_1, stamp_height * escala_1
        # new_ctm = calcular_ctm(largura_content, altura_content, largura_stamp, altura_stamp)

        ctm = [1, 0, 0, 1, 1, 1]
        # ctm = new_ctm

        image_page.add_transformation(ctm)
        
        content_page.merge_page(image_page)

        

        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
    



def calcular_escala(proporcao_content, largura_stamp, altura_stamp):
    largura_content, altura_content = proporcao_content


    escala_largura = largura_content / largura_stamp
    escala_altura = altura_content / altura_stamp


    # Escolhe a escala mínima para manter a proporção original
    escala = min(escala_largura, escala_altura)

    escala = round(escala)

    return escala

def calcular_ctm(largura_content, altura_content, largura_stamp, altura_stamp):
    # Calcula os offsets para centralizar a marca d'água
    offset_x = (largura_content - largura_stamp) / 2
    offset_y = (altura_content - altura_stamp) / 2
    if offset_x < 0:
        offset_x = 0
    if offset_y < 0:
        offset_y = 0

    # Retorna os valores da matriz de transformação
    return [1, 0, 0, 1, offset_x, offset_y]


def remover_fundo_branco(caminho_da_imagem, caminho_da_saida):
    # Abre a imagem
    imagem = Image.open(caminho_da_imagem)

    # Converte a imagem para o modo RGBA (se ainda não estiver no modo RGBA)
    imagem = imagem.convert("RGBA")
    dados = imagem.getdata()

    # Define um valor de limiar para considerar como branco
    limiar_branco = 200

    nova_lista = []
    for item in dados:
        # Verifica se o pixel é branco (considerando um limiar)
        if item[0] > limiar_branco and item[1] > limiar_branco and item[2] > limiar_branco:
            # Torna o pixel completamente transparente
            nova_lista.append((0, 0, 0, 0))
        else:
            nova_lista.append(item)

    imagem.putdata(nova_lista)

    # Salva a imagem sem o fundo branco
    imagem.save(caminho_da_saida, "PNG")
    return caminho_da_saida


def remove_watermark(self: Ui_Menu):
    for item_data in self.icon_dict.values():
        self.listWidget.setCurrentRow(int(item_data["atual"]) - 1)
        current_item = self.listWidget.currentItem()
        # base64_dict = item_data["base64_pdf"]
        pdf_file = base64_to_pdf(item_data["base64_pdf"],'temp_base_pdfwater_export.pdf')
         # Tenta remover a marca d'água usando remove_watermark_type01
        remove_watermark_type01_success = remove_watermark_type01(pdf_file, 'temp_output_export_water.pdf')
        # Se remove_watermark_type01 não removeu nada, chama remove_watermark_type02
        if not remove_watermark_type01_success:
            
            remove_watermark_type02_success = remove_watermark_type02(pdf_file, 'temp_output_export_water.pdf')

            if not remove_watermark_type02_success:
                shutil.copy(pdf_file, 'temp_output_export_water.pdf')
                new_pdf = 'temp_output_export_water.pdf'
            else:
                pdf_to_word(self, 'temp_output_export_water.pdf', 'temp_output_export_water.docx')
                new_pdf = word_to_pdf(self, 'temp_output_export_water.docx')
        else:
            new_pdf = 'temp_output_export_water.pdf'

        base64_new_pdf = pdf_to_base64(new_pdf,0)
        self.icon_dict[int(item_data["atual"])]["watermark_base64_pdf"] = None
        self.icon_dict[int(item_data["atual"])]["base64_pdf"] = base64_new_pdf

        # Salva as alterações no novo arquivo PDF
        pdf_document = fitz.open(new_pdf)
        new_page = pdf_document.load_page(0)
        img_bytes = new_page.get_pixmap()
        img_bytes = img_bytes.tobytes()

        # Fecha o arquivo PDF
        pdf_document.close()

        self.icon_dict[int(item_data["atual"])]["icon_bytes"] = img_bytes
        
        # Atualize diretamente o ícone do item atual na QListWidget
        pixmap = QPixmap()
        pixmap.loadFromData(img_bytes)
        pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
        
        current_item.setIcon(QIcon(pixmap))
        current_item.setSizeHint(QSize(pixmap.size()))
        os.remove(new_pdf)
        try:
            os.remove('temp_output_export_water.docx')
        except:
            pass
        os.remove(pdf_file)
        display_image(self)



            
        




def remove_watermark_type02(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            x_objects = page['/Resources']['/XObject'].get_object() if '/XObject' in page['/Resources'] else {}

            # Lista para armazenar chaves (nomes) dos objetos a serem removidos
            objects_to_remove = []

            for obj in x_objects:
                if x_objects[obj]['/Subtype'] == '/Image':
                    image_info = x_objects[obj]

                    # Verificar se o filtro é ['/ASCII85Decode', '/FlateDecode']
                    filters = x_objects[obj]['/Filter'] if '/Filter' in x_objects[obj] else []
                    has_correct_filter = filters == ['/ASCII85Decode', '/FlateDecode']

                    # Verificar se a máscara de transparência está presente e é indireta
                    has_smask = '/SMask' in x_objects[obj]
                    smask_is_indirect = isinstance(x_objects[obj].get('/SMask'), generic.IndirectObject)

                    if has_correct_filter and (not has_smask or (has_smask and smask_is_indirect)):
                        print(f"Page {page_num + 1}, Image Object {obj}: {image_info}")
                        objects_to_remove.append(obj)

            # Remover objetos XObject da página
            for obj_key in objects_to_remove:
                page['/Resources']['/XObject'].pop(obj_key)

            pdf_writer.add_page(page)

        if len(objects_to_remove) == 0:
            return False
        
        else:

            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            return True


def remove_watermark_type01(input_pdf, output_pdf):
    is_watermark = False
    # Abrir o documento PDF
    doc = fitz.open(input_pdf)

    # Iterar sobre as páginas do PDF
    for page_number in range(doc.page_count):
        page = doc[page_number]

        # Padronizar os objetos da página /Contents
        page.clean_contents()

        # Obter o xref do objeto /Contents resultante após a padronização
        xref = page.get_contents()[0]
        
        # Ler o conteúdo fonte como um bytearray (objeto de array de bytes modificável)
        cont = bytearray(page.read_contents())
        # print(cont)

        # Confirmar a presença de uma marca d'água do tipo "marked-content watermark"
        if cont.find(b"/Subtype/Watermark") > 0:
            print(f"Marca d'água encontrada na página {page_number + 1}")

            # Loop para remover todas as ocorrências de marcas d'água
            while True:
                i1 = cont.find(b"/Artifact")  # Encontrar o início da definição da marca d'água
                if i1 < 0:
                    break  # Se não encontrar mais ocorrências, encerrar o loop

                i2 = cont.find(b"EMC", i1)  # Encontrar o final da definição da marca d'água
                cont[i1 - 2 : i2 + 3] = b""  # Remover a definição completa da marca d'água ("q ... EMC")
                is_watermark = True
            # Atualizar o stream com o conteúdo modificado
            doc.update_stream(xref, cont)

            # Salvar o documento resultante em um novo arquivo
            doc.save(output_pdf)
            doc.close()
            return is_watermark
    return is_watermark
    