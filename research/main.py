import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain.document_loaders import PyPDFLoader

file_path = "data\SDG.pdf"
loader = PyPDFLoader()
data = loader.load(file_path)




