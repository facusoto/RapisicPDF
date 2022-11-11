import csv
import re
import sys

import PyPDF2
from crear_imagen import *

class Meta:
    def __init__(self):
        pass

    def pdf_read(self):
    # PDF read work
        for infile in sys.argv[1:]:
            try:
                pdfFileObj = open(infile, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                pageObj = pdfReader.getPage(0)
                text = pageObj.extractText()
                text = text.replace("AMOC", "")

            except Exception as e:
                print(e)

            finally:
                pdfFileObj.close()

        # Data obtaining
            try:
                found_user = re.compile(r'\b\d{12}\b')
                found_barcode = re.compile(r'\b\d{20}\b')

            except AttributeError:
                print('Error, tarjeta no encontrada')

            for user, barcode in zip(re.finditer(found_user, text), re.finditer(found_barcode, text)):
                self.img_getter(user.group(0), barcode.group(0))

    def img_getter(self, user, bardoce):
        img_creator = Img()
        img_creator.creator(user, bardoce)

if __name__ == '__main__':
    init = Meta()
    init.pdf_read()