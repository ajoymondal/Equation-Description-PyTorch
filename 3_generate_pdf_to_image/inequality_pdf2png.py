import PyPDF2
from wand.image import Image
import io
import os
import glob
import cv2
import numpy as np
from PIL import Image as I

pdf_path ='../2_generate_latex_to_pdf/3_inequality_pdf/'
image_path = '3_inequality_pdf_to_image/'

if not os.path.exists(image_path):
    os.makedirs(image_path)

def pdf_page_to_png(src_pdf, pagenum = 0, resolution = 100):
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))
    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)
    img = Image(file = pdf_bytes, resolution = resolution)
    return img

for filename in os.listdir(pdf_path):
    if filename.endswith('.pdf'):
        print('filename',filename)
        r =filename.replace(".pdf","")
        
        full_name = os.path.join(pdf_path,filename)
        src_pdf = PyPDF2.PdfFileReader(full_name, "rb")
        no_page = src_pdf.getNumPages()
        for j in range (0, 1):
            img = pdf_page_to_png(src_pdf, pagenum = j, resolution = 100)
            file_name = r+".png"
            b = os.path.join(image_path,file_name)
            img.save(filename=b)
            img = cv2.imread(b)
            img_height, img_width, img_ch = img.shape
            act_image = np.zeros((img_height, img_width, 3), np.uint8)
            act_image = img
            act_image1 = I.fromarray(act_image)
            act_image1.save(b,'png') 
                    

                

