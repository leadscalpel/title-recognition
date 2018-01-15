import os
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def pdf_to_txt(pdfpath, txtpath):
    for file in os.listdir(pdfpath):
        if '.pdf' in file:
            pdfFile = open(os.path.join(pdfpath, file), 'rb')
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)

            process_pdf(rsrcmgr, device, pdfFile)
            device.close()

            content = retstr.getvalue()
            retstr.close()
            with open(os.path.join(txtpath, file.replace('.pdf', '.txt')), 'w') as f:
                f.write(content)

