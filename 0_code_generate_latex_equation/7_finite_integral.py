import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/7_finite_integral_latex/finite_integral/'
tex_name = 'f_integral'

caption_path = '../20_generate_textual_description/finite_integral/'
caption_name = 'f_integral_image_caption'

if not os.path.exists(caption_path):
    os.makedirs(caption_path)
caption_string1 = os.path.join(caption_path, caption_name)
caption_string1 = caption_string1+'.txt' 
f2 = open(caption_string1,"w+")

variable_list =['x','z','t', 'y']       
name_variable_list =['x','z','t', 'y']   
length_variable_list = len(variable_list)

operator_list1 = ['+','-']
name_operator_list1 = ['plus', 'minus'] 
length_operator_list1 =len(operator_list1)

function_list1 = ['sin\ ', 'cos\ ', 'tan\ ', 'sec\ ', 'cosec\ ', 'cot\ ']
name_function_list1 =[' sin ', ' cos ', ' tan ', ' sec ', ' cosec ', ' cot ']
length_function_list1 = len(function_list1)

function_list3 = ['sin^{2}', 'cos^{2}', 'tan^{2}', 'sec^{2}', 'cosec^{2}', 'cot^{2}']
name_function_list3 =[' second power of sin ', ' second power of cos ', ' second power of tan ', 
                      ' second power of sec ', ' second power of cosec ', ' second power of cot ']
length_function_list3 = len(function_list3)

function_list2 = ['sin^{-1}', 'cos^{-1}', 'tan^{-1}', 'sec^{-1}', 'cosec^{-1}', 'cot^{-1}',
                   'arcsin\ ', 'arccos\ ', 'arctan\ ', 'arcsec\ ', 'arccosec\ ', 'arccot\ '] 
name_function_list2 =[' inverse sin ', ' inverse cos ', ' inverse tan ', ' inverse sec ', ' inverse cosec ', ' inverse cot ',
                      ' inverse sin ', ' inverse cos ', ' inverse tan ', ' inverse sec ', ' inverse cosec ', ' inverse cot ']
length_function_list2 = len(function_list2)

uper_limit1 = ['\\frac{-3 \pi}{4}', '\\frac{-\pi}{2}', '\\frac{-\pi}{4}', '0', '\\frac{\pi}{4}','\\frac{\pi}{2}', '\\frac{3 \pi}{4}', '\pi']
name_uper_limit1 =[' minus three pie by four ', ' minus pie by two ', ' minus pie by four ', ' zero ', ' pie by four ', ' pie by two ', ' three pie by four ', ' pie ']
length_uper_limit1 = len(uper_limit1)

lower_limit1 = ['-\pi', '\\frac{-3 \pi}{4}', '\\frac{-\pi}{2}', '\\frac{-\pi}{4}', '0', '\\frac{\pi}{4}','\\frac{\pi}{2}', '\\frac{3 \pi}{4}']
name_lower_limit1 =[' minus pie ', ' minus three pie by four ', ' minus pie by two ', ' minus pie by four ', ' zero ', ' pie by four ', ' pie by two ', ' three pie by four ']
length_lower_limit1 = len(lower_limit1)

uper_limit2 = ['\\frac{-3}{\sqrt{2}}', '\\frac{-1}{2}', '\\frac{-1}{\sqrt{2}}', '0', '\\frac{1}{\sqrt{2}}','\\frac{1}{2}', '\\frac{3}{\sqrt{2}}', '1']
name_uper_limit2 =[' minus three by root two ', ' minus one by two ', ' minus one by root two ', ' zero ', ' one by root two ', ' one by two ', ' three by root two ', ' one ']
length_uper_limit2 = len(uper_limit2)

lower_limit2 = ['-1', '\\frac{-3}{\sqrt{2}}', '\\frac{-1}{2}', '\\frac{-1}{\sqrt{2}}', '0', '\\frac{1}{\sqrt{2}}','\\frac{1}{2}', '\\frac{3}{\sqrt{2}}' ]
name_lower_limit2 =[' minus one ', ' minus three by root two ', ' minus one by two ', ' minus one by root two ', ' zero ', ' one by root two ', ' one by two ', ' three by root two ']
length_lower_limit2 = len(lower_limit2)

constant_list1 = ['2', '3', '4', '5']
name_constant_list1 =[' two times ', ' three times ', ' four times ', ' five times ']
length_constant_list1 = len(constant_list1)

total_no =0

