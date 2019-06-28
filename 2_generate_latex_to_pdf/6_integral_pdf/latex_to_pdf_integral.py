import os
import os.path
import sys
import glob
import shutil

latex_path = '../../1_generate_latex_files/6_integral_latex/integral/'
a = "pdflatex "
a1 =" rm -rf "

for file_name in os.listdir(latex_path):
    if file_name.endswith('.tex'):
        f1 = file_name.split('.')
        f2 = f1[0]
        f3 = f1[1]
        if f3 == "tex":
            print("file_name", file_name)
            b = os.path.join(latex_path,file_name)
            c = a+b
            os.system(c)
            
            # remove .ps, .aux, .log, .dvi files 

            f11 = f1[0]+".ps"
            f12 = f1[0]+".aux"
            f13 = f1[0]+".log"
            f14 = f1[0]+".dvi"
        
            fa1 = a1+f11
            fa2 = a1+f12
            fa3 = a1+f13
            fa4 = a1+f14
            
            os.system(fa1)
            os.system(fa2)
            os.system(fa3)
            os.system(fa4)







    
	 	 

