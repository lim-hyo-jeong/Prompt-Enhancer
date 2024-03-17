import streamlit as st
import os 
from src.utils import enhance_prompt


st.set_page_config(page_title="Prompt Enhancer", page_icon=":blue_heart:", initial_sidebar_state="collapsed", layout="wide")
st.title(":blue_heart: Prompt Enhancer")
st.info("""
Upgrade your prompts in just a few clicks with intuitive interface.
""")

OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")
st.info("""
You can get your OpenAI API key [here](https://openai.com/blog/openai-api)
""")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 

if not OPENAI_API_KEY:
    st.error("Please enter your OpenAI API Key") 

col1, col2 = st.columns([0.25, 0.75])

with col1:
    st.write("""### Select Prompt Engineering Skills""")
    st.info("For more information about each prompt engineering skill, click [here](https://gagadi.tistory.com/55)!") # link need to be updated 
    with st.expander("**Content and Language Style**", expanded=True): 
        no_politeness = st.toggle("No Politeness")
        imperative_task = st.toggle("Imperative Task")
        preserve_style = st.toggle("Preserve Style") 
        # more toggle buttons to be added 

    skills_to_apply = {"no_politeness": no_politeness, 
                       "imperative_task": imperative_task,
                    }
    skills_to_insert = {"preserve_style": preserve_style}

with col2:
    prompt = st.text_area("**Original Prompt**", placeholder="Enter your prompt here to receive an enhanced version.", height=300)
    model_name = st.radio("**Select the model**", ('gpt-3.5-turbo-0125', 'gpt-4'), horizontal=True)
    enhance_btn = st.button("**Enhance!**")

    if enhance_btn:
        with st.spinner("Processing..."): 
            enhanced_prompt = enhance_prompt(model_name, skills_to_apply, skills_to_insert, prompt)

        st.toast("Prompt Enhancement Success!")     
        st.write("**Enhanced Prompt**")
        container = st.container(border=True)
        container.title(":crystal_ball:") 
        container.write(enhanced_prompt) 