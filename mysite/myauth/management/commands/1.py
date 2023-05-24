from ptext.pdf.document import Document
from ptext.pdf.page.page import Page
from ptext.pdf.pdf import PDF

# Create an empty Document
document = Document()

# Create an empty page
page = Page()

# Add the Page to the Document
document.append_page(page)

# Write the Document to a file
with open("output.pdf", "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, document)