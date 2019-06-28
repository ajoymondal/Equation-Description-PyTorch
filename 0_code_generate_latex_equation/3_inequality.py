# linear equations with two variables

import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/3_inequality_latex/inequality/'
tex_name = 'inequality'

caption_path = '../20_generate_textual_description/inequality/'
caption_name = 'inequality_image_caption'

latex_path = '../21_generate_latex_description/inequality/'
latex_name = 'inequality_latex_description'

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

function_list = ['<','\leq ', '>', '\geq ']
name_function_list = [' less than ', ' less than or equal to ', ' greater than ', ' greater than or equal to ']
length_function_list =len(function_list)

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
length_operator_list4 = len(operator_list4)

operator_list5 = ['+','-']
name_operator_list5 = ['plus', 'minus'] 
length_operator_list5 = len(operator_list5)

operator_list6 = ['','-']
name_operator_list6 = ['', 'minus'] 
length_operator_list6 = len(operator_list6)

constant_list1 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list1 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list1 =len(constant_list1)

constant_list2 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list2 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list2 =len(constant_list2)

constant_list3 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list3 = ['two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten'] 
length_constant_list3 =len(constant_list3)

constant_list4 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list4 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list4 =len(constant_list4)

constant_list5 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list5 = [' one ',' two ', ' three ', ' four ', ' five ', ' six ', ' seven ',' eight ', ' nine ', ' ten ']  
length_constant_list5 =len(constant_list5)

