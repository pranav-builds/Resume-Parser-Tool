# utils/parser.py

import re
import pdfplumber

def extract_info_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''

    # Simple regex-based extraction
    name = re.findall(r'Name[:\-]?\s*(\w+ \w+)', text)
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.findall(r'\+?\d[\d\s\-\(\)]{8,}\d', text)
    skills = re.findall(r'Skills[:\-]?\s*(.+)', text)

    return {
        'File': pdf_path.split('/')[-1],
        'Name': name[0] if name else '',
        'Email': email[0] if email else '',
        'Phone': phone[0] if phone else '',
        'Skills': skills[0] if skills else '',
    }
