# Script to take folder of PDF files, and output a CSV that lists all of the IIIF links for pages within PDF's

# Path to folder of PDF files:
filepath = r'/Users/path/to/folder'

#base path of where images are stored on IIIF Server
iiifPath = "https://iiif.example.org/iiif/2/folder-of-PDFs!"

import pandas as pd
import os
from PyPDF2 import PdfFileReader
df = pd.DataFrame(columns=['fileName', 'fileLocation', 'pageNumber'])
for root, dirs, files in os.walk(filepath):
    for f in files:
        if f.endswith(".pdf"):
            pdf=PdfFileReader(open(os.path.join(root, f),'rb'))
            df2 = pd.DataFrame([[f, os.path.join(root,f), pdf.getNumPages()]], columns=['fileName', 'fileLocation', 'pageNumber'])
            df = df.append(df2, ignore_index=True)

tmp = []
for index,line in df.iterrows():
    for i in range(1,line['pageNumber'] + 1):
        tmp.append({'fileName':line['fileName'], 'iiifLink':f"{iiifPath}{line['fileName']}/full/full/0/default.jpg?page={i}", 'pageNumber':line['pageNumber']})
df3 = pd.DataFrame(tmp,columns=['fileName', 'iiifLink', 'pageNumber'])

df3.to_csv("iiif-PDF-pages.csv")
