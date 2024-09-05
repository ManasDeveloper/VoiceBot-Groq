from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq

def get_response(text,api_key):
    llm = ChatGroq(model = "gemma2-9b-it",api_key=api_key)
    output = StrOutputParser()
    response = llm.invoke(text)
    parsed = output.parse(response)

    return parsed