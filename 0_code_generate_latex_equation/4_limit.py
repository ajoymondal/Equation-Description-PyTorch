# limit equation

import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/4_limit_latex/limit/'
tex_name = 'limit'

caption_path = '../20_generate_textual_description/limit/'
caption_name = 'limit_image_caption'

latex_path = '../21_generate_latex_description/limit/'
latex_name = 'limit_latex_description'

if not os.path.exists(caption_path):
    os.makedirs(caption_path)
caption_string1 = os.path.join(caption_path, caption_name)
caption_string1 = caption_string1+'.txt' 
f2 = open(caption_string1,"w+")

if not os.path.exists(latex_path):
    os.makedirs(latex_path)
latex_string1 = os.path.join(latex_path, latex_name)
latex_string1 = latex_string1+'.txt'
f3 = open(latex_string1,"w+")

total_no = 0

variable_list =['x','z','t', 'y']       
name_variable_list =['x','z','t','y']   
length_variable_list = len(variable_list)

function_list = ['sin\ ', 'cos\ ', 'tan\ ', 'sec\ ', 'cosec\ ', 'cot\ ']
name_function_list = ['sin', 'cos', 'tan', 'sec', 'cosec', 'cot']
length_function_list = len(function_list)

operator_list1 = ['','-']
name_operator_list1 = ['', 'minus'] 
length_operator_list1 =len(operator_list1)

operator_list2 = ['+','-']
name_operator_list2 = ['plus', 'minus'] 
length_operator_list2 =len(operator_list2)

operator_list3 = ['+','-']
name_operator_list3 = ['plus', 'minus'] 
length_operator_list3 =len(operator_list3)

operator_list4 = ['','-']
name_operator_list4 = ['', 'minus'] 
length_operator_list4 = len(operator_list4)

operator_list5 = ['+','-']
name_operator_list5 = ['plus', 'minus'] 
length_operator_list5 = len(operator_list5)

operator_list6 = ['+','-']
name_operator_list6 = ['plus', 'minus'] 
length_operator_list6 = len(operator_list6)

constant_list1 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list1 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list1 =len(constant_list1)

constant_list2 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list2 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list2 =len(constant_list2)

constant_list3 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list3 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list3 =len(constant_list3)

constant_list4 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list4 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list4 =len(constant_list4)

