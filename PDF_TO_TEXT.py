#!/usr/bin/env python
# coding: utf-8

# In[8]:


from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# Create a PDF resource manager object
rsrcmgr = PDFResourceManager()

# Create a string buffer to hold the converted text
output_string = StringIO()

# Create a text converter object
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, output_string, codec=codec, laparams=laparams)

# Open the PDF file and create a PDF page interpreter object
with open('ex6.pdf', 'rb') as fp:
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)

# Close the text converter object and get the converted text
text = output_string.getvalue()
device.close()
output_string.close()

# Print the extracted text
print(text)


# In[ ]:




