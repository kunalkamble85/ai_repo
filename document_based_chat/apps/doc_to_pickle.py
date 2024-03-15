import traceback

from dotenv import load_dotenv
import chromadb
from langchain_community.document_loaders import PyPDFLoader
import pickle

load_dotenv()



loader = PyPDFLoader("C:/kunal/work/sample_data/conda-cheatsheet.pdf")
pages = loader.load_and_split()
print(pages[:1])
# with open("./test.pickle", "wb") as file:
#     pickle.dump(pages, file=file)

with open("./test.pickle", "rb") as file:
    pages = pickle.load(file=file)
    print(pages[:1])
