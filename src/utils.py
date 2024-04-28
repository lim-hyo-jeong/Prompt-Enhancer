from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
import os 
from src.prompts import templates


def load_model(model_name):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name=model_name)
    return llm 


def convert_newlines(prompt):
    prompt = prompt.replace("\n", "  \n")
    return prompt


def apply_skill(llm, skill, prompt, order_num, lang_eng=False):
    system_message = templates["system"]
    if lang_eng and order_num == 1:
        system_message += '\n' + templates["lang_eng"]
    elif not lang_eng:
        system_message += '\n' + templates["lang_default"]

    template = templates[skill]
    prompt_template = PromptTemplate.from_template(template)
    formatted_input = prompt_template.format(prompt=prompt)
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=formatted_input),
    ]

    response = llm.invoke(messages)

    return response.content


def apply_skills(llm, skills_to_apply, prompt, lang_eng=False):
    system_message = templates["system_multiple"]
    if lang_eng:
        system_message += '\n' + templates["lang_eng"]
    else:
        system_message += '\n' + templates["lang_default"]

    skills = [skill for skill, toggled in skills_to_apply.items() if toggled]
    integrated_templates = "[Prompt Engineering Techniques to Apply]\n"

    for idx, skill in enumerate(skills):
        template = templates[f"{skill}_simpler"]
        integrated_templates += f"{idx+1}. {skill}: {template}\n"
    integrated_templates += "Based on [Prompt engineering techniques to apply], refine the prompt provided below. Ensure that each technique is fully incorporated to achieve a clear and effective improvement:\n\n[original]\n{prompt}\n[improved]\n"

    prompt_template = PromptTemplate.from_template(integrated_templates)
    formatted_input = prompt_template.format(prompt=prompt)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=formatted_input),
    ]

    response = llm.invoke(messages)

    return response.content

