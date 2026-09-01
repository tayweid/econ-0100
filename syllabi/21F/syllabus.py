import os
from datetime import date
from PyPDF2 import PdfFileMerger
from IPython.display import Image
import nbformat
import warnings


def export_syllabus(parameters):
    
    [title, author, time] = parameters
    
    file_to_convert = nbformat.read('syllabus.ipynb', nbformat.NO_CONVERT)
    file_to_convert['metadata']['title'] = title + ' \\\\ ' + author + ' \\\\ ' + time
    del file_to_convert['cells'][0]
    
    today = date.today()
    savedate = '.'.join([str(today.year),str(today.strftime('%m')),str(today.strftime('%d'))])    
    
    nbformat.write(file_to_convert, 'file_to_convert.ipynb')
    os.system(
        'jupyter nbconvert' +
        ' --to pdf --no-prompt --no-input' +
        ' --output file_to_merge' +
        ' --template paper' +
        ' file_to_convert.ipynb'
    )
    os.remove('file_to_convert.ipynb')
    
    pdfs = ['file_to_merge.pdf', 'calendar_page.pdf']
    
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write('syllabus_'+savedate+'.pdf')
    merger.close()
    
    os.remove('file_to_merge.pdf')