constant_list5 = ['','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list5 = ['','two times', 'three times', 'four times', 'five times', 'six times', 'seven times','eight times', 'nine times', 'ten times']  
length_constant_list5 =len(constant_list5)

constant_list6 = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
name_constant_list6 = ['one','two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_constant_list6 =len(constant_list6)

power_list = ['a^{2}', 'b^{2}', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100']
name_power_list = [' a square ', ' b square ', ' one ', ' four ', ' nine ', ' sixteen ',' tweenty five ', ' thirty six ', ' fourty nine ',' sixty four ', ' eighty one ', ' hundred ']  
length_power_list = len(power_list)

root_list = ['\sqrt{a}', '\sqrt{b}', '1',  '\sqrt{2}', '\sqrt{3}', '\sqrt{4}', '\sqrt{5}', '\sqrt{6}', '\sqrt{7}', '\sqrt{8}', '\sqrt{9}', '\sqrt{10}']
name_root_list = [' secnd root of a ', ' second root of b ', ' one ', ' second root of two ', ' second root of three ', ' second root of four ', ' second root of five ', 
                       ' second root of six ', ' second root of seven ',' second root of eight ', ' second root of nine ', ' second root of ten ']  
length_root_list =len(root_list) 

limit_constant_list1 = ['a', 'b', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
name_limit_constant_list1 = ['a', 'b', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_limit_constant_list1 =len(limit_constant_list1)

limit_constant_list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
name_limit_constant_list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_limit_constant_list2 =len(limit_constant_list2)

limit_constant_list3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
name_limit_constant_list3 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']  
length_limit_constant_list3 =len(limit_constant_list3)

limit_operator_list = ['', '+', '-']
name_limit_operator_list = ['limit', 'right hand limit', 'left hand limit']
length_limit_operator_list = len(limit_operator_list)

#############################################################################
for i in range (length_variable_list): # different types of variables
    for j in range (length_limit_operator_list):
        a = r'\scalebox{4.0}'
        for k in range(57): #57
            for p in range (100): #100
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

                variable_index = i 
                limit_operator_index = j 
                
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
                
                function_index = random.randint(0, length_function_list-1)
                power_index = random.randint(0, length_power_list-1)
                root_index = random.randint(0, length_root_list-1) 
                
                limit_constant_index1 = random.randint(0, length_limit_constant_list1-1) 
                limit_constant_index2 = random.randint(0, length_limit_constant_list2-1) 
                limit_constant_index3 = random.randint(0, length_limit_constant_list3-1) 

                var1 = variable_list[variable_index]
                fun = function_list[function_index]

                cons1 = constant_list1[constant_index1]
                cons2 = constant_list2[constant_index2]
                cons3 = constant_list3[constant_index3]
                cons4 = constant_list4[constant_index4]
                cons5 = constant_list5[constant_index5]
                cons6 = constant_list6[constant_index6]
                
                opr1  = operator_list1[operator_index1]
                opr2  = operator_list2[operator_index2]
                opr3  = operator_list3[operator_index3]
                opr4  = operator_list4[operator_index4]
                opr5  = operator_list5[operator_index5]
                opr6  = operator_list6[operator_index6]
                
                power = power_list[power_index]
                root = root_list[root_index]
                limit_cons1 = limit_constant_list1[limit_constant_index1]
                limit_cons2 = limit_constant_list2[limit_constant_index2]
                limit_cons3 = limit_constant_list3[limit_constant_index3]

                limit_opr = limit_operator_list[limit_operator_index]
                                    
                name_var1 = name_variable_list[variable_index]
                name_fun = name_function_list[function_index]
                
                name_cons1 = name_constant_list1[constant_index1]
                name_cons2 = name_constant_list2[constant_index2]
                name_cons3 = name_constant_list3[constant_index3]
                name_cons4 = name_constant_list4[constant_index4]
                name_cons5 = name_constant_list5[constant_index5]
                name_cons6 = name_constant_list6[constant_index6]
                
                name_opr1 = name_operator_list1[operator_index1]
                name_opr2 = name_operator_list2[operator_index2]
                name_opr3 = name_operator_list3[operator_index3]
                name_opr4 = name_operator_list4[operator_index4]
                name_opr5 = name_operator_list5[operator_index5]
                name_opr6 = name_operator_list6[operator_index6]

                name_power = name_power_list[power_index]
                name_root  =  name_root_list[root_index]
                name_limit_cons1 = name_limit_constant_list1[limit_constant_index1]
                name_limit_cons2 = name_limit_constant_list2[limit_constant_index2]
                name_limit_cons3 = name_limit_constant_list3[limit_constant_index3]

                name_limit_opr = name_limit_operator_list[limit_operator_index]
                
                power_name_limit_cons = name_limit_constant_list1[power_index]
                power_limit_cons = limit_constant_list1[power_index]

                root_limit_cons = limit_constant_list1[root_index]
                root_name_limit_cons = name_limit_constant_list1[root_index]

###########################################################################################
                if k == 0: # lim ax2 +-bx +-c / dx2+-ex+-f
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
                if k == 1: # lim ax2 +-bx +-c / +-dx+-f
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+opr4+cons4+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+opr4+cons4+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
###########################################################################
                if k == 2: # lim  +-bx +-c / dx2+-ex+-f
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+opr3+cons3 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+opr3+cons3 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#######################################################################
                if k == 3: # lim +-c+-bx+-ax2/+-dx2+-ex+-f
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    if cons3 > '1':
                        f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#################################################################################
                if k == 4: # lim ax2 +-bx +-c / +-d+-ex+-fx2
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4=='-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#################################################################################
                if k == 5: # lim +-c +-bx +-ax2 / +-d+-ex+-fx2
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}' +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")    
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4=='-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#######################################################################
                if k == 6: # lim +-c+-bx+-ax2/+-dx+-e
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons4+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons4+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    if cons3 > '1':
                        f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
################################################################################################
                if k == 7: # lim ax2 +-bx +-c / +-d+-fx
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+opr4+cons6+opr6+cons4+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+'^{2}'+opr2+cons2+var1+opr3+cons3 +'}{'+opr4+cons6+opr6+cons4+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    #if cons4 > '1':
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#######################################################################
                if k == 8: # lim +-c+-bx+-ax2/+-d+-fx
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons6+opr6+cons4+var1 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr2+cons2+var1+opr3+cons1+var1+'^{2}'+'}{'+ opr4+cons6+opr6+cons4+var1 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    if cons3 > '1':
                        f2.write(" ")
                    f2.write(name_opr2)
                    f2.write(" ")
                    f2.write(name_cons2)
                    if cons2 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
###########################################################################
                if k == 9: # lim  +-b +-cx / dx2+-ex+-f
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr3+cons1+var1 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr3+cons1+var1 +'}{'+ opr4+cons4+var1+'^{2}'+opr5+cons5+var1+opr6+cons6 +'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    #if cons1 > '1':
                    f2.write(" ")
                    #f2.write(name_var1)
                    #f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4 == '-':
                        f2.write(" ")
                    f2.write(name_cons4)
                    if cons4 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#################################################################################
                if k == 10: # lim +-ax +-c / +-d+-ex+-fx2
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+opr3+cons3 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons1+var1+opr3+cons3 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4=='-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#################################################################################
                if k == 11: # lim +-c +-ax / +-d+-ex+-fx2
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr3+cons1+var1 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ limit_cons3+'^{' + limit_opr+ '}}'+ r'\frac{'+opr1+cons3+opr3+cons1+var1 +'}{'+ opr4+cons6+opr5+cons5+var1+opr6+cons4+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_opr1)
                    if opr1 == '-':
                        f2.write(" ")
                    f2.write(name_cons3)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_cons1)
                    if cons1 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")   
                    f2.write(name_opr4)
                    if opr4=='-':
                        f2.write(" ")
                    f2.write(name_cons6)
                    f2.write(" ")
                    f2.write(name_opr5)
                    f2.write(" ")
                    f2.write(name_cons5)
                    if cons5 > '1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_cons4)
                    if cons4>'1':
                        f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(name_limit_cons3)
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
#################################################################################
                if k == 12: # lim x2 +-a2 / x+-a
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+opr3+power+'}{'+var1+opr6+power_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+opr3+power+'}{'+var1+opr6+power_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("all over ")   
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(power_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 13: # lim x2 +-a2 / a+-x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+opr3+power+'}{'+power_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+opr3+power+'}{'+power_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("all over ")   
                    f2.write(power_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 14: # lim a2 +-x2 / a+-x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+opr3+var1+'^{2}'+'}{'+power_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+opr3+var1+'^{2}'+'}{'+power_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write("all over ")   
                    f2.write(power_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 15: # lim a2 +-x2 / x+-a
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+opr3+var1+'^{2}'+'}{'+var1+opr6+power_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+opr3+var1+'^{2}'+'}{'+var1+opr6+power_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write("all over ") 
                    f2.write(name_var1)  
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(power_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 16: # lim  x+-a/x2 +-a2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+power_limit_cons+'}{'+var1+'^{2}'+opr3+power+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+power_limit_cons+'}{'+var1+'^{2}'+opr3+power+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(power_name_limit_cons)
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 17: # lim  a+-x/x2 +-a2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power_limit_cons+opr6+var1+'}{'+var1+'^{2}'+opr3+power+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power_limit_cons+opr6+var1+'}{'+var1+'^{2}'+opr3+power+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(power_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 18: # lim  x+-a/a2 +-x2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+power_limit_cons+'}{'+power+opr3+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+power_limit_cons+'}{'+power+opr3+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(power_name_limit_cons)
                    f2.write(" all over")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")                
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 19: # lim  a+-x/a2 +-x2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power_limit_cons+opr6+var1+'}{'+power+opr3+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power_limit_cons+opr6+var1+'}{'+power+opr3+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(power_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")                
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 20: # lim  x^{1/2}+-a^{1/2}/x +-a 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+opr3+root+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+opr3+root+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(name_root)
                    f2.write("all over ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 21: # lim  x^{1/2}+-a^{1/2}/a+-x 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+opr3+root+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+opr3+root+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(name_root)
                    f2.write("all over ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 22: # lim  a^{1/2}+-x^{1/2}/x +-a 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+opr3+r'\sqrt{'+var1+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+opr3+r'\sqrt{'+var1+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_root)           
                    f2.write(name_opr3)
                    f2.write(" second root of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 23: # lim  a^{1/2}+-x^{1/2}/a +-x 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+opr3+r'\sqrt{'+var1+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+opr3+r'\sqrt{'+var1+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_root)           
                    f2.write(name_opr3)
                    f2.write(" second root of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 24: # lim  x +-a / x^{1/2}+-a^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(name_root)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 25: # lim  a +-x / x^{1/2}+-a^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(name_root)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 26: # lim  x +-a / a^{1/2}+-x^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over")
                    f2.write(name_root)
                    f2.write(name_opr6)
                    f2.write(" second root of ") 
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 27: # lim  a +-x / a^{1/2}+-x^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr3+root_limit_cons+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over")
                    f2.write(name_root)
                    f2.write(name_opr6)
                    f2.write(" second root of ") 
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 28: # lim (x +-a)^{1/2} / x+-a
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")   
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 29: # lim (x +-a)^{1/2} / a+-x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")   
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 30: # lim (a +-x)^{1/2} / a+-x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of all ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")   
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 31: # lim (a +-x)^{1/2} / x+-a
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of all ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(name_var1)   
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 32: # lim  x+-a/(x +-a)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+root_limit_cons+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+root_limit_cons+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 33: # lim  a+-x/(x +-a)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+opr6+var1+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+opr6+var1+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 34: # lim  x+-a/(a +-x)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+root_limit_cons+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+opr6+root_limit_cons+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 35: # lim  a+-x/(a +-x)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+opr6+var1+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+opr6+var1+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 36: # lim  x/(x +-a)
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)                              
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 37: # lim  x/(a +-x)
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)                              
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 38: # lim  a/(x +-a)
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+var1+opr6+root_limit_cons+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+var1+opr6+root_limit_cons+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)                              
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 39: # lim  a/(a +-x)
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+root_limit_cons+opr6+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+root_limit_cons+opr6+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_limit_cons)
                    f2.write(" all over ")
                    f2.write(root_name_limit_cons)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(" ")
                    f2.write(name_var1)                              
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 40: # lim  x2/x2 +-a2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+'}{'+var1+'^{2}'+opr3+power+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+'}{'+var1+'^{2}'+opr3+power+'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 41: # lim  x2/a2 +-x2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+'}{'+power+opr3+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'^{2}'+'}{'+power+opr3+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" square")
                    f2.write(" all over")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")                        
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 42: # lim  a2/x2 +-a2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+'}{'+var1+'^{2}'+opr3+power+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+'}{'+var1+'^{2}'+opr3+power+'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_power)
                    f2.write("all over ")
                    f2.write(name_var1)
                    f2.write(" square ")
                    f2.write(name_opr3)
                    f2.write(name_power)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 43: # lim  a2/a2 +-x2 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+'}{'+power+opr3+var1+'^{2}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ power_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+power+'}{'+power+opr3+var1+'^{2}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1
                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_power)
                    f2.write("all over")
                    f2.write(name_power)
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" square ")                        
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(power_name_limit_cons)
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
#################################################################################
                if k == 44: # lim  x^{1/2} / x^{1/2}+-a^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of ")
                    f2.write(name_var1)
                    f2.write(" all over second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(name_root)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 45: # lim  x^{1/2} / a^{1/2}+-x^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+r'\sqrt{'+var1+'}'+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of second root of ")
                    f2.write(name_var1)
                    f2.write(" all over")
                    f2.write(name_root)
                    f2.write(name_opr6)
                    f2.write(" second root of ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 46: # lim  a^{1/2} / x^{1/2}+-a^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+'}{'+r'\sqrt{'+var1+'}'+opr6+root+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_root)
                    f2.write("all over second root of ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr6)
                    f2.write(name_root)
                    f2.write("as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 47: # lim  a^{1/2} / a^{1/2}+-x^{1/2}/ 
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root+'}{'+root+opr6+r'\sqrt{'+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of")
                    f2.write(name_root)
                    f2.write("all over")
                    f2.write(name_root)
                    f2.write(name_opr6)
                    f2.write(" second root of ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 48: # lim  x/(x +-a)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 49: # lim  x/(a +-x)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+var1+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(root_name_limit_cons)  
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)       
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 50: # lim  a/(x +-a)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+r'\sqrt{'+var1+opr3+root_limit_cons+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(name_var1)
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(root_name_limit_cons)         
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 51: # lim  a/(a +-x)^{1/2}
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ root_limit_cons+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'}{'+r'\sqrt{'+root_limit_cons+opr3+var1+'}'+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all over ")
                    f2.write("second root of all ")
                    f2.write(root_name_limit_cons)  
                    f2.write(" ")
                    f2.write(name_opr3)
                    f2.write(" ")
                    f2.write(name_var1)       
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to ")
                    f2.write(root_name_limit_cons)
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
#################################################################################
                if k == 52: # lim  sin x/ x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'sin'+'\ '+var1 +'}{'+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'sin'+'\ '+var1+'}{'+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of sin ")
                    f2.write(name_var1)
                    f2.write(" over ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to zero")
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
#################################################################################
                if k == 53: # lim  exp (x)-1/ x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'e^{'+var1+'}-1' +'}{'+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'e^{'+var1+'}-1'+'}{'+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of exponential of ")
                    f2.write(name_var1)
                    f2.write(" all minus one")
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to zero")
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
#################################################################################
                if k == 54: # lim a^x-1/ x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'^{'+var1+'}-1' +'}{'+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+root_limit_cons+'^{'+var1+'}-1'+'}{'+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of ")
                    f2.write(name_var1)
                    f2.write(" power of ")
                    f2.write(root_name_limit_cons)
                    f2.write(" all minus one")
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to zero")
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
#################################################################################
                if k == 55: # lim  exp (sinx)-1/ x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'e^{'+fun+var1+'}-1' +'}{'+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'e^{'+fun+var1+'}-1'+'}{'+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of exponential of ")
                    f2.write(name_fun)
                    f2.write(" ")
                    f2.write(name_var1)
                    f2.write(" all minus one")
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to zero")
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
#################################################################################
                if k == 56: # lim  log (x+1)/ x
                    b1 = r'{$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'\ln('+var1+'+1)'+'}{'+var1+'}'+ '$}'
                    z1 = '$'+ r'\displaystyle \lim_{'+var1+r'\to '+ '0'+'^{' + limit_opr+ '}}'+ r'\frac{'+'\ln('+var1+'+1)'+'}{'+var1+'}'+ '$'
                    
                    d = a+b1
                    latex = z1

                    f2.write(name_limit_opr)
                    f2.write(" of natural logarthmic of all ")
                    f2.write(name_var1)
                    f2.write(" plus one")
                    f2.write(" all over ")
                    f2.write(name_var1)
                    f2.write(" as ")
                    f2.write(name_var1)
                    f2.write(" approaches to zero")
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
      




                       


   
              
   
                           
                            

                    


                       


     
      
