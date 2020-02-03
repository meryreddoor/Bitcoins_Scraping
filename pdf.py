# importing libraries
from fpdf import FPDF 
import pandas as pd 
from func import fit_word
# importing variable
from data import data, european_countries

# Trying out different fpdf methods

# Create FPDF object
# FPDF(orientation, unit, format)
pdf = FPDF('P','mm','A4')

# Add page
pdf.add_page()

# Set font type
# .set_font(font,style,size)
pdf.set_font('Arial', 'B', 16)

# .text prints text on any position on screen, even over other objects
# .text(x,y,string)
"""pdf.text(0,10,'Hello, World')
tam = pdf.get_string_width("Hello, World")
pdf.text(1+tam,10,'Goodbye, World')"""

# .cell creates an object with defined borders, which don't overlap
# .cell(w,h,string,border,ln)
pdf.cell(190, 10, 'Hello, World!',1,1,'C')


pdf.set_font("Courier",'',14)
pdf.cell(190, 10, 'printf("Hello, World!");','LTR',1,'C')

# .set_text_color(r,g=-1,b=-1)
pdf.set_text_color(198,21,21)
pdf.cell(190, 10, 'print("Hello, World!")',"LRB",1,'C')

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(0)
pdf.cell(95,10,"C",1,0,'C')

# .set_draw_color(r,g,b)
pdf.set_draw_color(198,21,21)
# .set_line_width(size) in user defined unit
pdf.set_line_width(1)
pdf.cell(95,10,"Python",1,0,'C')

pdf.set_draw_color(4,139,63)
pdf.set_fill_color(4,139,63)
pdf.line(10,50,200,10)

pdf.set_draw_color(4,139,63)
pdf.set_fill_color(4,139,63)
# .rect(x,y,w,h,style)
pdf.rect(10,60,190,10,'DF')

pdf.set_draw_color(198,21,21)
pdf.set_fill_color(198,21,21)
# use parameter as values
for i in range(72,157,12):
    pdf.rect(10,i,190,10,'DF')

# .image for jpeg, png and gif images
pdf.image('zamora.png', 10, 170, h=50, link='http://www.diputaciondezamora.es/')
pdf.image('ironhacker.jpg', 100, 170, w=100, link='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

################################################################################

# Generating table from dataFrame

pdf.add_page()
df = pd.DataFrame(data)

# Defining parameters
num_col = len(df.columns)
w,h=190,277
font_type = ('Arial', 'B', 16)
pdf.set_font(*font_type)
pdf.set_text_color(0)
pdf.set_draw_color(0)

# Title
pdf.cell(w,10,'Datos Personales',1,1,'C')

# Column names
pdf.set_line_width(0.2)
for col in df.columns:
    pdf.cell(w/num_col,10,col,1,0,'C')
pdf.ln()

# Data
# First version, too specific
"""for index,row in df.iterrows():
    pdf.cell(w/num_col,10,row["name"],1,0,'C')
    pdf.cell(w/num_col,10,row["phone"],1,0,'C')
    pdf.cell(w/num_col,10,row["country"],1,0,'C')
    pdf.ln()"""
# After refactor:
pdf.set_fill_color(243,95,95)
font_type = ('Arial', '', 12)
pdf.set_font(*font_type)
# iteration rows
for _,row in df.iterrows():
    # Adding conditional
    fill = 0
    if row["country"] in european_countries:
        fill = 1
    # iterating columns
    for value in df.columns:
        pdf.cell(w/num_col,10,fit_word(row[value],w/num_col,font_type),1,0,'C',fill)
    pdf.ln()
    
# Exporting file
pdf.output("archivo.pdf",'F')