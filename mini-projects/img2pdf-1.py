import img2pdf

# opening from filename
with open("2.jpeg","wb") as f:
	f.write(img2pdf.convert('test.pdf'))