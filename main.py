import streamlit as st
import os 
from src.utils import load_model, apply_skill
from src.constants import insert_front, insert_back 


st.set_page_config(page_title="Prompt Enhancer", page_icon=":rocket:", initial_sidebar_state="collapsed", layout="wide")
st.title(":rocket: Prompt Enhancer")
st.info("""
Enhance your prompts in just a few clicks with intuitive interface.
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
    st.markdown("""### Select Prompt Engineering Skills""")
    st.info("For more information about each prompt engineering skill, click [here](https://gagadi.tistory.com/55)!") # link need to be updated 
    
    with st.expander("**Prompt Structure and Clarity**", expanded=True):
        audience_integration = st.toggle("Audience Integration")
        affirmative_sentencing = st.toggle("Affirmative Sentencing")
        output_primers = st.toggle("Output Primers") 
        delimiters = st.toggle("Delimiters") 
        formatted_prompt = st.toggle("Formatted Prompt") 
    
    with st.expander("**Specificity and Information**", expanded=True):
        fewshot_prompting = st.toggle("Few-Shot Prompting")
        guideline_indicators = st.toggle("Guideline Indicators")

    with st.expander("**Content and Language Style**", expanded=True): 
        no_politeness = st.toggle("No Politeness")
        imperative_task = st.toggle("Imperative Task")
        penalty_warning = st.toggle("Penalty Warning") 
        role_assignment = st.toggle("Role Assignment")
        echo_directive = st.toggle("Echo Directive")
    
    with st.expander("**Complex Tasks and Coding Prompts**", expanded=True): 
        task_decomposition = st.toggle("Task Decomposition")
        cot_with_fewshot = st.toggle("CoT with Few-Shot")

    # skills order need to be optimized 
    skills_to_apply = {
        "no_politeness": no_politeness, 
        "affirmative_sentencing": affirmative_sentencing,  
        "audience_integration": audience_integration,
        "imperative_task": imperative_task,
        "penalty_warning": penalty_warning,
        "task_decomposition": task_decomposition,
        "fewshot_prompting": fewshot_prompting,
        "cot_with_fewshot": cot_with_fewshot,
        "guideline_indicators": guideline_indicators,
        "role_assignment": role_assignment,
        "echo_directive": echo_directive,
        "delimiters": delimiters,
        "formatted_prompt": formatted_prompt,
        "output_primers": output_primers,
    }

with col2:
    prompt = st.text_area("**Original Prompt**", placeholder="Enter your prompt here to receive an enhanced version.", height=300)

    phrases_to_insert = {} 
    st.write("**How about including these magical phrases or words in your prompt?**")
    step_by_step = st.checkbox("Take a deep breath and work on this step by step.")
    tipping = st.checkbox("I’m going to tip $200 for a better solution!")
    important_to_career = st.checkbox("This is very important to my career.")
    explain_beginner = st.checkbox("Explain to me as if I'm a beginner.")
    detailed_writing = st.checkbox("Write a detailed text for me by adding all the information necessary.")
    human_like_response = st.checkbox("Answer in a natural, human-like manner.")
    unbiased_response = st.checkbox("Ensure that your answer is unbiased and avoids relying on stereotypes.")
    
    # phrases order need to be optimized 
    phrases_to_insert = {
        "step_by_step": step_by_step,
        "tipping": tipping,
        "important_to_career": important_to_career,
        "expain_beginner": explain_beginner,
        "detailed_writing": detailed_writing,
        "human_like_response": human_like_response,
        "unbiased_response": unbiased_response,
    }


    model_name = st.radio("**Select the model**", ('gpt-3.5-turbo-0125', 'gpt-4-0125-preview', 'gpt-4'), horizontal=True)
    enhance_btn = st.button("**Enhance!**")

    if enhance_btn:
        if not OPENAI_API_KEY:
            st.toast("Please enter your OpenAI API Key")

        order_num = 1
        with st.spinner("Processing..."): 
            llm = load_model(model_name)

            for skill, toggled in skills_to_apply.items():
                if toggled:
                    prompt = apply_skill(llm, skill, prompt)
                    st.markdown(f"{order_num}. Your prompt has been enhanced with **\"{skill}\"**!")
                    container = st.container(border=True)
                    container.markdown(prompt) 
                    order_num+=1

            for phrase, checked in phrases_to_insert.items():
                if checked and phrase in insert_front.keys():
                    st.markdown(f"{order_num}. Your prompt has been enhanced with **\"{phrase}\"**!")
                    prompt = insert_front[phrase] + '<br>' + prompt
                    container = st.container(border=True)
                    container.markdown(prompt, unsafe_allow_html=True) 
                    order_num+=1
                elif checked and phrase in insert_back.keys():
                    st.markdown(f"{order_num}. Your prompt has been enhanced with **\"{phrase}\"**!")
                    prompt = prompt + '<br>' + insert_back[phrase]
                    container = st.container(border=True)
                    container.markdown(prompt, unsafe_allow_html=True) 
                    order_num+=1
                

        st.toast("Prompt Enhancement Success!")     
        st.markdown("### Enhanced Prompt")
        container = st.container(border=True)
        container.title(":crystal_ball:") 
        container.markdown(prompt, unsafe_allow_html=True) 