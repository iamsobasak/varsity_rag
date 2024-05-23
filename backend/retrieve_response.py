import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()


def get_llm_response(query):
    db = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"))
    

    template = """
        Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Always say "Thanks for asking!" at the end of the answer.
        
        Context : {context}
        
        Question : {question}
        
        Helpful Answer:
        
    """

    custom_rag_prompt = PromptTemplate.from_template(template)

    llm = ChatOpenAI(model="gpt-3.5-turbo")

    rag_chain = (
            {
                "context": db.as_retriever(),
                "question": RunnablePassthrough()
            }
            | custom_rag_prompt
            | llm
    )

    print(rag_chain.invoke(query))