# systhetic one variable linear equations

import numpy as np
import os
import os.path
import sys
import random

tex_path = '../1_generate_latex_files/5_differentiation_latex/differentiation/'
tex_name = 'diff'

caption_path = '../20_generate_textual_description/differentiation/'
caption_name = 'diff_image_caption'

variable_list =['x','y','z', 't']       
name_variable_list =['x','y','z', 't']   
length_variable_list = len(variable_list)

if not os.path.exists(caption_path):
    os.makedirs(caption_path)
caption_string1 = os.path.join(caption_path, caption_name)
caption_string1 = caption_string1+'.txt' 
mode = 'a+' if os.path.exists(caption_string1) else 'w+'
f2 = open(caption_string1, mode)

total_no = 0

for i in range (8): # 8
    for j in range(length_variable_list): # length_variable_list
        a = r'\scalebox{4.0}'
########################################################################################    
        if i ==0: #type of diff
            constant_list =['1', 'a^{2}', 'b^{2}', '4', '9', '16', '25', '36', '49', '64', '81', '100']
            name_constant_list = [' one ', ' a square ', ' b square ', ' four ', ' nine ', ' sixteen ', ' tweenty five ', ' thirty six ', ' fourty nine ', ' sixty four ', ' eighty one ', ' hundred ']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 
            length_constant_list = len(constant_list)
            length_operator_list =len(operator_list)

            constant_list1 =['1', 'a','b', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            name_constant_list1 = ['one', 'a', 'b', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

            for k in range(12): # total equation in diff1
                for p in range (200):        #write into tex file 
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
                    
                    l = random.randint(0, length_constant_list-1)
                    m = random.randint(0, length_operator_list-1)

                    variable_index = j
                    constant_index = l
                    operator_index = m
        
                    var = variable_list[variable_index]
                    opr = operator_list[operator_index]
                    cons = constant_list[constant_index]
                    cons1 = constant_list1[constant_index]
                    
                    name_var = name_variable_list[variable_index]
                    name_opr = name_operator_list[operator_index]
                    name_cons = name_constant_list[constant_index]
                    name_cons1 = name_constant_list1[constant_index]
                    
                    ###########################################################################################
                    if k ==0: # 1st eqn
                                    
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left(\sqrt{'+var+'^{2}'+opr+cons+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################        
                    if k ==1: # 2nd eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'\sqrt{'+var+'^{2}'+opr+cons+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==2: # 3rd eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+'\sqrt{'+cons +opr+var+'^{2}'+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==3: # 4th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'\sqrt{'+cons +opr+var+'^{2}'+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################        
                    if k ==4: # 5th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+var+'}'+'{\sqrt{'+var+'^{2}'+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==5: # 6th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+var+'}'+'{\sqrt{'+cons+opr+var+'^{2}'+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==6: # 7th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{\sqrt{'+cons+opr+var+'^{2}'+'}}'+ '{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(name_var)
                        f2.write(" square all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()                         
                    ###########################################################################################        
                    if k ==7: # 8th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{\sqrt{'+var+'^{2}'+opr+cons+'}}'+ '{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==8: # 9th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons1+'}'+'{\sqrt{'+var+'^{2}'+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_cons1)
                        f2.write(" all over second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==9: # 10th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons1+'}'+'{'+var+'\sqrt{'+var+'^{2}'+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_cons1)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" and second root of all ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==10: # 11th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons1+'}'+'{\sqrt{'+cons+opr+var+'^{2}'+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_cons1)
                        f2.write(" all over second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################        
                    if k ==11: # 12th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons1+'}'+'{'+var+'\sqrt{'+cons+opr+var+'^{2}'+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_cons1)
                        f2.write(" all over ")
                        f2.write(name_var) 
                        f2.write(" and second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" square ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()        
########################################################################################    
        if i ==1: #type of diff
            constant_list =['1', 'a','b', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            name_constant_list = [' one ', ' a ', ' b ', ' two ', ' three ', ' four ', ' five ', ' six ', ' seven ', ' eight ', ' nine ', ' ten ']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 
            length_constant_list = len(constant_list)
            length_operator_list =len(operator_list)

            for k in range(12): # total equation in diff1
                for p in range(200): #write into tex file 
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
                    
                    l = random.randint(0, length_constant_list-1)
                    m = random.randint(0, length_operator_list-1) 
                    
                    variable_index = j
                    constant_index = l
                    operator_index = m
        
                    var = variable_list[variable_index]
                    opr = operator_list[operator_index]
                    cons = constant_list[constant_index]
                                            
                    name_var = name_variable_list[variable_index]
                    name_opr = name_operator_list[operator_index]
                    name_cons = name_constant_list[constant_index]
                                            
                    ###########################################################################################
                    if k ==0: # 1st eqn
                                    
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left(\sqrt{'+var+opr+cons+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################        
                    if k ==1: # 2nd eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'\sqrt{'+var+opr+cons+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==2: # 3rd eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+'\sqrt{'+cons +opr+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==3: # 4th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'\sqrt{'+cons +opr+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################        
                    if k ==4: # 5th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+var+'}'+'{\sqrt{'+var+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==5: # 6th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+var+'}'+'{\sqrt{'+cons+opr+var+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==6: # 7th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{\sqrt{'+cons+opr+var+'}}'+ '{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(name_var)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()                         
                    ###########################################################################################        
                    if k ==7: # 8th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{\sqrt{'+var+opr+cons+'}}'+ '{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    
                    ###########################################################################################        
                    if k ==8: # 9th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons+'}'+'{\sqrt{'+var+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("all over second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==9: # 10th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons+'}'+'{'+var+'\sqrt{'+var+opr+cons+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("all over ")
                        f2.write(name_var)
                        f2.write(" and second root of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons)
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################        
                    if k ==10: # 11th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons+'}'+'{\sqrt{'+cons+opr+var+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("all over second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################        
                    if k ==11: # 12th eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+cons+'}'+'{'+var+'\sqrt{'+cons+opr+var+'}}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("all over ")
                        f2.write(name_var) 
                        f2.write(" and second root of all")
                        f2.write(name_cons)
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write("with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
########################################################################################    
        if i ==2: #type of diff
            constant_list =['cos', 'sin', 'tan', 'sec', 'cot', 'cosec', 'cosh', 'sinh', 'tanh', 'sech', 'coth', 'cosech']
            name_constant_list = [' cos ', ' sin ', ' tan ', ' sec ',' cot ', ' cosec ', ' hyperbolic cos ', ' hyperbolic sin ', ' hyperbolic tan ', ' hyperbolic sec ', ' hyperbolic cot ', ' hyperbolic cosec ']
            length_constant_list = len(constant_list)
            
            for k in range(8): # total equation in diff1
                for p in range(200):
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
                    l = random.randint(0, length_constant_list-1)
                    variable_index = j
                    constant_index = l
                            
                    var = variable_list[variable_index]
                    cons = constant_list[constant_index]
                                            
                    name_var = name_variable_list[variable_index]
                    name_cons = name_constant_list[constant_index]
                                            
                    ###########################################################################################
                    if k ==0: # 1st eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+'\ '+var +r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==1: # 2 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+'\ '+str(2)+var +r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("of two times ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==2: # 3 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+'\ '+var+'^{2}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write("of ")
                        f2.write(name_var)
                        f2.write(" square with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==3: # 4 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+'^{2}'+var+r'\right)' +'$}'
                        f2.write("differentiation of second power of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==4: # 5 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+cons+'\ '+var+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==5: # 6 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ r'\frac{'+var+'}{'+ cons+'\ '+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==6: # 7 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ r'\frac{'+str(1)+'}{'+ cons+'\ '+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        #f2.write(name_var)
                        f2.write("one all over")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==7: # 8 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ r'\frac{'+cons+'\ '+var+'}{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" all over ")
                        f2.write(name_var) 
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
########################################################################################    
        if i ==3: #4 type of diff
            constant_list =['arccos\ ', 'arcsin\ ', 'arctan\ ', 'arcsec\ ', 'arccot\ ', 'arccosec\ ', 'arccosh\ ', 'arcsinh\ ', 'arctanh\ ', 'arcsech\ ', 'arccoth\ ', 'arccosech\ ',
                            'cos^{-1}','sin^{-1}','tan^{-1}','sec^{-1}','cot^{-1}','cosec^{-1}','cosh^{-1}','sinh^{-1}','tanh^{-1}', 'sech^{-1}','coth^{-1}','cosech^{-1}' ]
            name_constant_list = [' inverse cos ', ' inverse sin ', ' inverse tan ', ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                                  ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', ' inverse hyperbolic sec ', 
                                  ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ', ' inverse cos ', ' inverse sin ', ' inverse tan ', ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                                  ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', ' inverse hyperbolic sec ', 
                                  ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ']
            length_constant_list = len(constant_list)
            
            for k in range(9): # total equation in diff1
                for p in range(200):
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
                    
                    l = random.randint(0, length_constant_list-1)
                    variable_index = j
                    constant_index = l
                            
                    var = variable_list[variable_index]
                    cons = constant_list[constant_index]
                                            
                    name_var = name_variable_list[variable_index]
                    name_cons = name_constant_list[constant_index]
                                            
                    ###########################################################################################
                    if k ==0: # 1st eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+var +r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==1: # 2 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+cons+var +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==2: # 3 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+ var+'}{'+cons+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" all over")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==3: # 4 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+ str(1)+'}{'+cons+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of one")
                        f2.write(" all over")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==4: # 5 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+ cons+var+'}{'+var+'}'+r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==5: # 6 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'+'+cons+var +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" plus")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()   
                    ###########################################################################################
                    if k ==6: # 7 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+'-'+cons+var +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" minus")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==7: # 8 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+var+'+'+var +r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" plus ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==8: # 9 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+cons+var+'-'+var +r'\right)' +'$}'
                        f2.write("differentiation of")
                        f2.write(name_cons)
                        f2.write(name_var)
                        f2.write(" minus ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1    
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 

########################################################################################    
        if i ==4: # 5type of diff
            constant_list =['a', 'b']
            name_constant_list = ['a', 'b']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 

            length_constant_list = len(constant_list)
            length_operator_list =len(operator_list)

            for k in range(1): # total equation in diff1
                for l in range(length_constant_list): # total constant
                    for m in range(length_operator_list): # total operation
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

                        variable_index = j
                        constant_index = l
                        operator_index = m
        
                        var = variable_list[variable_index]
                        opr = operator_list[operator_index]
                        cons = constant_list[constant_index]
                                              
                        name_var = name_variable_list[variable_index]
                        name_opr = name_operator_list[operator_index]
                        name_cons = name_constant_list[constant_index]
                                                
                        ###########################################################################################
                        if k ==0: # 1st eqn
                            if m ==1:
                                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ cons+'^{'+ opr+var+'}'+r'\right)' +'$}'
                                f2.write("differentiation of ")
                                f2.write(name_cons)
                                f2.write(" to the power minus ")
                                f2.write(name_var)
                                f2.write(" with respect to ")
                                f2.write(name_var)
                                f2.write("\n")
                                total_no = total_no+1 

                            else: 
                                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ cons+'^{'+ var+'}' +r'\right)' +'$}'
                                f2.write("differentiation of ")
                                f2.write(name_cons)
                                f2.write(" to the power ")
                                f2.write(name_var)
                                f2.write(" with respect to ")
                                f2.write(name_var)
                                f2.write("\n")
                                total_no = total_no+1 
                              
                            d=a+b
                            f.write(d)
                            f.write('\n')
                            f.write('\n')
                            f.write('\n')
                            f.write(end_docu)
                            f.close()

########################################################################################    
        if i ==5: # 6type of diff
            constant_list =['a', 'b']
            name_constant_list = ['a', 'b']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 

            length_constant_list = len(constant_list)
            length_operator_list =len(operator_list)

            for k in range(1): # total equation in diff1
                for l in range(length_constant_list): # total constant
                    for m in range(length_operator_list): # total operation
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

                        variable_index = j
                        constant_index = l
                        operator_index = m
        
                        var = variable_list[variable_index]
                        opr = operator_list[operator_index]
                        cons = constant_list[constant_index]
                                              
                        name_var = name_variable_list[variable_index]
                        name_opr = name_operator_list[operator_index]
                        name_cons = name_constant_list[constant_index]
                                                
                        ###########################################################################################
                        if k ==0: # 1st eqn
                            if m ==1:
                                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ cons+'^{'+ opr+var+'}'+r'\right)' +'$}'
                                f2.write("differentiation of ")
                                f2.write(name_cons)
                                f2.write(" to the power minus ")
                                f2.write(name_var)
                                f2.write(" with respect to ")
                                f2.write(name_var)
                                f2.write("\n")
                                total_no = total_no+1 

                            else: 
                                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ cons+'^{'+ var+'}' +r'\right)' +'$}'
                                f2.write("differentiation of ")
                                f2.write(name_cons)
                                f2.write(" to the power ")
                                f2.write(name_var)
                                f2.write(" with respect to ")
                                f2.write(name_var)
                                f2.write("\n")
                                total_no = total_no+1 
                              
                            d=a+b
                            f.write(d)
                            f.write('\n')
                            f.write('\n')
                            f.write('\n')
                            f.write(end_docu)
                            f.close() 

########################################################################################    
        if i ==6: # 7type of diff
            constant_list =['1','a', 'b', '2','3','4','5','6','7','8','9','10']
            name_constant_list = ['one','a', 'b','two','three','four','five','six','seven','eight','nine','ten']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 

            funtion_list =['ln','log']
            name_function_list=['natural logerthmic', 'logerthmic']

            length_constant_list = len(constant_list)
            length_operator_list = len(operator_list)
            length_function_list = len(funtion_list)

            for k in range(6): # total equation in diff1
                for p in range(200):            #write into tex file 
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

                    l = random.randint(0, length_constant_list-1)
                    m = random.randint(0, length_operator_list-1)
                    n = random.randint(0, length_function_list-1) 

                    variable_index = j
                    constant_index = l
                    operator_index = m
                    function_index = n
    
                    var = variable_list[variable_index]
                    opr = operator_list[operator_index]
                    cons = constant_list[constant_index]
                    fun = funtion_list[function_index]
                                        
                    name_var = name_variable_list[variable_index]
                    name_opr = name_operator_list[operator_index]
                    name_cons = name_constant_list[constant_index]
                    name_fun = name_function_list[function_index]
                                            
                    ###########################################################################################
                    if k ==0: # 1st eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ fun+'('+cons+opr+var+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==1: # 2 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ fun+'('+var+opr+cons+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==2: # 3 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+fun+'('+var+opr+cons+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==3: # 4 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+ fun+'('+cons+opr+var+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==4: # 5 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+fun+'('+cons+opr+var+')' +'}{'+ var+'}'+ r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_var)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    

                    ###########################################################################################
                    if k ==5: # 6 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+fun+'('+var+opr+cons+')' +'}{'+ var+'}'+ r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 

#######################################################################################    
        if i ==7: # 8type of diff
            constant_list =['1','a', 'b', '2','3','4','5','6','7','8','9','10']
            name_constant_list = ['one','a', 'b','two','three','four','five','six','seven','eight','nine','ten']
            operator_list = ['+','-']
            name_operator_list = ['plus', 'minus'] 

            funtion_list =['ln','log']
            name_function_list=['natural logerthmic', 'logerthmic']

            constant_list1 =['cos\ ', 'sin\ ', 'tan\ ', 'sec\ ', 'cot\ ', 'cosec\ ', 'cosh\ ', 'sinh\ ', 'tanh\ ', 'sech\ ', 'coth\ ', 'cosech\ ',
                              'arccos\ ', 'arcsin\ ', 'arctan\ ', 'arcsec\ ', 'arccot\ ', 'arccosec\ ', 'arccosh\ ', 'arcsinh\ ', 'arctanh\ ', 
                              'arcsech\ ', 'arccoth\ ', 'arccosech\ ', 'cos^{-1}','sin^{-1}','tan^{-1}','sec^{-1}','cot^{-1}','cosec^{-1}',
                              'cosh^{-1}','sinh^{-1}','tanh^{-1}', 'sech^{-1}','coth^{-1}','cosech^{-1}']    
            
               
            name_constant_list1 = [' cos ', ' sin ', ' tan ', ' sec ',' cot ', ' cosec ', ' hyperbolic cos ', ' hyperbolic sin ', 
                                   ' hyperbolic tan ', ' hyperbolic sec ', ' hyperbolic cot ', ' hyperbolic cosec ',
                                   ' inverse cos ', ' inverse sin ', ' inverse tan ', ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                                   ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', ' inverse hyperbolic sec ', 
                                   ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ', ' inverse cos ', ' inverse sin ', ' inverse tan ', 
                                   ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                                   ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', 
                                   ' inverse hyperbolic sec ', 
                                   ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ']
            length_constant_list1 = len(constant_list1)
            length_constant_list = len(constant_list)
            length_operator_list = len(operator_list)
            length_function_list = len(funtion_list)

            for k in range(6): # total equation in diff1
                for q in range(200):                #write into tex file 
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
                    
                    l = random.randint(0, length_constant_list-1)
                    m = random.randint(0, length_operator_list-1)
                    n = random.randint(0, length_function_list-1)
                    p = random.randint(0, length_constant_list1-1)
                    
                    variable_index = j
                    constant_index = l
                    operator_index = m
                    function_index = n
                    constant_index1 = p
    
                    var = variable_list[variable_index]
                    opr = operator_list[operator_index]
                    cons = constant_list[constant_index]
                    cons1 = constant_list1[constant_index1]
                    fun = funtion_list[function_index]
                                        
                    name_var = name_variable_list[variable_index]
                    name_opr = name_operator_list[operator_index]
                    name_cons = name_constant_list[constant_index]
                    name_fun = name_function_list[function_index]
                    name_cons1 = name_constant_list1[constant_index1]

                    ###########################################################################################
                    if k ==0: # 1st eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ fun+'('+cons+opr+cons1+var+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==1: # 2 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ fun+'('+cons1+var+opr+cons+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all")
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()  
                    ###########################################################################################
                    if k ==2: # 3 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+fun+'('+cons1+var+opr+cons+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and ")
                        f2.write(name_fun)
                        f2.write(" of all")
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
                    ###########################################################################################
                    if k ==3: # 4 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+ fun+'('+cons+opr+cons1+var+')' +r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_var)
                        f2.write(" and ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()
                    ###########################################################################################
                    if k ==4: # 5 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+fun+'('+cons+opr+cons1+var+')' +'}{'+ var+'}'+ r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all ")
                        f2.write(name_cons)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close()    

                    ###########################################################################################
                    if k ==5: # 6 eqn
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+r'\frac{'+fun+'('+cons1+var+opr+cons+')' +'}{'+ var+'}'+ r'\right)' +'$}'
                        f2.write("differentiation of ")
                        f2.write(name_fun)
                        f2.write(" of all")
                        f2.write(name_cons1)
                        f2.write(name_var)
                        f2.write(" ")
                        f2.write(name_opr)
                        f2.write(" ")
                        f2.write(name_cons)
                        f2.write(" all over ")
                        f2.write(name_var)
                        f2.write(" with respect to ")
                        f2.write(name_var)
                        f2.write("\n")
                        total_no = total_no+1 
                        d=a+b
                        f.write(d)
                        f.write('\n')
                        f.write('\n')
                        f.write('\n')
                        f.write(end_docu)
                        f.close() 
####################################################
#other differentiation
variable_list =['x','z','y', 't']       
name_variable_list =['x','z','y', 't']   
length_variable_list = len(variable_list)
 
for j in range(length_variable_list): # different types of variables
    a = r'\scalebox{4.0}'
    constant_list1 =['cos\ ', 'sin\ ', 'tan\ ', 'sec\ ', 'cot\ ', 'cosec\ ', 'cosh\ ', 'sinh\ ', 'tanh\ ', 'sech\ ', 'coth\ ', 'cosech\ ',
                        'arccos\ ', 'arcsin\ ', 'arctan\ ', 'arcsec\ ', 'arccot\ ', 'arccosec\ ', 'arccosh\ ', 'arcsinh\ ', 'arctanh\ ', 
                        'arcsech\ ', 'arccoth\ ', 'arccosech\ ', 'cos^{-1}','sin^{-1}','tan^{-1}','sec^{-1}','cot^{-1}','cosec^{-1}',
                        'cosh^{-1}','sinh^{-1}','tanh^{-1}', 'sech^{-1}','coth^{-1}','cosech^{-1}']    

    
    name_constant_list1 = [' cos ', ' sin ', ' tan ', ' sec ',' cot ', ' cosec ', ' hyperbolic cos ', ' hyperbolic sin ', 
                            ' hyperbolic tan ', ' hyperbolic sec ', ' hyperbolic cot ', ' hyperbolic cosec ',
                            ' inverse cos ', ' inverse sin ', ' inverse tan ', ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                            ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', ' inverse hyperbolic sec ', 
                            ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ', ' inverse cos ', ' inverse sin ', ' inverse tan ', 
                            ' inverse sec ',' inverse cot ', ' inverse cosec ', 
                            ' inverse hyperbolic cos ', ' inverse hyperbolic sin ', ' inverse hyperbolic tan ', 
                            ' inverse hyperbolic sec ', 
                            ' inverse hyperbolic cot ', ' inverse hyperbolic cosec ']
    length_constant_list1 = len(constant_list1)
    
    
    for k in range(2): # total equation in diff1
        for q in range(100):    #write into tex file 
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
            
            p = random.randint(0, length_constant_list1-1)
            variable_index = j
            constant_index1 = p

            var = variable_list[variable_index]
            cons1 = constant_list1[constant_index1]
                                        
            name_var = name_variable_list[variable_index]
            name_cons1 = name_constant_list1[constant_index1]

            ###########################################################################################
            if k ==0: # 1st eqn
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+cons1+var+')}' +r'\right)' +'$}'
                f2.write("differentiation of exponential of")
                f2.write(name_cons1)
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==1: # 2 eqn
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+cons1+var+')}' +r'\right)' +'$}'
                f2.write("differentiation of ")
                f2.write(name_var)
                f2.write(" and exponential of")
                f2.write(name_cons1)
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
###############################################################################
    operator_list = ['+','-']
    name_operator_list = ['plus', 'minus'] 
    length_operator_list =len(operator_list)

    for k in range(2): # total equation in diff1
        for q in range(100):        #write into tex file 
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

            p = random.randint(0, length_constant_list1-1)
            m = random.randint(0, length_operator_list-1)
            
            variable_index = j
            constant_index1 = p
            operator_index = m

            var = variable_list[variable_index]
            cons1 = constant_list1[constant_index1]
            opr = operator_list[operator_index]
                                        
            name_var = name_variable_list[variable_index]
            name_cons1 = name_constant_list1[constant_index1]
            name_opr = name_operator_list[operator_index]

            ###########################################################################################
            if k ==0: # 1st eqn
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+opr+ 'e'+'^{('+cons1+var+')}' +r'\right)' +'$}'
                f2.write("differentiation of exponential of ")
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)
                f2.write(name_cons1)
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k ==1: # 2 eqn
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+cons1+var+')}'+ opr+var +r'\right)' +'$}'
                f2.write("differentiation of exponential of")
                f2.write(name_cons1)
                f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)
                f2.write(" ")
                f2.write(name_var)
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
####################################################################################
    constant_list =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    name_constant_list = ['one', 'second', 'third power of', 'fourth power of', 
                           'fifth power of', 'sixth power of', 'seventh power of', 
                           'eighth power of', 'nineth power of', 'tenth power of']  
    length_constant_list =len(constant_list) 

    for k in range(12): # total equation in diff1
        for q in range(100):        #write into tex file 
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

            p = random.randint(0, length_constant_list-1)
            m = random.randint(0, length_operator_list-1) 

            variable_index = j
            constant_index = p
            operator_index = m

            var = variable_list[variable_index]
            cons = constant_list[constant_index]
            opr = operator_list[operator_index]
                                        
            name_var = name_variable_list[variable_index]
            name_cons = name_constant_list[constant_index]
            name_opr = name_operator_list[operator_index]
            ###########################################################################################
            if k == 0:
                if m == 0:
                    if p == 0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+var+')}' +r'\right)' +'$}'
                    else:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'    
                else:
                    if p==0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+opr+var+')}' +r'\right)' +'$}'
                    else: 
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+opr+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'

                f2.write("differentiation of exponential of ")
                if m==1:
                    f2.write(name_opr)
                    f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k == 1:
                
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+str(1)+opr+var+')}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+str(1)+opr+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of all one ")
                f2.write(name_opr)
                f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()   
            ###########################################################################################
            if k == 2:
                
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+var+opr+str(1)+')}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+var+'^{'+cons+'}'+opr+str(1)+')}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of all ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)          
                f2.write(" one with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()      
            ##########################################################################################
            if k == 3:
                if m == 0:
                    if p == 0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+ 'e'+'^{('+var+')}' +r'\right)' +'$}'
                    else:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'    
                else:
                    if p==0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+opr+var+')}' +r'\right)' +'$}'
                    else: 
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+opr+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'
                
                f2.write("differentiation of ")
                f2.write(name_var)
                f2.write(" and exponential of ")
                if m==1:
                    f2.write(name_opr)
                    f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k == 4:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+ 'e'+'^{('+str(1)+opr+var+')}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+str(1)+opr+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'    
                
                f2.write("differentiation of ")
                f2.write(name_var)
                f2.write(" and exponential of all one ")
                f2.write(name_opr)
                f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
            ###########################################################################################
            if k == 5:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+var+opr+str(1)+')}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+var+'^{'+cons+'}'+opr+str(1)+')}' +r'\right)' +'$}'    
                
                f2.write("differentiation of ") 
                f2.write(name_var)
                f2.write(" and exponential of all ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)          
                f2.write(" one with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k == 6:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+ r'\sqrt{'+str(1)+opr+var+'})}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+ r'\sqrt{'+str(1)+opr+var+'^{'+cons+'}'+'})}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of second root of all one ")
                f2.write(name_opr)
                f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()                                      
            ###########################################################################################
            if k == 7:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+r'\sqrt{'+var+opr+str(1)+'})}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+r'\sqrt{'+var+'^{'+cons+'}'+opr+str(1)+'})}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of second root of all ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)          
                f2.write(" one with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()                    
            ###########################################################################################
            if k == 8:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+ r'\sqrt{'+str(1)+opr+var+'})}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+ 'e'+'^{('+ r'\sqrt{'+str(1)+opr+var+'^{'+cons+'}'+'})}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of ")
                f2.write(name_var)
                f2.write(" and second root of all one ")
                f2.write(name_opr)
                f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()            
            ###########################################################################################
            if k == 9:
                if p == 0:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+r'\sqrt{'+var+opr+str(1)+'})}' +r'\right)' +'$}'
                else:
                    b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'e'+'^{('+r'\sqrt{'+var+'^{'+cons+'}'+opr+str(1)+'})}' +r'\right)' +'$}'    
                
                f2.write("differentiation of exponential of ")
                f2.write(name_var)
                f2.write(" and second root of all ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)
                f2.write(" ")
                f2.write(name_opr)          
                f2.write(" one with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()        
            ###########################################################################################
            if k == 10:
                if m == 0:
                    if p == 0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+var+opr+ 'e'+'^{('+var+')}' +r'\right)' +'$}'
                    else:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'^{'+cons+'}'+opr+'e'+'^{('+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'    
                else:
                    if p==0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+opr+'e'+'^{('+opr+var+')}' +r'\right)' +'$}'
                    else: 
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'^{'+cons+'}'+opr+'e'+'^{('+opr+var+'^{'+cons+'}'+')}' +r'\right)' +'$}'

                f2.write("differentiation of ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var) 
                f2.write(" ")         
                f2.write(name_opr)                 
                f2.write(" and exponential of ")
                if m==1:
                    f2.write(name_opr)
                    f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)      
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()
            ###########################################################################################
            if k == 11:
                if m == 0:
                    if p == 0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+'e'+'^{('+var+')}' + opr+var+r'\right)' +'$}'
                    else:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+var+'^{'+cons+'}'+')}'+opr+var+'^{'+cons+'}' +r'\right)' +'$}'    
                else:
                    if p==0:
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+'e'+'^{('+opr+var+')}'+ opr + var +r'\right)' +'$}'
                    else: 
                        b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ 'e'+'^{('+opr+var+'^{'+cons+'}'+')}' +opr+var+'^{'+cons+'}'+r'\right)' +'$}'

                f2.write("differentiation of exponential of ")
                if m==1:
                    f2.write(name_opr)
                    f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var)
                
                f2.write(" ")         
                f2.write(name_opr)
                f2.write(" ")
                if p==0:
                    f2.write(name_var)
                if p==1:
                    f2.write(name_var)
                    f2.write(" square")
                if p>1:
                    f2.write(name_cons)
                    f2.write(" ")
                    f2.write(name_var) 
                f2.write(" with respect to ")
                f2.write(name_var)
                f2.write("\n")
                total_no = total_no+1 
                
                d=a+b
                f.write(d)
                f.write('\n')
                f.write('\n')
                f.write('\n')
                f.write(end_docu)
                f.close()  
###########################################
#another differentiation
variable_list =['x','z','t', 'y']       
name_variable_list =['x','z','t', 'y']   
length_variable_list = len(variable_list)
 
for j in range(length_variable_list): # different types of variables
    a = r'\scalebox{4.0}'
################################################################################
    operator_list = ['+','-']
    name_operator_list = ['plus', 'minus'] 
    length_operator_list =len(operator_list)
####################################################################################
    constant_list =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    name_constant_list = ['one', 'second', 'third power of', 'fourth power of', 
                           'fifth power of', 'sixth power of', 'seventh power of', 
                           'eighth power of', 'nineth power of', 'tenth power of']  
    length_constant_list =len(constant_list) 
####################################################################################
    constant_list1 =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    name_constant_list1 = ['one', 'two', 'three', 'four', 
                           'five', 'six', 'seven', 
                           'eight', 'nine', 'ten']  
    length_constant_list1 = len(constant_list1)     
    
    for t in range(100):  
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

        variable_index = j
        k = random.randint(0, length_operator_list-1)
        l = random.randint(0, length_constant_list-1)
        m = random.randint(0, length_operator_list-1)
        n = random.randint(0, length_constant_list1-1)
        p = random.randint(0, length_operator_list-1)
        q = random.randint(0, length_constant_list1-1)
        operator_index1 = k
        constant_index1 = l
        operator_index2 = m
        constant_index2 = n
        operator_index3 = p 
        constant_index3 = q

        var = variable_list[variable_index]
        opr1 = operator_list[operator_index1]
        cons1 = constant_list[constant_index1]
        opr2 = operator_list[operator_index2]
        cons2 = constant_list1[constant_index2]
        opr3 = operator_list[operator_index3]
        cons3 = constant_list[constant_index3]
                                    
        name_var = name_variable_list[variable_index]
        name_opr1 = name_operator_list[operator_index1]
        name_cons1 = name_constant_list[constant_index1]
        name_opr2 = name_operator_list[operator_index2]
        name_cons2 = name_constant_list1[constant_index2]
        name_opr3 = name_operator_list[operator_index3]
        name_cons3 = name_constant_list1[constant_index3]
        ###########################################################################################
        
        if k == 0:
            if l == 0:
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+opr3+cons3 +r'\right)' +'$}'
            else:
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ var+'^{'+cons1+'}'+opr2+cons2+var+opr3+cons3 +r'\right)' +'$}'    
        else:
            if l==0:
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+ opr1+var+opr3+cons3 +r'\right)' +'$}'
            else: 
                b=r'{$'+ r'\frac{d}{d'+var+'}\left('+opr1+ var+'^{'+cons1+'}'+opr2+cons2+var+opr3+cons3 +r'\right)' +'$}'

        f2.write("differentiation of exponential of ")
        if k==1:
            f2.write(name_opr1)
            f2.write(" ")
        if l==0:
            f2.write(name_var)
        if l==1:
            f2.write(name_var)
            f2.write(" square")
        if l>1:
            f2.write(name_cons1)
            f2.write(" ")
            f2.write(name_var)
        if l>0:
            f2.write(" ")     
            f2.write(name_opr2)
            f2.write(" ")
            f2.write(name_cons2)
            f2.write(" times ")
            f2.write(name_var)
        f2.write(" ") 
        f2.write(name_opr3)
        f2.write(" ")
        f2.write(name_cons3)
        f2.write(" with respect to ")
        f2.write(name_var)
        f2.write("\n")
        total_no = total_no+1 
        
        d=a+b
        f.write(d)
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write(end_docu)
        f.close()                         
f2.close()                                               
                                    
                  
                       
                    

       
      




                       


   
              
   
                           
                            

                    


                       


     
      
