from PIL import Image, ImageDraw
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QListWidget, QAbstractItemView, QFileDialog, QMessageBox, QInputDialog
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
import fitz  # PyMuPDF
from menu2_ui import Ui_Menu
from dict_validate import dict_validate
import check
import io
from display import display_image

# def apply_watermark_to_icon(icon_bytes, watermark_path):
#     # Carregar a imagem do ícone a partir dos bytes
#     icon_image = Image.open(io.BytesIO(icon_bytes)).convert("RGBA")

#     # Carregar a imagem da marca d'água
#     watermark_image = Image.open(watermark_path).convert("RGBA")

#     # Criar uma nova imagem para a marca d'água com a mesma dimensão do ícone
#     watermark_composite = Image.new("RGBA", icon_image.size, (0, 0, 0, 0))

#     # Calcular a posição para centralizar a marca d'água
#     x_offset = (icon_image.width - watermark_image.width) // 2
#     y_offset = (icon_image.height - watermark_image.height) // 2

#     # Colocar a marca d'água na posição calculada
#     watermark_composite.paste(watermark_image, (x_offset, y_offset), watermark_image)

#     # Combinar as duas imagens considerando a transparência
#     result_image = Image.alpha_composite(icon_image, watermark_composite)

#     # Salvar a imagem resultante de volta nos bytes
#     output_buffer = io.BytesIO()
#     result_image.save(output_buffer, format="PNG")
#     updated_icon_bytes = output_buffer.getvalue()

#     return updated_icon_bytes
# def apply_watermark_to_icon(icon_bytes, watermark_path, opacity=0.5):
#     # Carregar a imagem do ícone a partir dos bytes
#     icon_image = Image.open(io.BytesIO(icon_bytes)).convert("RGBA")

#     # Carregar a imagem da marca d'água
#     watermark_image = Image.open(watermark_path).convert("RGBA")

#     # Ajustar a opacidade da marca d'água
#     watermark_image_with_opacity = Image.new("RGBA", watermark_image.size)
#     for x in range(watermark_image.width):
#         for y in range(watermark_image.height):
#             r, g, b, a = watermark_image.getpixel((x, y))
#             watermark_image_with_opacity.putpixel((x, y), (r, g, b, int(a * opacity)))

#     # Criar uma nova imagem para a marca d'água com a mesma dimensão do ícone
#     watermark_composite = Image.new("RGBA", icon_image.size, (0, 0, 0, 0))

#     # Calcular a posição para centralizar a marca d'água
#     x_offset = (icon_image.width - watermark_image.width) // 2
#     y_offset = (icon_image.height - watermark_image.height) // 2

#     # Colocar a marca d'água na posição calculada
#     watermark_composite.paste(watermark_image_with_opacity, (x_offset, y_offset), watermark_image_with_opacity)

#     # Combinar as duas imagens considerando a transparência
#     result_image = Image.alpha_composite(icon_image, watermark_composite)

#     # Salvar a imagem resultante de volta nos bytes
#     output_buffer = io.BytesIO()
#     result_image.save(output_buffer, format="PNG")
#     updated_icon_bytes = output_buffer.getvalue()

#     return updated_icon_bytes
def apply_watermark_to_icon(icon_bytes, watermark_path):
    # Carregar a imagem do ícone a partir dos bytes
    icon_image = Image.open(io.BytesIO(icon_bytes)).convert("RGBA")

    # Carregar a imagem da marca d'água
    watermark_image = Image.open(watermark_path).convert("RGBA")

    # Criar uma nova imagem para a marca d'água com a mesma dimensão do ícone e transparência de 50%
    watermark_image_with_transparency = watermark_image.copy()
    watermark_image_with_transparency.putalpha(128)  # 128 é 50% de opacidade (0 é completamente transparente, 255 é completamente opaco)

    # Criar uma nova imagem para a marca d'água com a mesma dimensão do ícone
    watermark_composite = Image.new("RGBA", icon_image.size, (0, 0, 0, 0))

    # Calcular a posição para centralizar a marca d'água
    x_offset = (icon_image.width - watermark_image.width) // 2
    y_offset = (icon_image.height - watermark_image.height) // 2

    # Colocar a marca d'água na posição calculada
    watermark_composite.paste(watermark_image_with_transparency, (x_offset, y_offset), watermark_image_with_transparency)

    # Combinar as duas imagens considerando a transparência
    result_image = Image.alpha_composite(icon_image, watermark_composite)

    # Salvar a imagem resultante de volta nos bytes
    output_buffer = io.BytesIO()
    result_image.save(output_buffer, format="PNG")
    updated_icon_bytes = output_buffer.getvalue()

    return updated_icon_bytes


def update_icon_in_list(widget_item, icon_bytes):
    pixmap = QPixmap()
    pixmap.loadFromData(icon_bytes)
    pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
    widget_item.setIcon(QIcon(pixmap))
    widget_item.setSizeHint(QSize(pixmap.size()))

def add_watermark(self: Ui_Menu, sender):
    function_name = None
    if dict_validate[sender]["check"] is not None:
        name_check = dict_validate[sender]["check"]
        function_name = getattr(check, name_check)
        check_function = function_name(self)

    if dict_validate[sender]["check"] is None or check_function:
        # Abrir um diálogo para selecionar a imagem da marca d'água
        watermark_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem de Marca d'Água", "", "Imagens (*.png *.jpg *.jpeg)")

        # Definir a chave "watermark" para o caminho do arquivo escolhido em todo o dicionário
        for item_data in self.icon_dict.values():
            item_data["watermark"] = watermark_path

            # # Atualizar os bytes do ícone com a marca d'água
            item_data["icon_bytes"] = apply_watermark_to_icon(item_data["icon_bytes"], watermark_path)

            # Atualizar os bytes do ícone com a marca d'água e opacidade de 50%
            # item_data["icon_bytes"] = apply_watermark_to_icon(item_data["icon_bytes"], watermark_path, tra=0.5)

            # Atualizar o ícone na lista
            list_item = self.listWidget.item(int(item_data["atual"]) - 1)
            update_icon_in_list(list_item, item_data["icon_bytes"])
            display_image(self, "listWidget")
            




