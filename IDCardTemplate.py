from reportlab.lib.units import inch
def template(c):
    c.translate(inch,inch)
    c.setFont("Helvetica", 14)
    c.setStrokeColorRGB( 204, 102, 0)
    c.setFillColor( "darkorange") # font colour
    c.drawImage('ute_id_template.png',-1.1*inch,-1*inch)
    return c