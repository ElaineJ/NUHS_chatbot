# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 22:37:43 2018

@author: User
"""
from fpdf import FPDF
Record  = open("Patient 7827986.txt", "r")
for line in  Record:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    pdf.cell(60, 10, " ", 0,1,)#add space so title isnt shown and now paragraphs are aligned
    pdf.cell(60, 10, line, 0,1,) # add by default when i have time :(
    pdf.cell(60, 10, line, 0,1,)
pdf.output('test.pdf', 'F')
