import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from pypdf import PdfReader
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatGooglePalm
from dotenv import load_dotenv
from htmlTemplates import user_template, bot_template, css
import os
from langchain_google_genai import GoogleGenerativeAI


def get_conversation_chain():
    # for RetrievalQA
    memory = ConversationBufferMemory(memory_key="chat_history", output_key='result', return_messages = True,
                                      return_source_documents=True)
    # for ConversationalRetrievalChain
    # memory = ConversationBufferMemory(memory_key="chat_history", output_key='answer', return_messages=True,
    #                                   return_source_documents=True)
    # llm = load_hugging_face_llm()
    llm = ChatGooglePalm(temprature = 0.5)
    # llm = GoogleGenerativeAI(model="gemini-pro", temprature=0.5)
    return RetrievalQA.from_llm(llm=llm, retriever=vector_store.as_retriever(),
                                memory = memory, verbose= True, return_source_documents=True)
    # return ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(),
    #                             memory = memory, verbose= True, return_source_documents=True)


def load_hugging_face_llm():
    repo_id = "gpt2"
    return HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 100})


def store_documents_in_database(docs):
    reader = PdfReader(docs)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=10, separator="\n", length_function=len)
    chunks = text_splitter.split_text(text)
    # to use own embedding
    # embeddings = HuggingFaceEmbeddings(model_name='google/flan-t5-xxl',model_kwargs={'device': 'cpu'})
    # db = st.session_state.vectordb.from_texts(texts = chunks)
    vector_store.from_texts(persist_directory=os.environ.get("CHROMA_DB_PATH"), texts = chunks,
                            embedding=embedding_function)


def handle_user_questions(query):
    # for RetrievalQA
    output = st.session_state.conversation_chain({"query": query})
    # for ConversationalRetrievalChain
    # output = st.session_state.conversation_chain({"question": query})
    print(output)
    st.session_state.chat_history=output["chat_history"]
    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)


st.set_page_config(page_title="Q and A using Documents", page_icon=":book:")
st.write(css, unsafe_allow_html= True)
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

load_dotenv()
with st.spinner('Initializing database...'):
    vector_store = Chroma(persist_directory=os.environ.get("CHROMA_DB_PATH"),
                          embedding_function = embedding_function)
    # vector_retriever = st.session_state.vectordb.as_retriever()

if "conversation_chain" not in st.session_state:
    st.session_state.conversation_chain = get_conversation_chain()
if "chat_history" in st.session_state:
    st.session_state.chat_history=None


st.title("Q&A using documents")
query = st.text_input(label="Enter question here:")

with st.sidebar:
    st.title("Upload your documents..")
    documents = st.file_uploader(label="Choose a file")
    button = st.button(label="Process")
    if button:
        with st.spinner('Processing...'):
            if documents:
                store_documents_in_database(documents)
                st.success('Document processed!')


if query:
    handle_user_questions(query)

