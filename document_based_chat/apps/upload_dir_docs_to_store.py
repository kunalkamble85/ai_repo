import traceback

from dotenv import load_dotenv
import os
import chromadb
from chromadb.config import Settings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain.document_loaders import DirectoryLoader
import shutil

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


def load_directory_files():
    text = ""
    try:
        print("loading files..")
        # outlook msg still having problem
        loader = DirectoryLoader(doc_upload_path, glob="**/*.docx", show_progress=True, use_multithreading= True)
        documents = loader.load()
        for document in documents:
            print(f"Processing file {document.metadata}")
            text+= document.page_content
    except:
        print(f"Error while loading directory {doc_upload_path}")
        traceback.format_exc()
    return text



def upload_files_to_database():
    print("Resetting database..")
    # chromadb.Client(Settings(persist_directory=chroma_db_path, allow_reset=True)).reset()
    shutil.rmtree(chroma_db_path)
    os.mkdir(chroma_db_path)
    text = load_directory_files()
    if text!= "":
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separator="\n", length_function=len)
        print("Splitting files into chunks.")
        chunks = text_splitter.split_text(text)
        print("Saving into database.")
        # sentence - transformers / all - MiniLM - L6 - v2
        Chroma.from_texts(persist_directory=chroma_db_path, texts = chunks, embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
        print("Files successfully saved to database.")


upload_files_to_database()