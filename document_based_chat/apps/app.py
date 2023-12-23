import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from pypdf import PdfReader
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatGooglePalm
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template

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

def handle_user_questions(query):
    output = st.session_state.conversation_chain({"question": query})
    st.session_state.chat_history=output["chat_history"]
    for i, message in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)


st.set_page_config(page_title="Q and A using Documents", page_icon=":book:")
st.write(css, unsafe_allow_html= True)

st.title("Q&A using documents")
query = st.text_input(label="Enter question here:")

load_dotenv()

if "conversation_chain" not in st.session_state:
    st.session_state.conversation_chain = None
if "chat_history" in st.session_state:
    st.session_state.chat_history=None

with st.sidebar:
    st.title("Upload your documents..")
    documents = st.file_uploader(label="Choose a file")
    button = st.button(label="Process")
    if button:
        with st.spinner('Processing...'):
            if documents:
                vector_store = store_documents_in_database(documents)
                st.session_state.conversation_chain = get_conversation_chain(vector_store)
                st.success('Document processed!')
if query:
    handle_user_questions(query)