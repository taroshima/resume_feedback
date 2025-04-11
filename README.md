# CV Sensei

**CV Sensei** is a Streamlit-based application that provides intelligent, formatted feedback on resumes/CVs using state-of-the-art language models.  
Users can choose between **Gemini (cloud-based)** and **LLaMA 3 via Ollama (local)** to review `.txt`, `.md`, `.docx`, or `.pdf` files.

---

## Features

- Upload `.txt`, `.md`, `.docx`, or `.pdf` files
- Choose between:
  - Google Gemini (cloud-based API)
  - LLaMA 3 (locally hosted via Ollama)
- Receive structured markdown feedback including:
  - Strengths
  - Areas for improvement
  - Suggestions for formatting or clarity
  - Grammar or technical issues

---

## Project Structure

```
resume-genius/
│
├── app.py                # Main Streamlit app
├── llm_engine.py         # Gemini/Ollama LLM logic
├── md_proc.py            # Markdown file processing
├── txt_proc.py           # Text file processing
├── docx_proc.py          # DOCX file processing
├── pdf_proc.py           # PDF file processing
├── .env                  # Environment variables
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-genius.git
cd resume-genius
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root folder and include the following:

```env
GOOGLE_API_KEY=your_gemini_api_key
OLLAMA_PORT=11434 (Default port but you can change it if required)
```

---

## Language Model Options

### Option A: Gemini (Cloud)

#### Requirements:
- Google account
- [Create an API key](https://aistudio.google.com/app/apikey)

Gemini will be automatically used when `run_llm_on_text is called.

---

### Option B: Ollama (Local)

#### Requirements:
- Uncomment the code 
- [Download and install Ollama](https://ollama.com/download)
- Run the model manually or let the script start it:

```bash
ollama run llama3
```

The script includes logic to automatically start Ollama if it's not already running.

---

## Running the App

```bash
streamlit run app.py
```

---

## Sample Prompt Used

You are a professional resume reviewer.  
Please review the following resume content and provide feedback in markdown format. Your feedback should include:

- Strengths  
- Areas of improvement  
- Suggestions for formatting or clarity  
- Any grammar or technical issues  

---