constant_list6 = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list6 = ['two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list6 =len(constant_list6)

constant_list7 = ['0','1' ,'2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list7 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list7 =len(constant_list7)

#############################################################################
for i in range (length_variable_list): # different types of variables
    for j in range (i, length_function_list):
        a = r'\scalebox{4.0}'
        for k in range(1): #15
            for p in range (1): #600
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
                function_index = j 
                
                operator_index1 = random.randint(0, length_operator_list1-1)
                operator_index2 = random.randint(0, length_operator_list2-1)
                operator_index3 = random.randint(0, length_operator_list3-1)
                operator_index4 = random.randint(0, length_operator_list4-1)
                operator_index5 = random.randint(0, length_operator_list5-1)
                operator_index6 = random.randint(0, length_operator_list6-1)
                            
                constant_index1 = random.randint(0, length_constant_list1-1)   
                constant_index2 = random.randint(0, length_constant_list2-1)
                constant_index3 = random.randint(0, length_constant_list3-1)
                constant_index4 = random.randint(0, length_constant_list4-1)
                constant_index5 = random.randint(0, length_constant_list5-1)
                constant_index6 = random.randint(0, length_constant_list6-1)
                constant_index7 = random.randint(0, length_constant_list7-1)
            
                var1 = variable_list[variable_index1]
                fun = function_list[function_index]

                cons1 = constant_list1[constant_index1]
                cons2 = constant_list2[constant_index2]
                cons3 = constant_list3[constant_index3]
                cons4 = constant_list4[constant_index4]
                cons5 = constant_list5[constant_index5]
                cons6 = constant_list6[constant_index6]
                cons7 = constant_list7[constant_index7]
                
                opr1  = operator_list1[operator_index1]
                opr2  = operator_list2[operator_index2]
                opr3  = operator_list3[operator_index3]
                opr4  = operator_list4[operator_index4]
                opr5  = operator_list5[operator_index5]
                opr6  = operator_list6[operator_index6]
                                    
                name_var1 = name_variable_list[variable_index1]
                name_fun = name_function_list[function_index]
                
                name_cons1 = name_constant_list1[constant_index1]
                name_cons2 = name_constant_list2[constant_index2]
                name_cons3 = name_constant_list3[constant_index3]
                name_cons4 = name_constant_list4[constant_index4]
                name_cons5 = name_constant_list5[constant_index5]
                name_cons6 = name_constant_list6[constant_index6]
                name_cons7 = name_constant_list7[constant_index7]
            
                name_opr1 = name_operator_list1[operator_index1]
                name_opr2 = name_operator_list2[operator_index2]
                name_opr3 = name_operator_list3[operator_index3]
                name_opr4 = name_operator_list4[operator_index4]
                name_opr5 = name_operator_list5[operator_index5]
                name_opr6 = name_operator_list6[operator_index6]
                
                ###########################################################################################
                if k == 0: # eqn +-ax <> +- b 
                    b1=r'{$'+opr1+cons1+var1+fun+opr4+cons7+'$}'
                    z1 = '$'+opr1+cons1+var1+fun+opr4+cons7+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
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
                if k == 1: # eqn +-b <> +-ax 
                    b1=r'{$'+opr4+cons7+fun+opr1+cons1+var1+'$}'
                    z1 = '$'+opr4+cons7+fun+opr1+cons1+var1+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons7)
                    f2.write(name_fun)
                    if opr1 == '-':
                        f2.write(name_opr1)
                        f2.write(" ")
                    f2.write(name_cons1)    
                    if cons1>'1':
                        f2.write(" ")
                    f2.write(name_var1)    
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
                if k == 2: # eqn +-ax +- b <> +-c 
                    b1=r'{$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons7+'$}'
                    z1 = '$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons7+'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
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
                if k == 3: # eqn +-c <> +-ax +- b 
                    b1=r'{$'+opr4+cons7+fun+opr1+cons1+var1+opr2+cons2+'$}'
                    z1 = '$'+opr4+cons7+fun+opr1+cons1+var1+opr2+cons2+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons7)
                    f2.write(name_fun)
                    if opr1 == '-':
                        f2.write(name_opr1)
                        f2.write(" ")
                    f2.write(name_cons1)    
                    if cons1>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
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
                if k == 4: # eqn +-ax +- b <> +-cx 
                    b1=r'{$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons4+var1+'$}'
                    z1 = '$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons4+var1+'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write(name_cons4)
                    f2.write(" ")
                    f2.write(name_var1)
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
                if k == 5: # eqn +-cx <> +-ax +- b 
                    b1=r'{$'+opr4+cons4+var1+fun+opr1+cons1+var1+opr2+cons2+ '$}'
                    z1 = '$'+opr4+cons4+var1+fun+opr1+cons1+var1+opr2+cons2+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(name_fun)
                    if opr1 == '-':
                        f2.write(name_opr1)
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
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
                if k == 6: # eqn +-ax +- b <> +-cx+-d 
                    b1=r'{$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons4+var1+opr5+cons5 +'$}'
                    z1 = '$'+opr1+cons1+var1+opr2+cons2+fun+opr4+cons4+var1+opr5+cons5 +'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write(name_cons4)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(name_cons5)
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
                if k == 7: # eqn +-ax +- b / +-c <> +-dx+-e /-+f
                    b1=r'{$'+r'\frac{'+opr1+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+r'\frac{'+opr4+cons4+var1+opr5+cons5+'}{'+opr6+cons6+'}' +'$}'
                    z1 = '$'+r'\frac{'+opr1+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+r'\frac{'+opr4+cons4+var1+opr5+cons5+'}{'+opr6+cons6+'}'+'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(" all over ")
                    f2.write(name_opr3)
                    if opr3 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write(name_cons4)
                    #f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(name_cons5)
                    f2.write("all over ")
                    f2.write(name_opr6)
                    if opr6 == '-':
                        f2.write(" ")
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
                if k == 8: # eqn +-ax +- b / +-c <> +-dx
                    b1=r'{$'+r'\frac{'+opr1+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+opr4+cons4+var1+'$}'
                    z1 = '$'+r'\frac{'+opr1+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+opr4+cons4+var1+'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(" all over ")
                    f2.write(name_opr3)
                    if opr3 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write(name_cons4)
                    f2.write(" ")
                    f2.write(name_var1)
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
                if k == 9: # eqn +-ax +- b / +-c <> +-d
                    b1=r'{$'+r'\frac{'+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+opr4+cons7+'$}'
                    z1 = '$'+r'\frac{'+opr1+cons1+var1+opr2+cons2+'}{'+ opr3+cons3+'}'+fun+opr4+cons7+'$'
                    
                    d = a+b1
                    latex = z1

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
                    f2.write(" all over ")
                    f2.write(name_opr3)
                    if opr3 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
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
                if k == 10: # eqn +-a/x <>+- 1/b 
                    b1=r'{$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$}'
                    z1 = '$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons2)
                    f2.write(" over ")
                    f2.write(name_var1)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write("one over ")    
                    f2.write(name_cons3)
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
                if k == 11: # eqn +-a/x +- 1/b <> +-1/c 
                    b1=r'{$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$}'
                    z1 = '$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons2)
                    f2.write(" over ")
                    f2.write(name_var1)
                    f2.write(" all ")
                    f2.write(name_opr2)
                    f2.write(" one over ")
                    f2.write(name_cons6)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write("one over ")    
                    f2.write(name_cons3)
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
                if k == 12: # eqn +-a/x +- 1/b <> +-d/x 
                    b1=r'{$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ cons2 +'}{'+ var1 +'}'+'$}'
                    z1 = '$'+opr1+r'\frac{'+cons2+'}{'+var1+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ cons2 +'}{'+ var1 +'}'+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons2)
                    f2.write(" over ")
                    f2.write(name_var1)
                    f2.write(" all ")
                    f2.write(name_opr2)
                    f2.write(" one over ")
                    f2.write(name_cons6)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write(name_cons2)    
                    f2.write(" over ")    
                    f2.write(name_var1)
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
                if k == 13: # eqn +-x/a <>+- 1/b 
                    b1=r'{$'+opr1+r'\frac{'+var1+'}{'+cons6+'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$}'
                    z1 = '$'+opr1+r'\frac{'+var1+'}{'+cons6+'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" over ")
                    f2.write(name_cons6)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write("one over ")    
                    f2.write(name_cons3)
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
                if k == 14: # eqn +-x/a +- 1/b <> +-1/c 
                    b1=r'{$'+opr1+r'\frac{'+var1+'}{'+cons3+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$}'
                    z1 = '$'+opr1+r'\frac{'+var1+'}{'+cons3+'}'+opr2+r'\frac{'+ str(1) +'}{'+ cons6 +'}'+fun+opr4+r'\frac{'+ str(1) +'}{'+ cons3 +'}'+'$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" over ")
                    f2.write(name_cons3)
                    f2.write(" all ")
                    f2.write(name_opr2)
                    f2.write(" one over ")
                    f2.write(name_cons6)
                    f2.write(name_fun)
                    if opr4 == '-':
                        f2.write(name_opr4)
                        f2.write(" ")
                    f2.write("one over ")    
                    f2.write(name_cons3)
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
      




                       


   
              
   
                           
                            

                    


                       


     
      