# linear equations with two variables

import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/1_pair_of_equation_latex/pair_of_equation/'
tex_name = 'pair'

caption_path = '../20_generate_textual_description/pair_of_equation/'
caption_name = 'pair_equn_image_caption'

latex_path = '../21_generate_latex_description/pair_of_equation/'
latex_name = 'pair_equn_latex_description'

if not os.path.exists(caption_path):
    os.makedirs(caption_path)
    
caption_string1 = os.path.join(caption_path, caption_name)
caption_string1 = caption_string1+'.txt' 

mode = 'a+' if os.path.exists(caption_string1) else 'w+'
f2 = open(caption_string1, mode)

if not os.path.exists(latex_path):
    os.makedirs(latex_path)
latex_string1 = os.path.join(latex_path, latex_name)
latex_string1 = latex_string1+'.txt'
mode = 'a+' if os.path.exists(latex_string1) else 'w+'
f3 = open(latex_string1, mode)

total_no = 0

variable_list =['x','y','z', 't']       
name_variable_list =['x','y','z','t']   
length_variable_list = len(variable_list)

operator_list1 = ['','-']
name_operator_list1 = ['', 'minus'] 
length_operator_list1 =len(operator_list1)

operator_list2 = ['+','-']
name_operator_list2 = ['plus', 'minus'] 
length_operator_list2 =len(operator_list2)

operator_list3 = ['','-']
name_operator_list3 = ['', 'minus'] 
length_operator_list3 =len(operator_list3)

operator_list4 = ['','-']
name_operator_list4 = ['', 'minus'] 
length_operator_list4 =len(operator_list4)

operator_list5 = ['+','-']
name_operator_list5 = ['plus', 'minus'] 
length_operator_list5 =len(operator_list5)

operator_list6 = ['','-']
name_operator_list6 = ['', 'minus'] 
length_operator_list6 =len(operator_list6)

operator_list7 = ['+','-']
name_operator_list7 = ['plus', 'minus'] 
length_operator_list7 =len(operator_list7)

operator_list8 = ['+','-']
name_operator_list8 = ['plus', 'minus'] 
length_operator_list8 =len(operator_list8)

operator_list9 = ['','-']
name_operator_list9 = ['', 'minus'] 
length_operator_list9 =len(operator_list9)

operator_list10 = ['','-']
name_operator_list10 = ['', 'minus'] 
length_operator_list10 =len(operator_list10)

constant_list1 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list1 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list1 =len(constant_list1)

constant_list2 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list2 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list2 =len(constant_list2)

