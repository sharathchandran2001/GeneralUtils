import fitz  # PyMuPDF
import sys

##python rpa_pdf_data_analyst.py Test.pdf "Agentic"


def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        pages.append((page_num + 1, text))
    return pages

def search_pdf(pdf_path, search_text):
    pages = extract_text_by_page(pdf_path)
    found_pages = [page_num for page_num, text in pages if search_text.lower() in text.lower()]

    if found_pages:
        print(f"'{search_text}' found on page(s): {', '.join(map(str, found_pages))}")
    else:
        print(f"'{search_text}' not found in the PDF.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search_pdf.py <path_to_pdf> <search_text>")
    else:
        pdf_path = sys.argv[1]
        search_text = sys.argv[2]
        search_pdf(pdf_path, search_text)
