from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
import os 


def load_model(model_name):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name=model_name)
    return llm 


def apply_skill(llm, skill, prompt):
    with open(f"templates/system.prompt", "r") as f:
        system_message = f.read() 

    with open(f"templates/{skill}.prompt", "r") as f:
        template = f.read() 

    prompt_template = PromptTemplate.from_template(template)
    formatted_input = prompt_template.format(prompt=prompt)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=formatted_input),
    ]

    response = llm.invoke(messages)

    return response.content


def insert_phrases(llm, phrases_to_insert, prompt):
    with open(f"templates/system.prompt", "r") as f:
        system_message = f.read() 
    
    with open(f"templates/insert_phrases.prompt", "r") as f:
        template = f.read()

    phrases_collection = ""
    for i, phrase in enumerate(phrases_to_insert):
        phrases_collection += f"{i+1}. {phrase}\n"
    
    prompt_template = PromptTemplate.from_template(template)
    formatted_input = prompt_template.format(phrases_collection=phrases_collection,
                                             prompt=prompt)
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=formatted_input),
    ]

    response = llm.invoke(messages)

    return response.content

