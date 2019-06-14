import pdfx
for i in range(31,31):
    pdf = pdfx.PDFx("pdf{0}.pdf".format(i))
    metadata = pdf.get_metadata()
    references_list = pdf.get_references()
    references_dict = pdf.get_references_as_dict()
    pdf.download_pdfs("/Users/fahadkhan/Downloads/webscraping/")
