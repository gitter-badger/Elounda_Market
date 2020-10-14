#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
from PyPDF2 import PdfFileMerger

path1 = '/Users/kommas/Downloads/1.pdf'
path2 = '/Users/kommas/Downloads/2.pdf'

pdfs = [path1, path2]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write('/Users/kommas/Downloads/result.pdf')
merger.close()

