import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/6_integral_latex/integral/'
tex_name = 'integral'

caption_path = '../20_generate_textual_description/integral/'
caption_name = 'integral_image_caption'

total_no = 0
#1st one 
function_list =['arccos\ ','cos\ ', 'cosh\ ', 'sin\ ', 'arcsin\ ', 'sinh\ ', 'tan\ ', 'arctan\ ', 'tanh\ ',
                 'arcsec\ ', 'sec\ ', 'arccot\ ','cot\ ', 'coth\ ',  'arccosec\ ', 'cosec\ ', 'cosech\ ', 'cos^{-1}',
                'sin^{-1}', 'tan^{-1}', 'sec^{-1}', 'cot^{-1}', 'cosec^{-1}',
                'cosh^{-1}',
                'sinh^{-1}', 'tanh^{-1}', 'sech^{-1}', 'coth^{-1}', 'cosech^{-1}',
                'arccosh\ ', 'arcsinh\ ', 'arctanh\ ', 'arcsech\ ', 'arccoth\ ', 'arccosech\ ']

name_function_list = ['inverse cos', 'cos', 'hyperbolic cos', 'sin', 'inverse sin', 'hyperbolic sin', 
                       'tan', 'inverse tan', 'hyperbolic tan', 
                       'inverse sec', 'sec', 'hyperbolic sec', 
                       'inverse cot', 'cot', 'hyperbolic cot', 'inverse cosec', 'cosec', 'hyperbolic cosec',
                       'inverse cos', 'inverse sin', 'inverse tan', 'inverse sec', 'inverse cot', 'inverse cosec',
                       'inverse hyperbolic cos', 'inverse hyperbolic sin', 'inverse hyperbolic tan', 
                       'inverse hyperbolic sec', 'inverse hyperbolic cot', 'inverse hyperbolic cosec',
                       'inverse hyperbolic cos', 'inverse hyperbolic sin', 'inverse hyperbolic tan', 
                       'inverse hyperbolic sec', 'inverse hyperbolic cot', 'inverse hyperbolic cosec']

function_list1 =['cos\ ', 'cosh\ ', 'sin\ ', 'sinh\ ', 'tan\ ', 'tanh\ ',
                 'sec\ ', 'cot\ ', 'coth\ ',  'cosec\ ', 'cosech\ ']

name_function_list1 = ['cos', 'hyperbolic cos', 'sin', 'hyperbolic sin', 
                       'tan', 'hyperbolic tan', 'sec', 'hyperbolic sec', 
                       'cot', 'hyperbolic cot', 'cosec', 'hyperbolic cosec']

variable_list =['x','z','t','y','\\theta']       
name_variable_list =['x','z','t','y','theta']       
operator_list = ['+', '-']
name_operator_list = ['plus', 'minus']   

operator_list1 = ['', '-']
name_operator_list1 = ['', 'minus']  

power_list = ['1', 'a^{2}', 'b^{2}', '4', '9', '16', 
              '25', '36', '49', '64', '81', '100']
name_power_list = [' one ', ' a square ', ' b square ', ' four ',
                    ' nine ', ' sixteen ', ' tweenty five ', 
                    ' thirty six ', ' fourty nine ', ' sixty four ',
                    ' eighty one ', ' hundred ']

