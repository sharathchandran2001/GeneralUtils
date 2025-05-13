import streamlit as st
import fitz  # PyMuPDF
from io import BytesIO

st.title("PDF Search and Viewer")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])

# Text input for search
search_text = st.text_input("Enter text to search in the PDF")

# Action buttons
search_button = st.button("Search")
display_button = st.button("Display All Contents")

def extract_text_by_page(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        pages.append((page_num + 1, text))
    return pages

if uploaded_pdf:
    pdf_bytes = uploaded_pdf.read()
    pages = extract_text_by_page(pdf_bytes)

    if display_button:
        st.subheader("Full PDF Content (Page-by-Page)")
        for page_num, text in pages:
            st.markdown(f"### Page {page_num}")
            st.text(text)

    if search_button and search_text:
        st.subheader(f"Searching for '{search_text}'...")
        found_pages = []
        for page_num, text in pages:
            if search_text.lower() in text.lower():
                found_pages.append(page_num)

        if found_pages:
            st.success(f"'{search_text}' found on page(s): {', '.join(map(str, found_pages))}")
        else:
            st.error(f"'{search_text}' not found in the PDF.")
