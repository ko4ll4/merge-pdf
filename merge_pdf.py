from PyPDF2 import PdfFileWriter, PdfFileReader
 
 
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]
 

def filelist(infile):
    with open(infile, 'r', encoding='utf-8') as f:
        file_names = f.read().strip().split('\n')
    return file_names


input_file = 'filelist.txt'


if __name__ == '__main__':
    output = PdfFileWriter()
    files = filelist(input_file)
    for f in files:
        append_pdf(PdfFileReader(open(f, "rb")),output)
    output.write(open("combined.pdf", "wb"))