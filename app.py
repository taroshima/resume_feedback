import streamlit as st
import md_proc, txt_proc, docx_proc, pdf_proc
from llm_engine import run_llm_on_text

st.set_page_config(layout="wide")
st.title("CV Sensei")

col1, col2 = st.columns(2)

with col1:
    st.header("Upload File")
    uploaded_file = st.file_uploader(
        "Choose a .md, .txt, .docx, or .pdf file",
        type=["md", "txt", "docx", "pdf"]
    )

with col2:
    st.header("AI Output")
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1].lower()

        try:
            if file_type == "md":
                extracted_text = md_proc.extract_text(uploaded_file)
            elif file_type == "txt":
                extracted_text = txt_proc.extract_text(uploaded_file)
            elif file_type == "docx":
                extracted_text = docx_proc.extract_text(uploaded_file)
            elif file_type == "pdf":
                extracted_text = pdf_proc.extract_text(uploaded_file)
            else:
                st.error("Unsupported file type.")
                extracted_text = ""

            if extracted_text:
                response = run_llm_on_text(extracted_text)
                st.markdown(f"#### Parsed Response\n\n{response}", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("Upload a file to get AI insights.")