constant_list = ['1', 'a', 'b', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
name_constant_list = [' one ', ' a ', ' b ', ' two ', ' three ', 
                      ' four ', ' five ', ' six ', ' seven ', 
                      ' eight ', ' nine ', ' ten ']   

length_function_list = len(function_list)
length_variable_list = len(variable_list) 
length_operator_list = len(operator_list)
length_function_list1 = len(function_list1)
length_power_list = len(power_list)
length_constant_list = len(constant_list)
length_operator_list1 = len(operator_list1)

if not os.path.exists(caption_path):
    os.makedirs(caption_path)
caption_string1 = os.path.join(caption_path, caption_name)
caption_string1 = caption_string1+'.txt' 
f2 = open(caption_string1,"w+")

for j in range(length_variable_list): #length_variable_list
    for k in range(63): #63
        for p in range(160): # 160
            tex_string1 = os.path.join(tex_path,tex_name)
            tex_string1 = tex_string1+"_"+str(total_no)+'.tex'
            f = open(tex_string1,"w+")
            string1 = tex_name+"_"+str(total_no)+".png"
            f2.write(string1)
            f2.write("\t")
            docu_class = '\documentclass[16pt]{article}'
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
            i = random.randint(0, length_function_list-1)
            function_index = i
            variable_index = j
            function_index1 = random.randint(0, length_function_list1-1)
            oper_index = random.randint(0, length_operator_list-1)
            oper_index1 = random.randint(0, length_operator_list1-1)
            fun = function_list[function_index]
            fun1 = function_list1[function_index1]
            var = variable_list[variable_index]

            power_index = random.randint(0, length_power_list-1)
            constant_index = random.randint(0, length_constant_list-1)

            name_fun = name_function_list[function_index]
            name_fun1 = name_function_list1[function_index1]
            name_var = name_variable_list[variable_index]
            oper = operator_list[oper_index]
            name_oper = name_operator_list[oper_index]
            power = power_list[power_index]
            name_power = name_power_list[power_index]
            constant = constant_list[constant_index]
            name_constant = name_constant_list[constant_index]
            oper1 = operator_list1[oper_index1]
            name_oper1 = name_operator_list1[oper_index1]
            ##################################################
            if k ==0: #intgral (six)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+fun+var+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ###################################################
            if k ==1: #integral (x/sinx)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b=r'{'+fun+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" all over ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ###################################################  
            if k ==2: # intergral (1/sinx)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+str(1)+'}'
                b=r'{'+fun+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write("one")
                f2.write(" all over ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ###################################################  
            if k ==3: # intergral (sinx2)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+fun+var+'^{'+str(2)+'}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_fun)
                f2.write(" of ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1 
            ###################################################
            if k ==4: #integral (1+-sinx)
                a = r'\scalebox{4.0}'
                b=r'{$\int('+str(1)+oper+fun+var+')\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1          
            ###################################################
            if k ==5: #integral (x+-sinx)  
                a = r'\scalebox{4.0}'
                b=r'{$\int('+var+oper+fun+var+')\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1 
            ###################################################
            if k ==6: #integral (xsinx)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'\ '+fun+var+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var) 
                f2.write(" and ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1 
            ###################################################
            if k ==7: #integral(sinx^2)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+name_fun1+'^{'+str(2)+'}'+var+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of second power of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1    
            ##################################################
            if k ==8: #integral(1/1+-sinx)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+str(1)+'}'
                b=r'{'+str(1)+oper+fun1+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of one all over one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==9: #integral(x/1+-sinx) 
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b=r'{'+str(1)+oper+fun1+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" all over one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1           
            ##################################################
            if k ==10: #integral (1/1+-sin^2x) 
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+str(1)+'}'
                b=r'{'+str(1)+oper+name_fun1+'^{2}'+'\ '+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of one all over one ")
                f2.write(name_oper)
                f2.write(" second power of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==11: #integral (x/1+-sin^2x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b=r'{'+str(1)+oper+name_fun1+'^{2}'+'\ '+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" all over one ")
                f2.write(name_oper)
                f2.write(" second power of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==12: #integral (1-sinx)/(1+sinx)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+str(1)+'-'+fun1+var+'}'
                b=r'{'+str(1)+'+'+fun1+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of one minus ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" all over one plus ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1   
            ##################################################
            if k ==13: #integral (1+sinx)/(1-sinx) 
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+str(1)+'+'+fun1+var+'}'
                b=r'{'+str(1)+'-'+fun1+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of one plus ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" all over one minus ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==14: #integral (sinx)/(1+-sinx)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+fun1+var+'}'
                b=r'{'+str(1)+oper+fun1+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" all over one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==15: #integral (sinx)/(1+-sin^2x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+fun1+var+'}'
                b=r'{'+str(1)+oper+name_fun1+'^{2}'+'\ '+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" all over one ")
                f2.write(name_oper)
                f2.write(" second power of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
            ##################################################
            if k ==16: #integral (sqrt(x^2-a^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'\sqrt{'+var+'^{2}'+oper+power+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==17: #integral (sqrt(a^2-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'\sqrt{'+power+oper+var+'^{2}'+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("second root of all")
                f2.write(name_power)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==18: #integral (x sqrt(x^2+-a^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'\sqrt{'+var+'^{2}'+oper+power+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var) 
                f2.write(" and second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==19: #integral (x sqrt(a^2-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'\sqrt{'+power+oper+var+'^{2}'+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var) 
                f2.write(" and second root of all")
                f2.write(name_power)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==20: #integral (x /sqrt(x^2-a^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b =r'{'+'\sqrt{'+var+'^{2}'+oper+power+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write(name_var)
                f2.write(" all over second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==21: #integral (x /sqrt(a^2-x^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b =r'{'+'\sqrt{'+power+oper+var+'^{2}'+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write(name_var)
                f2.write(" all over second root of all")
                f2.write(name_power) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==22: #integral (1 /sqrt(x^2-a^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+'\sqrt{'+var+'^{2}'+oper+power+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==23: #integral (1 /sqrt(a^2-x^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+'\sqrt{'+power+oper+var+'^{2}'+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over second root of all")
                f2.write(name_power) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==24: #integral (1 /x sqrt(x^2-a^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+var+'\sqrt{'+var+'^{2}'+oper+power+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over ")
                f2.write(name_var)
                f2.write(" and second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==25: #integral (1 /x sqrt(a^2-x^2))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+'\sqrt{'+power+oper+var+'^{2}'+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over ")
                f2.write(name_var)
                f2.write(" and second root of all")
                f2.write(name_power) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==26: #integral (sqrt(x^2-a^2)/x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+r'\sqrt{'+var+'^{2}'+oper+power+'}}'
                b =r'{'+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of second root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(name_power)
                f2.write("all over ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==27: #integral (sqrt(a^2-x^2)/x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+r'\sqrt{'+power+oper+var+'^{2}'+'}}'
                b =r'{'+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of second root of all")
                f2.write(name_power)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write("all over ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==28: #integral (sqrt(x-a))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'\sqrt{'+var+oper+constant+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==29: #integral (sqrt(a-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'\sqrt{'+constant+oper+var+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("second root of all")
                f2.write(name_constant)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==30: #integral (x sqrt(x+-a))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'\sqrt{'+var+oper+constant+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var) 
                f2.write(" and second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==31: #integral (x sqrt(a-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'\sqrt{'+constant+oper+var+'}'+'}\ d'+var+'$}' 
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var) 
                f2.write(" and second root of all")
                f2.write(name_constant)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==32: #integral (x /sqrt(x-a))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b =r'{'+'\sqrt{'+var+oper+constant+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write(name_var)
                f2.write(" all over second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==33: #integral (x /sqrt(a-x))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+var+'}'
                b =r'{'+'\sqrt{'+constant+oper+var+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write(name_var)
                f2.write(" all over second root of all")
                f2.write(name_constant) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==34: #integral (1 /sqrt(x-a))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+'\sqrt{'+var+oper+constant+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==35: #integral (1 /sqrt(a-x))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+'\sqrt{'+constant+oper+var+'}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over second root of all")
                f2.write(name_constant) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==36: #integral (1 /x sqrt(x-a))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+var+'{\sqrt{'+var+oper+constant+'}}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over ")
                f2.write(name_var)
                f2.write(" and second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==37: #integral (1 /x sqrt(a-x))
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+'1'+'}'
                b =r'{'+var+'{\sqrt{'+constant+oper+var+'}}'+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ") 
                f2.write("one")
                f2.write(" all over ")
                f2.write(name_var)
                f2.write(" and second root of all")
                f2.write(name_constant) 
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" ")
                f2.write("with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==38: #integral (sqrt(x-a)/x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+r'\sqrt{'+var+oper+constant+'}}'
                b =r'{'+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of second root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(name_constant)
                f2.write("all over ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==39: #integral (sqrt(a-x)/x)
                a = r'\scalebox{4.0}'
                a1 = r'{$\int \frac{'+r'\sqrt{'+constant+oper+var+'}}'
                b =r'{'+var+'}\ d'+var+'$}'
                d = a+a1+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of second root of all")
                f2.write(name_constant)
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" ")
                f2.write("all over ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1
            ##################################################
            if k ==40: #integral (e^+-x)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{'+oper1+var+'}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==41: #integral (e^(1+-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{('+'1'+oper+var+')}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==42: #integral (e^(x+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{('+var+oper+'1'+')}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1  
            ##################################################
            if k ==43: #integral (e^(1+-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{('+'1'+oper+var+'^{2}'+')}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==44: #integral (e^(x^2+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{('+var+'^{2}'+oper+'1'+')}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1   
            ##################################################
            if k ==45: #integral (e^+-x^2)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{'+oper1+var+'^{2}'+'}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==46: #integral (x(e^+-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{'+oper1+var+'}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==47: #integral (x(e^+-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{'+oper1+var+'^{2}'+'}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==48: #integral (xe^(1+-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{('+'1'+oper+var+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==49: #integral (xe^(x+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{('+var+oper+'1'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1  
            ##################################################
            if k ==50: #integral (xe^(1+-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{('+'1'+oper+var+'^{2}'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==51: #integral (xe^(x^2+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{('+var+'^{2}'+oper+'1'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1   
            ##################################################
            if k ==52: #integral (e^sqrt(1+-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{\sqrt{('+'1'+oper+var+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of square root of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==53: #integral (e^sqrt(x+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{\sqrt{('+var+oper+'1'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of square root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1  
            ##################################################
            if k ==54: #integral (e^sqrt(1+-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{\sqrt{('+'1'+oper+var+'^{2}'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of square root of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==55: #integral (e^sqrt(x^2+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{\sqrt{('+var+'^{2}'+oper+'1'+')}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of square root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1   
            ##################################################
            if k ==56: #integral (xe^sqrt(1+-x))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{\sqrt{('+'1'+oper+var+')}}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of square root of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==57: #integral (xe^sqrt(x+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{\sqrt{('+var+oper+'1'+')}}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of square root of all ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1  
            ##################################################
            if k ==58: #integral (xe^sqrt(1+-x^2))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{\sqrt{('+'1'+oper+var+'^{2}'+')}}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of square root of all one ")
                f2.write(name_oper)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" square with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==59: #integral (xe^sqrt(x^2+-1))
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{\sqrt{('+var+'^{2}'+oper+'1'+')}}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of square root of all ")
                f2.write(name_var)
                f2.write(" square ")
                f2.write(name_oper)
                f2.write(" one with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1   
            ##################################################
            if k ==60: #integral (e^+-sinx)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'e^{'+oper1+fun+var+'}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==61: #integral (x e^+-sinx)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+var+'{e^{'+oper1+fun+var+'}}'+'}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" and exponential of ")
                if oper1 == '-':
                    f2.write(name_oper1)
                    f2.write(" ")
                f2.write(name_fun)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")
                total_no = total_no+1 
            ##################################################
            if k ==62: #integral (a^sinx)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'a^{'+fun1+var+'} } \ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_fun1)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" power of a")
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1
##############################################################
for j in range(length_variable_list):
    for k in range(63, 73):#63 73
        for p in range (4): #4
            tex_string1 = os.path.join(tex_path,tex_name)
            tex_string1 = tex_string1+"_"+str(total_no)+'.tex'
            f = open(tex_string1,"w+")
            string1 = tex_name+"_"+str(total_no)+".png"
            f2.write(string1)
            f2.write("\t")
            docu_class = '\documentclass[16pt]{article}'
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
            i = random.randint(0, length_function_list-1)
            function_index = i
            variable_index = j
            function_index1 = random.randint(0, length_function_list1-1)
            oper_index = random.randint(0, length_operator_list-1)
            oper_index1 = random.randint(0, length_operator_list1-1)
            fun = function_list[function_index]
            fun1 = function_list1[function_index1]
            var = variable_list[variable_index]
            power_index = random.randint(0, length_power_list-1)
            constant_index = random.randint(0, length_constant_list-1)
            name_fun = name_function_list[function_index]
            name_fun1 = name_function_list1[function_index1]
            name_var = name_variable_list[variable_index]
            oper = operator_list[oper_index]
            name_oper = name_operator_list[oper_index]
            power = power_list[power_index]
            name_power = name_power_list[power_index]
            constant = constant_list[constant_index]
            name_constant = name_constant_list[constant_index]
            oper1 = operator_list1[oper_index1]
            name_oper1 = name_operator_list1[oper_index1]
            i = random.randint(0, 1)
            ##################################################
            if k ==63: #integral (a^x)
                a = r'\scalebox{4.0}'
                b=r'{$\int{'+'a^{'+var+'} } \ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                f2.write("integral of ")
                f2.write(name_var)
                f2.write(" power of a")
                f2.write(" with respect to ")
                f2.write(name_var) 
                f2.write("\n")      
                total_no = total_no+1 
            ##################################################
            if k ==64: #integral (ln x)
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$\int{'+'log('+var+')}\ d'+var+'$}'
                else:
                    b=r'{$\int{'+'ln('+var+')}\ d'+var+'$}'
                    
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of logarithmic of ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of natural logerthmic of ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1       
            ##################################################
            if k ==65: #integral (ln 1+-x)
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$\int{'+'log('+str(1)+oper+var+')}\ d'+var+'$}'
                else:
                    b=r'{$\int{'+'ln('+str(1)+oper+var+')}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of natural logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1    
            ##################################################
            if k ==66: #integral (ln x/x)
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$ \int \frac{'+'\ log('+var+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                else:
                    b=r'{$ \int \frac{' +'\ ln('+var+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                d = a+b+a1
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write("logarithmic of ")
                    f2.write(name_var)
                    f2.write(" all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write("natural logarithmic of ")
                    f2.write(name_var)
                    f2.write(" all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1
            ##################################################
            if k ==67: #integral (x ln x) 
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$ \int{'+var +'\ log('+var+')}' + '\ d'+var+'$}'
                else:
                    b=r'{$ \int{'+var +'\ ln('+var+')}' + '\ d'+var+ '$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write(name_var)
                    f2.write(" and logarithmic of ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write(name_var)
                    f2.write(" and natural logarithmic of ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1
            ##################################################
            if k ==68: #integral (x ln (1+-x))
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$\int{'+var +'\ log('+str(1)+oper+var+')}\ d'+var+'$}'
                else:
                    b=r'{$\int{'+var+ '\ ln('+str(1)+oper+var+')}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write(name_var) 
                    f2.write(" and logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write(name_var)
                    f2.write(" and natural logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1 
            ##################################################
            if k ==69: #integral (ln (x+-1))
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$\int{'+'log('+var+oper+str(1)+')}\ d'+var+'$}'
                else:
                    b=r'{$\int{'+'ln('+var+oper+str(1)+')}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of natural logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1
            ##################################################
            if k ==70: #integral (x ln (x+-1))
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$\int{'+var +'\ log('+var+oper+str(1)+')}\ d'+var+'$}'
                else:
                    b=r'{$\int{'+var+ '\ ln('+var+oper+str(1)+')}\ d'+var+'$}'
                d = a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write(name_var) 
                    f2.write(" and logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write(name_var)
                    f2.write(" and natural logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1
            ##################################################
            if k ==71: #integral (ln (1+-x)/x)
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$ \int \frac{'+'\ log('+str(1)+oper+var+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                else:
                    b=r'{$ \int \frac{' +'\ ln('+str(1)+oper+var+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                d = a+b+a1
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write("logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write("natural logarithmic of all one ")
                    f2.write(name_oper)
                    f2.write(" ")
                    f2.write(name_var)
                    f2.write(" all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1
            ##################################################
            if k ==72: #integral (ln (x+-1)/x)
                a = r'\scalebox{4.0}'
                if i == 0:
                    b=r'{$ \int \frac{'+'\ log('+var+oper+str(1)+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                else:
                    b=r'{$ \int \frac{' +'\ ln('+var+oper+str(1)+')}'
                    a1 = r'{'+ var+'}'+'\ d'+var+'$}'
                d = a+b+a1
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
                if i==0:
                    f2.write("integral of ")
                    f2.write("logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one")
                    f2.write(" all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                else:
                    f2.write("integral of ")
                    f2.write("natural logarithmic of all ")
                    f2.write(name_var)
                    f2.write(" ")
                    f2.write(name_oper)
                    f2.write(" one all over ")
                    f2.write(name_var)
                    f2.write(" with respect to ")
                    f2.write(name_var) 
                    f2.write("\n") 
                total_no = total_no+1



f2.close()       
      
