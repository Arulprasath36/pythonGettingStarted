"""
In This python example we are going to do operations like
read a text and
Print the number of pages
a PDF file.
"""

import PyPDF2
def pdfreader():
    pdfFileObj =open("C:\Users\Elcot\Documents\Head-First-Java-2nd-edition.pdf","rb")
    pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
    no_of_pages=pdfReader .numPages
    print(no_of_pages)

    pageObj =pdfReader.getPage(2)

    content=pageObj.extractText()
    print(content)

    pdfFileObj.close()

def main():
    pdfreader()

if __name__ == '__main__':
    main()