constant_list3 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list3 = [' one ',' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list3 =len(constant_list3)

constant_list4 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list4 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list4 =len(constant_list4)

constant_list5 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list5 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list5 =len(constant_list5)

constant_list6 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list6 = [' one ',' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list6 =len(constant_list6)

constant_list7 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list7 = [' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list7 =len(constant_list7)

constant_list8 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list8 = [' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list8 =len(constant_list8)

constant_list9 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list9 = [' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list9 =len(constant_list9)

constant_list10 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list10 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list10 =len(constant_list10)

constant_list11 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list11 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list11 =len(constant_list11)

constant_list12 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list12 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list12 =len(constant_list12)

constant_list13 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list13 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list13 =len(constant_list13)

#############################################################################
for i in range(length_variable_list): # different types of variables
    for j in range(i, length_variable_list, 1):
        if i!=j:
            a = r'\scalebox{4.0}'      #4.0
            for k in range(18):        #18
                for p in range (500):   #500
                    #write into tex file 
                    tex_string1 = os.path.join(tex_path,tex_name)
                    tex_string1 = tex_string1+"_"+str(total_no)+'.tex'
                    f = open(tex_string1,"w+")
                    string1 = tex_name+"_"+str(total_no)+".png"
                    f2.write(string1)
                    f2.write("\t")

                    docu_class = '\documentclass[12pt]{article}'
                    eqnarray = r'\usepackage{eqnarray}' 
                    asmath =r'\usepackage{amsmath}'
                    color =r'\usepackage{xcolor}'
                    graphics =r'\usepackage{graphicx}'
                    begin_docu =r'\begin{document}'
                    end_docu =r'\end{document}' 
                    f.write(docu_class)
                    f.write('\n')
                    f.write(eqnarray)
                    f.write('\n')
                    f.write(asmath)
                    f.write('\n')
                    f.write(graphics)
                    f.write('\n')
                    f.write(begin_docu)
                    f.write('\n')

                    variable_index1 = i  
                    variable_index2 = j

                    operator_index1 = random.randint(0, length_operator_list1-1)
                    operator_index2 = random.randint(0, length_operator_list2-1)
                    operator_index3 = random.randint(0, length_operator_list3-1)
                    operator_index4 = random.randint(0, length_operator_list4-1)
                    operator_index5 = random.randint(0, length_operator_list5-1)
                    operator_index6 = random.randint(0, length_operator_list6-1)
                    operator_index7 = random.randint(0, length_operator_list7-1)
                    operator_index8 = random.randint(0, length_operator_list8-1)
                    operator_index9 = random.randint(0, length_operator_list9-1)
                    operator_index10 = random.randint(0, length_operator_list10-1)
                    
                    constant_index1 = random.randint(0, length_constant_list1-1)   
                    constant_index2 = random.randint(0, length_constant_list2-1)
                    constant_index3 = random.randint(0, length_constant_list3-1)
                    constant_index4 = random.randint(0, length_constant_list4-1)
                    constant_index5 = random.randint(0, length_constant_list5-1)
                    constant_index6 = random.randint(0, length_constant_list6-1)
                    constant_index7 = random.randint(0, length_constant_list7-1)
                    constant_index8 = random.randint(0, length_constant_list8-1)
                    constant_index9 = random.randint(0, length_constant_list9-1)
                    constant_index10 = random.randint(0, length_constant_list10-1)
                    constant_index11 = random.randint(0, length_constant_list11-1)
                    constant_index12 = random.randint(0, length_constant_list12-1)
                    constant_index13 = random.randint(0, length_constant_list13-1)
 
 
 
                    var1 = variable_list[variable_index1]
                    var2 = variable_list[variable_index2]

                    cons1 = constant_list1[constant_index1]
                    cons2 = constant_list2[constant_index2]
                    cons3 = constant_list3[constant_index3]
                    cons4 = constant_list4[constant_index4]
                    cons5 = constant_list5[constant_index5]
                    cons6 = constant_list6[constant_index6]
                    cons7 = constant_list7[constant_index7]
                    cons8 = constant_list8[constant_index8]
                    cons9 = constant_list9[constant_index9]
                    cons10 = constant_list10[constant_index10]
                    cons11 = constant_list11[constant_index11]
                    cons12 = constant_list12[constant_index12]
                    cons13 = constant_list13[constant_index13]

                    opr1  = operator_list1[operator_index1]
                    opr2  = operator_list2[operator_index2]
                    opr3  = operator_list3[operator_index3]
                    opr4  = operator_list4[operator_index4]
                    opr5  = operator_list5[operator_index5]
                    opr6  = operator_list6[operator_index6]
                    opr7  = operator_list7[operator_index7]
                    opr8  = operator_list8[operator_index8]
                    opr9  = operator_list9[operator_index9]
                    opr10  = operator_list10[operator_index10]

                  
                    name_var1 = name_variable_list[variable_index1]
                    name_var2 = name_variable_list[variable_index2] 

                    name_cons1 = name_constant_list1[constant_index1]
                    name_cons2 = name_constant_list2[constant_index2]
                    name_cons3 = name_constant_list3[constant_index3]
                    name_cons4 = name_constant_list4[constant_index4]
                    name_cons5 = name_constant_list5[constant_index5]
                    name_cons6 = name_constant_list6[constant_index6]
                    name_cons7 = name_constant_list7[constant_index7]
                    name_cons8 = name_constant_list8[constant_index8]
                    name_cons9 = name_constant_list9[constant_index9]
                    name_cons10 = name_constant_list10[constant_index10]
                    name_cons11 = name_constant_list11[constant_index11]
                    name_cons12 = name_constant_list12[constant_index12]
                    name_cons13 = name_constant_list13[constant_index13]

                    name_opr1 = name_operator_list1[operator_index1]
                    name_opr2 = name_operator_list2[operator_index2]
                    name_opr3 = name_operator_list3[operator_index3]
                    name_opr4 = name_operator_list4[operator_index4]
                    name_opr5 = name_operator_list5[operator_index5]
                    name_opr6 = name_operator_list6[operator_index6]
                    name_opr7 = name_operator_list7[operator_index7]
                    name_opr8 = name_operator_list8[operator_index8]
                    name_opr9 = name_operator_list9[operator_index9]
                    name_opr10 = name_operator_list10[operator_index10]

                    ###########################################################################################
                    if k == 0: # 10 eqn +-ax +- by = +-c
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1>'1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 1: # 9 eqn +-ax +- by +-c = 0
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to zero and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 2: # 1-1 eqn +-ax +- by = +-c and +-ax = +-c
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr4+cons4+var1+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1>'1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 3: # 1-2 eqn +-ax +- by +-c =0 and +-ax +-c = 0
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr4+cons4+var1+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to zero and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n") 
                    ###########################################################################################
                    if k == 4: # 2-1 eqn +-ax +- by = +-c and +-by = +-c
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr10+cons5+var2+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr10+cons5+var2+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1>'1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr10 == '-':
                            f2.write(" ")
                            f2.write(name_opr10)
                        if cons5 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 5: # 2-2 eqn +-ax +- by +-c = 0 and +-by +-c = 0
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+opr7+cons3+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr10+cons5+var2+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr10+cons5+var2+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to zero and")
                        if opr10 == '-':
                            f2.write(" ")
                            f2.write(name_opr10)
                        if cons5 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 6: # 3-1 eqn +-ax = +-c and +-ax +- by = +-c 
                        b1=r'{$'+opr1+cons1+var1+'='+opr3+cons3+'$}'
                        z1 = '$'+opr1+cons1+var1+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1>'1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 7: # 3-1 eqn +-ax +-c = 0 and +-ax +- by +-c = 0
                        b1=r'{$'+opr1+cons1+var1+opr7+cons3+'= 0'+'$}'
                        z1 = '$'+opr1+cons1+var1+opr7+cons3+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to zero and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 8: # 4-1 eqn +- by = +-c and +-ax +- by = +-c
                        b1=r'{$'+opr9+cons2+var2+'='+opr3+cons3+'$}'
                        z1 = '$'+opr9+cons2+var2+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr9)
                        if opr9 == '-':
                            f2.write(" ")
                        f2.write(name_cons2)
                        if cons2>'1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n") 
                    ###########################################################################################
                    if k == 9: # 4-2 eqn +- by +-c = 0 and +-ax +- by +-c = 0
                        b1=r'{$'+opr9+cons2+var2+opr7+cons3+'= 0'+'$}'
                        z1 = '$'+opr9+cons2+var2+opr7+cons3+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr4+cons4+var1+opr5+cons5+var2+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr9)
                        if opr9 == '-':
                            f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to zero and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons5)
                        if cons5 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n") 
                    ###########################################################################################
                    if k == 10: # 5-1 eqn +-ax +-c = +-by and +-ax = +-c
                        b1=r'{$'+opr1+cons1+var1+opr2+cons3+'='+opr3+cons2+var2+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons3+'='+opr3+cons2+var2+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr4+cons4+var1+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1>'1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(name_cons3)
                        f2.write("equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        if cons2 > '1':
                            f2.write(" ")   
                        f2.write(name_cons2)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 11: # 5-2 eqn eqn +-ax +-c = +-by and +-ax +-c = 0
                        b1=r'{$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$}'
                        z1 = '$'+opr1+cons1+var1+opr2+cons2+var2+'='+opr3+cons3+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr4+cons4+var1+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr4+cons4+var1+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons2)
                        if cons2 > '1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(name_cons3)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        if cons4 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons4)
                        f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")  
                    ###########################################################################################
                    if k == 12: # 6-1 eqn +- by +-c = +-ax and +-by = +-c
                        b1=r'{$'+opr9+cons2+var2+opr7+cons3+'='+opr1+cons1+var1+'$}'
                        z1 = '$'+opr9+cons2+var2+opr7+cons3+'='+opr1+cons1+var1+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr10+cons5+var2+'='+opr6+cons6 +'$}'
                        z2 = '$'+ opr10+cons5+var2+'='+opr6+cons6 +'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr9)
                        if opr9 == '-':
                            f2.write(" ")
                        f2.write(name_cons2)
                        if cons2>'1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to")
                        if opr1 == '-':
                            f2.write(" ")
                            f2.write(name_opr1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_cons1)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" and")
                        if opr10 == '-':
                            f2.write(" ")
                            f2.write(name_opr10)
                        if cons5 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(name_cons6)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 13: # 6-2 eqn +- by +-c = +-ax and +-by +-c = 0
                        b1=r'{$'+opr9+cons2+var2+opr7+cons3+'='+opr1+cons1+var1+'$}'
                        z1 = '$'+opr9+cons2+var2+opr7+cons3+'='+opr1+cons1+var1+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+ opr10+cons5+var2+opr8+cons6+'= 0'+'$}'
                        z2 = '$'+ opr10+cons5+var2+opr8+cons6+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr9)
                        if opr9 == '-':
                            f2.write(" ")
                        f2.write(name_cons2)
                        if cons2>'1':
                            f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(name_cons3)
                        f2.write("equal to")
                        if opr1 == '-':
                            f2.write(" ")
                            f2.write(name_opr1)
                        if cons1 > '1':
                            f2.write(" ")
                        f2.write(name_cons1)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" and")
                        if opr10 == '-':
                            f2.write(" ")
                            f2.write(name_opr10)
                        if cons5 > '1':    
                            f2.write(" ")    
                        f2.write(name_cons5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(name_cons6)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 14: #  eqn +-a/x +- b/y = 1/+-c
                        b1=r'{$'+opr1+r'\frac{'+ cons10 +'}{'+ var1 +'}'+opr2+r'\frac{'+ cons11 +'}{'+ var2 +'}'+'='+opr3+r'\frac{'+str(1)+'}{'+cons9+'}'+'$}'
                        z1 = '$'+opr1+r'\frac{'+ cons10 +'}{'+ var1 +'}'+opr2+r'\frac{'+ cons11 +'}{'+ var2 +'}'+'='+opr3+r'\frac{'+str(1)+'}{'+cons9+'}'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+opr4+r'\frac{'+ cons12 +'}{'+ var1 +'}'+opr5+r'\frac{'+ cons13 +'}{'+ var2 +'}'+'='+opr6+r'\frac{'+str(1)+'}{'+cons7+'}'+'$}'
                        z2 = '$'+opr4+r'\frac{'+ cons12 +'}{'+ var1 +'}'+opr5+r'\frac{'+ cons13 +'}{'+ var2 +'}'+'='+opr6+r'\frac{'+str(1)+'}{'+cons7+'}'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons10)
                        f2.write(" over ")
                        f2.write(name_var1)
                        f2.write(" all ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons11)
                        f2.write(" over ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(" one over")
                        f2.write(name_cons9)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        f2.write(" ")    
                        f2.write(name_cons12)
                        f2.write(" over ")
                        f2.write(name_var1)
                        f2.write(" all ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons13)
                        f2.write(" over ")
                        f2.write(name_var2)
                        f2.write(" equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(" one over")
                        f2.write(name_cons7)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 15: #  eqn +-a/x +- b/y  1/+-c =0
                        b1=r'{$'+opr1+r'\frac{'+ cons10 +'}{'+ var1 +'}'+opr2+r'\frac{'+ cons11 +'}{'+ var2 +'}'+opr7+r'\frac{'+str(1)+'}{'+cons9+'}'+'= 0'+'$}'
                        z1 = '$'+opr1+r'\frac{'+ cons10 +'}{'+ var1 +'}'+opr2+r'\frac{'+ cons11 +'}{'+ var2 +'}'+opr7+r'\frac{'+str(1)+'}{'+cons9+'}'+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+opr4+r'\frac{'+ cons12 +'}{'+ var1 +'}'+opr5+r'\frac{'+ cons13 +'}{'+ var2 +'}'+opr8+r'\frac{'+str(1)+'}{'+cons7+'}'+'= 0'+'$}'
                        z2 = '$'+opr4+r'\frac{'+ cons12 +'}{'+ var1 +'}'+opr5+r'\frac{'+ cons13 +'}{'+ var2 +'}'+opr8+r'\frac{'+str(1)+'}{'+cons7+'}'+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_cons10)
                        f2.write(" over ")
                        f2.write(name_var1)
                        f2.write(" all ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_cons11)
                        f2.write(" over ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr7)
                        f2.write(" one over")
                        f2.write(name_cons9)
                        f2.write("equal to zero ")
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        f2.write(" ")    
                        f2.write(name_cons12)
                        f2.write(" over ")
                        f2.write(name_var1)
                        f2.write(" all ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_cons13)
                        f2.write(" over ")
                        f2.write(name_var2)
                        f2.write(" ")
                        f2.write(name_opr8)
                        f2.write(" one over")
                        f2.write(name_cons7)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 16: #  eqn +-x/a +- y/b = 1/+-c
                        b1=r'{$'+opr1+r'\frac{'+ var1 +'}{'+ cons7 +'}'+opr2+r'\frac{'+ var2 +'}{'+ cons8 +'}'+'='+opr3+r'\frac{'+str(1)+'}{'+cons9+'}'+'$}'
                        z1 = '$'+opr1+r'\frac{'+ var1 +'}{'+ cons7 +'}'+opr2+r'\frac{'+ var2 +'}{'+ cons8 +'}'+'='+opr3+r'\frac{'+str(1)+'}{'+cons9+'}'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+opr4+r'\frac{'+ var1 +'}{'+ cons8 +'}'+opr5+r'\frac{'+ var2 +'}{'+ cons9 +'}'+'='+opr6+r'\frac{'+str(1)+'}{'+cons7+'}'+'$}'
                        z2 = '$'+opr4+r'\frac{'+ var1 +'}{'+ cons8 +'}'+opr5+r'\frac{'+ var2 +'}{'+ cons9 +'}'+'='+opr6+r'\frac{'+str(1)+'}{'+cons7+'}'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" over")
                        f2.write(name_cons7)
                        f2.write("all ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" over")
                        f2.write(name_cons8)
                        f2.write("equal to")
                        if opr3 == '-':
                            f2.write(" ")
                            f2.write(name_opr3)
                        f2.write(" one over")
                        f2.write(name_cons9)
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        f2.write(" ")    
                        f2.write(name_var1)
                        f2.write(" over")
                        f2.write(name_cons8)
                        f2.write("all ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" over")
                        f2.write(name_cons9)
                        f2.write("equal to")
                        if opr6 == '-':
                            f2.write(" ")
                            f2.write(name_opr6)
                        f2.write(" one over")
                        f2.write(name_cons7)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")
                    ###########################################################################################
                    if k == 17: #  eqn +-x/a +- y/b +-1/c = 0
                        b1=r'{$'+opr1+r'\frac{'+ var1 +'}{'+ cons7 +'}'+opr2+r'\frac{'+ var2 +'}{'+ cons8 +'}'+opr7+r'\frac{'+str(1)+'}{'+cons9+'}'+'= 0'+'$}'
                        z1 = '$'+opr1+r'\frac{'+ var1 +'}{'+ cons7 +'}'+opr2+r'\frac{'+ var2 +'}{'+ cons8 +'}'+opr7+r'\frac{'+str(1)+'}{'+cons9+'}'+'= 0'+'$'
                        c = r'\\'+r'\\'+r'\\'
                        b2=r'{$'+opr4+r'\frac{'+ var1 +'}{'+ cons8 +'}'+opr5+r'\frac{'+ var2 +'}{'+ cons9 +'}'+opr8+r'\frac{'+str(1)+'}{'+cons7+'}'+'= 0'+'$}'
                        z2 = '$'+opr4+r'\frac{'+ var1 +'}{'+ cons8 +'}'+opr5+r'\frac{'+ var2 +'}{'+ cons9 +'}'+opr8+r'\frac{'+str(1)+'}{'+cons7+'}'+'= 0'+'$'

                        d = a+b1+c+a+b2
                        latex = z1+c+z2

                        f2.write(name_opr1)
                        if opr1 == '-':
                            f2.write(" ")
                        f2.write(name_var1)
                        f2.write(" over")
                        f2.write(name_cons7)
                        f2.write("all ")
                        f2.write(name_opr2)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" over")
                        f2.write(name_cons8)
                        f2.write("all ")
                        f2.write(name_opr7)
                        f2.write(" one over")
                        f2.write(name_cons9)
                        f2.write("equal to zero ")
                        f2.write("and")
                        if opr4 == '-':
                            f2.write(" ")
                            f2.write(name_opr4)
                        f2.write(" ")    
                        f2.write(name_var1)
                        f2.write(" over")
                        f2.write(name_cons8)
                        f2.write("all ")
                        f2.write(name_opr5)
                        f2.write(" ")
                        f2.write(name_var2)
                        f2.write(" over")
                        f2.write(name_cons9)
                        f2.write("all ")
                        f2.write(name_opr8)
                        f2.write(" one over")
                        f2.write(name_cons7)
                        f2.write("equal to zero")
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                        f3.write(latex)
                        f3.write("\n")
                        f3.write("\n")

f2.close()  
f3.close()  
  
      




                       


   
              
   
                           
                            

                    


                       


     
      
