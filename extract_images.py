import io
import pytesseract
from pdf2image import convert_from_path


def extract_text_from_pdf(pdf_path):
    # Convert PDF to image
    pages = convert_from_path(
        pdf_path,
        300,
        first_page=3,
        last_page=3,
        thread_count=4,
        use_pdftocairo=True,
    )

    # Extract text from each page using Tesseract OCR
    text_data = ""
    # print(len(pages))
    for page in pages:
        text = pytesseract.image_to_string(page, lang="tel")
        text_data += text + "\n"

    # Return the text data
    return text_data


text = extract_text_from_pdf(
    "/home/rajasekhar/Downloads/2 SANKHYAYOGAM(LATEST)_GITAMAKARANDAM.pdf"
)
print(text)
