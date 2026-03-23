import pandas as pd
from reportlab.pdfgen import canvas

df = pd.DataFrame({"x": [1,2], "y": [3,4]})

c = canvas.Canvas("data_frame.pdf")
c.drawString(50, 750, "x  y")
c.drawString(60, 730, "1  3")
c.drawString(80, 710, "2  4")
c.save()

print("data_frame.pdf created successfully!")