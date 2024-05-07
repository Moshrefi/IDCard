from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import csv

from IDCardTemplate import template

output_path='output.pdf' 
canv = canvas.Canvas(output_path, pagesize=(324,204))

canv.setFillColorRGB(204, 102, 0)
canv.setFont("Helvetica", 14) 

with open('users.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile)
    next(data)  
    for line in data:
        canv = template(canv)
        name, title, location = line 
        print(name)
        if location == "" :
            canv.drawImage('photos/photo.png', 1.4*inch, -0.1*inch)
        else:
            canv.drawImage('photos/' + location, 1.4*inch, -0.1*inch)
        canv.drawString(-0.5*inch, -0.7*inch, name)    
        canv.drawString(1.5*inch, -0.3*inch, title)    
        canv.showPage()
canv.save()