for j in range(length_function_list1): #length_function_list1
    a = r'\scalebox{4.0}'
    for k in range(26): #26
        for p in range (200):#200
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

            fun_index1 = j
            fun_index2 = random.randint(0, length_function_list2-1)
            fun_index3 = j
            var_index  = random.randint(0, length_variable_list-1)
            opr_index = random.randint(0, length_operator_list1-1)
            uper_index1 = random.randint(0, length_uper_limit1-1)
            lower_index1 = uper_index1
            uper_index2 = random.randint(0, length_uper_limit2-1)
            lower_index2 = uper_index2
            constant_index1 = random.randint(0, length_constant_list1-1)

            var1 = variable_list[var_index]
            opr1  = operator_list1[opr_index]
            fun1 = function_list1[fun_index1]
            fun2 = function_list2[fun_index2]
            fun3 = function_list3[fun_index3]
            uper1 = uper_limit1[uper_index1]
            lower1 = lower_limit1[lower_index1]
            uper2 = uper_limit2[uper_index2]
            lower2 = lower_limit2[lower_index2]
            cons1 = constant_list1[constant_index1]
                                        
            name_var1 = name_variable_list[var_index]
            name_opr1 = name_operator_list1[opr_index]
            name_fun1 = name_function_list1[fun_index1]
            name_fun2 = name_function_list2[fun_index2]
            name_fun3 = name_function_list3[fun_index3]
            name_uper1 = name_uper_limit1[uper_index1]
            name_lower1 = name_lower_limit1[lower_index1]
            name_uper2 = name_uper_limit2[uper_index2]
            name_lower2 = name_lower_limit2[lower_index2]
            name_cons1 = name_constant_list1[constant_index1]

            ###########################################################################################
            if k ==0: # 1 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ fun1+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==1: # 40 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+var1+fun1+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" and")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ##########################################################################################
            if k ==2: # 12,13 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower1 + '}^{'+ uper1+'}{\left('+var1+opr1+fun1+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ##########################################################################################
            if k ==3: # 12,13-2 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower1 + '}^{'+ uper1+'}{\left('+fun1+var1+opr1+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(" ")
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()    
            ##########################################################################################
            if k ==4: # 10,11 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower1 + '}^{'+ uper1+'}{\left('+str(1)+opr1+fun1+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one ")
                f2.write(name_opr1)
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ##########################################################################################
            if k ==5: # 10,11-2 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower1 + '}^{'+ uper1+'}{\left('+fun1+var1+opr1+str(1)+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(" one with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==6: # 1-2 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower2 + '}^{'+ uper2+'}{'+ fun2+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==7: # 40-2 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower2 + '}^{'+ uper2+'}{'+var1+fun2+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" and")
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ##########################################################################################
            if k ==8: # 12,13-3 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower2 + '}^{'+ uper2+'}{\left('+var1+opr1+fun2+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ##########################################################################################
            if k ==9: # 12,13-4 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower2 + '}^{'+ uper2+'}{\left('+fun2+var1+opr1+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(" ")
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
            ##########################################################################################
            if k ==10: # 10,11-3 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower2 + '}^{'+ uper2+'}{\left('+str(1)+opr1+fun2+var1+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one ")
                f2.write(name_opr1)
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
            ##########################################################################################
            if k ==11: # 10,11-4 eqn
                b=r'{$'+ r'\displaystyle' +r'\int_{'+ lower2 + '}^{'+ uper2+'}{\left('+fun2+var1+opr1+str(1)+r'\right)}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun2)
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(" one with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower2)
                f2.write("to upper limit")
                f2.write(name_uper2)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
            ###########################################################################################
            if k ==12: # 1-3 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ fun1+cons1+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write("of")
                f2.write(name_cons1)
                f2.write("times ")
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==13: # 4 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ fun1+var1+'^{2}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write("of ")
                f2.write(name_var1)
                f2.write(" square with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==14: # 5 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ fun3+var1+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun3)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
            ###########################################################################################
            if k ==15: # 3 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1) +'}{'+ fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one all over")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==16: # 2 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ var1 +'}{'+ fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" all over")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==17: # 2-1 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun1+var1 +'}{'+ var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" all over ")
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==18: # 6 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1) +'}{'+ str(1)+opr1+fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one")
                f2.write(" all over one ")
                f2.write(name_opr1)
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==19: # 6-2 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1) +'}{'+ fun1+var1+opr1+str(1) +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one all over")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" ")
                f2.write(name_opr1)
                f2.write(" one with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==20: # 6 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ var1 +'}{'+ str(1)+opr1+fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" all over one ")
                f2.write(name_opr1)
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==21: # 17 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1) +'}{'+ str(1)+opr1+fun3+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one")
                f2.write(" all over one ")
                f2.write(name_opr1)
                f2.write(name_fun3)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==22: # 17 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ var1 +'}{'+ str(1)+opr1+fun3+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of ")
                f2.write(name_var1)
                f2.write(" all over one ")
                f2.write(name_opr1)
                f2.write(name_fun3)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==23: # 18 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1)+'-'+ fun1+var1 +'}{'+ str(1)+'+'+fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one minus")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" all over one plus")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==24: # 19 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1)+'+'+ fun1+var1 +'}{'+ str(1)+'-'+fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of one plus")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" all over one minus")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close() 
            ###########################################################################################
            if k ==25: # 20-21 eqn
                b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun1+var1 +'}{'+ str(1)+opr1+fun1+var1 +'}'+'}\ d'+var1+'$}'
                d = a+b
                f2.write("integral of")
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" all over one ")
                f2.write(name_opr1)
                f2.write(name_fun1)
                f2.write(name_var1)
                f2.write(" with respect to ")
                f2.write(name_var1)
                f2.write(" from lower limit")
                f2.write(name_lower1)
                f2.write("to upper limit")
                f2.write(name_uper1)
                f2.write("\n")
                total_no = total_no+1 
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
#######################################################################################################
for i in range(length_function_list1):
    for j in range(length_function_list1):
        if (i!=j):
            a = r'\scalebox{4.0}'
            for k in range(10): 
                for p in range (50):#20
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

                    fun_index1 = i
                    fun_index2 = j
                    var_index  = random.randint(0, length_variable_list-1)
                    opr_index = random.randint(0, length_operator_list1-1)
                    uper_index1 = random.randint(0, length_uper_limit1-1)
                    lower_index1 = uper_index1
                    
                    var1 = variable_list[var_index]
                    opr1  = operator_list1[opr_index]
                    fun1 = function_list1[fun_index1]
                    fun2 = function_list1[fun_index2]
                    fun3 = function_list3[fun_index1]
                    fun4 = function_list3[fun_index2]
                    uper1 = uper_limit1[uper_index1]
                    lower1 = lower_limit1[lower_index1]
                                                                    
                    name_var1 = name_variable_list[var_index]
                    name_opr1 = name_operator_list1[opr_index]
                    name_fun1 = name_function_list1[fun_index1]
                    name_fun2 = name_function_list1[fun_index2]
                    name_fun3 = name_function_list3[fun_index1]
                    name_fun4 = name_function_list3[fun_index2]

                    name_uper1 = name_uper_limit1[uper_index1]
                    name_lower1 = name_lower_limit1[lower_index1]
                    ###########################################################################################
                    if k ==0: # 25 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ fun1+var1+'\ '+fun2+var1+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun2)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==1: # 24-1 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1) +'}{'+ fun1+var1+'\ '+fun2+var1 +'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of one all over")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun2)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==2: # 24-2 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ var1 +'}{'+ fun1+var1+'\ '+fun2+var1 +'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of ")
                        f2.write(name_var1)
                        f2.write(" all over")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun2)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==3: # 28 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun1+var1 +'}{'+ fun2+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" all over")
                        f2.write(name_fun2)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==4: # 33 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun3+var1 +'}{'+ fun4+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of")
                        f2.write(name_fun3)
                        f2.write(name_var1)
                        f2.write(" all over")
                        f2.write(name_fun4)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==5: # 38 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun1+var1 +'}{'+ fun4+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" all over")
                        f2.write(name_fun4)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################
                    if k ==6: # 39 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ fun3+var1 +'}{'+ fun1+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of")
                        f2.write(name_fun3)
                        f2.write(name_var1)
                        f2.write(" all over")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==7: # 34 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1)+'}{'+fun1+var1+'\ '+fun4+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of one all over")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun4)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==8: # 34 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1)+'}{'+fun3+var1+'\ '+fun1+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of one all over")
                        f2.write(name_fun3)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun1)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==9: # 33 eqn
                        b=r'{$'+r'\displaystyle' + r'\int_{'+ lower1 + '}^{'+ uper1+'}{'+ r'\frac{'+ str(1)+'}{'+fun3+var1+'\ '+fun4+var1+'}'+'}\ d'+var1+'$}'
                        d = a+b
                        f2.write("integral of one all over")
                        f2.write(name_fun3)
                        f2.write(name_var1)
                        f2.write(" and")
                        f2.write(name_fun4)
                        f2.write(name_var1)
                        f2.write(" with respect to ")
                        f2.write(name_var1)
                        f2.write(" from lower limit")
                        f2.write(name_lower1)
                        f2.write("to upper limit")
                        f2.write(name_uper1)
                        f2.write("\n")
                        total_no = total_no+1 
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()

f2.close()       
            
