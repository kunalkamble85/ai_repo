from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from pypdf import PdfReader
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatGooglePalm


def get_conversation_chain(vector_store):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages= True)
    # llm = load_hugging_face_llm()
    llm = ChatGooglePalm()
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory= memory)
    return conversation_chain


def load_hugging_face_llm():
    repo_id = "google/flan-t5-xxl"
    return HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 100})


def store_documents_in_database(docs):
    reader = PdfReader(docs)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=10, separator="\n", length_function=len)
    chunks = text_splitter.split_text(text)
    # embeddings = HuggingFaceEmbeddings(model_name='google/flan-t5-xxl',
    #                                    model_kwargs={'device': 'cpu'})
    db = Chroma.from_texts(chunks, HuggingFaceEmbeddings())
    return db