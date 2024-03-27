import streamlit as st
import os 
from src.utils import load_model, apply_skill, convert_newlines
from src.constants import insert_front, insert_back 


st.set_page_config(page_title="Prompt Enhancer", page_icon=":rocket:", initial_sidebar_state="collapsed", layout="wide")
st.title(":rocket: Prompt Enhancer")
st.markdown("""
##### Enhance your prompts in just a few clicks with intuitive interface.
""")
st.text("")
st.text("")

with st.popover("**:blue[Enter your OpenAI API key]**"):
    OPENAI_API_KEY = st.text_input("OpenAI API key", type="password")
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 
    st.info("""
    You can get your OpenAI API key [here](https://platform.openai.com/api-keys)
    """)

temp, buff = st.columns([0.3, 0.7]) 
if not OPENAI_API_KEY:
    temp.error("**Please enter your OpenAI API key**") 
st.text("")
st.text("")

col1, buff, col2 = st.columns([0.3, 0.05, 0.65])

with col1:
    st.markdown("""### Select Prompt Engineering Skills""")
    with st.popover("**:blue[Learn more about this section]**"):
        st.info("For detailed information on each prompt engineering skill, click [here](https://arxiv.org/pdf/2312.16171.pdf)")
        st.warning("**Warning**: Some prompt engineering skills can conflict with each other and may not be applied effectively.  \ne.g. \"Impertavie Task\" and \"Penalty Warning\"")
    
    toggle_all = st.toggle("**Select/Unselect all skills**", key="master_toggle")
    
    with st.expander("**Prompt Structure and Clarity**", expanded=True):
        audience_integration = st.toggle("**Audience Integration**", value=toggle_all)
        st.markdown("Integrate the intended audience in the prompt.")
        affirmative_sentencing = st.toggle("**Affirmative Sentencing**", value=toggle_all)
        st.markdown("Employ affirmative directives such as 'do,' while steering clear of negative language like 'don’t'.")
        output_primers = st.toggle("**Output Primers**", value=toggle_all)
        st.markdown("Use output primers, which involve concluding the prompt with the beginning of the desired output.")
        delimiters = st.toggle("**Delimiters**", value=toggle_all) 
        st.markdown("Use delimiters to distinguish specific segments of text within the prompt.")
        formatted_prompt = st.toggle("**Formatted Prompt**", value=toggle_all) 
        st.markdown("Use Formatted prompt to allow the model to understand the requirements structurally.")

    with st.expander("**Specificity and Information**", expanded=True):
        fewshot_prompting = st.toggle("**Few-Shot Prompting**", value=toggle_all)
        st.markdown("Implement example-driven prompting.")
        guideline_indicators = st.toggle("**Guideline Indicators**", value=toggle_all)
        st.markdown("Clarify the requirements using keywords, regulations, hints, or instructions.")

    with st.expander("**Content and Language Style**", expanded=True): 
        no_politeness = st.toggle("**No Politeness**", value=toggle_all)
        st.markdown("If you prefer more concise answers, remove any unnecessary polite or indirect phrases in the prompt.")
        imperative_task = st.toggle("**Imperative Task**", value=toggle_all)
        st.markdown("Incorporate the following phrases: \"Your task is\" and \"You MUST\".")
        penalty_warning = st.toggle("**Penalty Warning**", value=toggle_all) 
        st.markdown("Incorporate the following phrases: \"You will be penalized\".")
        role_assignment = st.toggle("**Role Assignment**", value=toggle_all)
        st.markdown("Assign a specific role or persona to the model within the prompt.")
        echo_directive = st.toggle("**Echo Directive**", value=toggle_all)
        st.markdown("Repeat a specific word or phrase multiple times within a prompt.")
    
    with st.expander("**Complex Tasks**", expanded=True): 
        task_decomposition = st.toggle("**Task Decomposition**", value=toggle_all)
        st.markdown("Break down complex tasks into a sequence of simpler prompts in an interactive conversation.")
        # cot_with_fewshot = st.toggle("**CoT with Few-Shot**", value=toggle_all)
        # st.markdown("Combine Cot with few-shot prompts.")

    # skills order need to be optimized 
    skills_to_apply = {
        "no_politeness": no_politeness, 
        "affirmative_sentencing": affirmative_sentencing,  
        "audience_integration": audience_integration,
        "role_assignment": role_assignment,
        "penalty_warning": penalty_warning,
        "imperative_task": imperative_task,
        "guideline_indicators": guideline_indicators,
        "task_decomposition": task_decomposition,
        "fewshot_prompting": fewshot_prompting,
        # "cot_with_fewshot": cot_with_fewshot,  
        "echo_directive": echo_directive,
        "delimiters": delimiters,
        "formatted_prompt": formatted_prompt,
        "output_primers": output_primers,
    }


with col2:
    st.markdown("""### Enhance your prompt easily!""")
    st.text("")
    prompt = st.text_area("**Original Prompt**", placeholder="Enter your prompt here to receive an enhanced version.", height=300)

    phrases_to_insert = {} 
    st.text("")
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

    st.text("")
    model_name = st.radio("**Select the model**", ('gpt-3.5-turbo-0125', 'gpt-4-0125-preview', 'gpt-4'), horizontal=True)
    st.text("")
    st.text("")
    enhance_btn = st.button("**:blue[Enhance!]**")

    if enhance_btn:
        if not prompt:
            st.toast("Please enter your prompt.")
        if not OPENAI_API_KEY:
            st.toast("Please enter your OpenAI API Key.")

        order_num = 1
        with st.spinner("Processing..."): 
            llm = load_model(model_name)

            for skill, toggled in skills_to_apply.items():
                if toggled:
                    prompt = apply_skill(llm, skill, prompt)
                    st.markdown(f":zap: {order_num}. Your prompt has been enhanced with **\"{skill}\"**!")
                    container = st.container(border=True)
                    container.markdown(convert_newlines(prompt))
                    order_num+=1

            for phrase, checked in phrases_to_insert.items():
                if checked and phrase in insert_front.keys():
                    st.markdown(f":zap: {order_num}. Your prompt has been enhanced with **\"{phrase}\"**!")
                    prompt = insert_front[phrase] + '\n' + prompt
                    container = st.container(border=True)
                    container.markdown(convert_newlines(prompt)) 
                    order_num+=1
                elif checked and phrase in insert_back.keys():
                    st.markdown(f":zap: {order_num}. Your prompt has been enhanced with **\"{phrase}\"**!")
                    prompt = prompt + '\n' + insert_back[phrase]
                    container = st.container(border=True)
                    container.markdown(convert_newlines(prompt)) 
                    order_num+=1
                

        st.toast("Prompt Enhancement Success!")     
        st.markdown("### Enhanced Prompt")
        container = st.container(border=True)
        container.title(":crystal_ball:") 
        container.markdown(convert_newlines(prompt)) 

st.text("")
st.text("")
st.markdown("<p style='text-align: center;'>Email: lim.gadi@gmail.com</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Github: @lim-hyo-jeong</p>", unsafe_allow_html=True)