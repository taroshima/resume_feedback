""" This script uses the Gemini API to review resumes. """
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def run_llm_on_text(resume_text: str) -> str:
    prompt = f"""
You are a professional resume/CV reviewer.
Please review the following resume content and provide feedback.
If theres no content, please say mention that there is no content and provide a basic overview on how a resume/CV should be structured.

Resume Content:
\"\"\"
{resume_text}
\"\"\"

Your feedback should include:
- Strengths 
- Areas of improvement 
- Suggestions for formatting or clarity 
- Any technical or grammar issues 
"""
    response = model.generate_content(prompt)
    return response.text



""" This script is designed to run a local LLM using the Ollama library. """

# import ollama
# import subprocess
# import socket
# import time

# port_no=os.getenv("OLLAMA_PORT")
# def is_ollama_running(port=port_no):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         return s.connect_ex(("localhost", port)) == 0

# def start_ollama_model(model="llama3"):
#     if not is_ollama_running():
#         print("🟡 Starting Ollama server...")
#         subprocess.Popen(["ollama", "run", model])
#         time.sleep(5)  # wait for model to load
#     else:
#         print("🟢 Ollama is already running.")

# def run_llm_on_text(resume_text: str) -> str:
#     start_ollama_model("llama3")

#     prompt = f"""
# You are a professional resume/CV reviewer.
# Please review the following resume/CV content and provide feedback in **markdown format**.

# Resume Content:
# \"\"\"
# {resume_text}
# \"\"\"

# Your feedback should include:
# - **Strengths** 💪
# - **Areas of Improvement** 🛠️
# - **Suggestions for Formatting or Clarity** 📝
# - **Technical or Grammar Issues** ⚠️

# Use proper markdown syntax with headings, and bullet points.
# Keep your tone helpful and constructive.
# """
#     response = ollama.chat(
#         model="llama3",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['message']['content']