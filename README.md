# IIIF-PDF-pages

Script to take folder of PDF files, and output a CSV that lists all of the IIIF links for pages within PDF's

Currently functional with Cantaloupe IIIF server, which (currently) does not provide any way to access the pages within a PDF thorugh the manifest

- set the path of the folder with the PDF files
- set the base URL of the IIIF server


Output will be:

filename / iiifLink / numberOfPages
