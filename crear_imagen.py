import urllib.request
import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

class Img:
    def __init__(self):
        pass

    def creator(self, user, barcode):
        # Obtención de las columnas como variables
        tarjeta = str(user)
        barcode = str(barcode)
        # En el caso del código se concatena una url para acceder a la imagen
        codigo = "http://img.cajadepagos.com/pagospyme/barcodes/genbarcode.php?cad=" + barcode

        # Se hace una request de la imágen desde PagosPyme y se la guarda con su nombre en formato PNG
        urllib.request.urlretrieve(codigo, barcode + ".png")

        # Apertura de las imagenes
        img = Image.open(barcode + ".png")
        im1 = Image.open(open("C:\\Users\\Facu\\Desktop\\Code\\RapisicPDF\\Images\\header.png", mode='rb'))
        im3 = Image.open(open("C:\\Users\\Facu\\Desktop\\Code\\RapisicPDF\\Images\\footer.png", mode='rb'))

        # Definición del nuevo tamaño del código de barras
        new_width = 434
        new_height = 100

        # Conversión de la imagen del código de barras a RGB, reescalado y filtrado
        im2 = img.convert('RGB').resize((new_width, new_height), Image.NEAREST).filter(ImageFilter.EDGE_ENHANCE)

        # Funcion creadora de la imagen
        def get_concat_v(im1, im2, im3, color=(255, 255, 255)):
            # Creación de la imagen, ancha como im1, alto 434, blanca
            dst = Image.new('RGB', (im1.width, 434), color)
            # Pega la img Header
            dst.paste(im1, (0, 0))

            # Variable escritura
            d = ImageDraw.Draw(dst)
            myFont = ImageFont.truetype(r'C:\\Users\\Facu\\AppData\\Local\\Microsoft\\Windows\\Fonts\\CircularStd-Bold.ttf', 40)
            # Escribe el texto de la columna tarjeta de esa celda
            d.text((228, 132), tarjeta ,(51, 51, 51), font=myFont)

            # Pega la img Codigo de barras
            dst.paste(im2, (133, im1.height + 10))
            ds = ImageDraw.Draw(dst)
            myFont2 = ImageFont.truetype(r'C:\\Users\\Facu\\AppData\\Local\\Microsoft\\Windows\\Fonts\\CircularStd-Book.ttf', 27)
            # Escribe el texto de la columna codigo de esa celda
            ds.text((205, 306), barcode ,(51, 51, 51), font=myFont2)
            
            # Pega la img footer
            dst.paste(im3, (0, im1.height + 190))
            # Tras finalizar, devuelve el resultado de dst como valor de la funcion
            return dst

        # Realiza la funcion que genera la imagen y la guarda, nombrandola como el numero de la linea
        get_concat_v(im1, im2, im3).save('Tarjeta - ' + str(user) + ".png")
        os.remove(barcode + ".png")