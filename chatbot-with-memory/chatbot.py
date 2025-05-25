from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from memory import create_vectorstore
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def get_chain():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = create_vectorstore().as_retriever()
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory
    )
    return chain
