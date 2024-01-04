import PyPDF2
from dotenv import load_dotenv
import os
import chromadb
from chromadb.config import Settings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma

load_dotenv()
doc_upload_path=os.environ.get("UPLOAD_DOCUMENT_PATH")
chroma_db_path=os.environ.get("CHROMA_DB_PATH")


def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files
    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' does not exist.")
    return None


def read_pdf(files):
    text = ""
    for file in files:
        file_path = doc_upload_path+"/" + file
        print(f"Processing file: {file_path}")
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
        except FileNotFoundError:
            print(f"The specified PDF file '{file_path}' does not exist.")
    return text


def upload_files_to_database():
    print("files to load..")
    files = list_files_in_folder(doc_upload_path)
    text = read_pdf(files)
    if text!= "":
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator="\n", length_function=len)
        print("Splitting files into chunks.")
        chunks = text_splitter.split_text(text)
        print("Saving into database.")
        Chroma.from_texts(persist_directory=chroma_db_path, texts = chunks, embedding=HuggingFaceEmbeddings())
        print("Files successfully saved to database.")


upload_files_to_database()