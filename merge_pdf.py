#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyPDF2 import PdfFileWriter, PdfFileReader
 
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]
 
output = PdfFileWriter()
append_pdf(PdfFileReader(open("a.pdf","rb")),output)
append_pdf(PdfFileReader(open("b.pdf","rb")),output)
append_pdf(PdfFileReader(open("c.pdf","rb")),output)
 
output.write(open("combined.pdf","wb"))