import docx

def extract_text(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])