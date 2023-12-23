from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


def load_hugging_face_llm():
    repo_id = "google/flan-t5-xxl"
    return HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0.2, "max_length": 100})


def get_menu_items(llm, cuisine):
    template = """suggest some food menu items for {cuisine}."""
    prompt = PromptTemplate(template=template, input_variables=["cuisine"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)
    print(llm_chain(cuisine))


if __name__ == "__main__":
    load_dotenv()
    llm = load_hugging_face_llm()
    get_menu_items(llm, "Indian")
