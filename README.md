# :rocket: Prompt Enhancer
#### Prompt Engineering at Your Fingertips!

Welcome to Prompt Enhancer, a streamlit-powered application designed to improve your prompts effortlessly. This tool integrates various prompt engineering principles, as outlined in the paper [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/pdf/2312.16171.pdf). With Prompt Enhancer, you can easily apply prompt engineering techniques validated by latest research through a user-friendly interface, enhancing your communication with AI models.


## Getting Started 

### 1. Online access : 

   You can access the Prompt Enhancer website directly by visiting the following URL: 
   https://prompt-enhancer.streamlit.app/ 

### 2. Local setup : 
1. **Clone the Prompt Enhancer repository**:
   ```
   git clone https://github.com/lim-hyo-jeong/Prompt-Enhancer.git
   ```
2. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```
3. **Get OpenAI API key**:
   You can get your OpenAI API key [here](https://platform.openai.com/api-keys)
4. **Run Prompt Enhancer**:
   ```
   streamlit run main.py
   ```


## How to Use 

1. **Prompt Input**: Enter the prompt you want to enhance in the designated text area.
2. **Skill Application**: Select the skills you want to apply to refine your prompt.
3. **Phrase Inclusion**: Choose whether to add specific phrases that guide the AI towards generating better responses.
4. **Enhancement**: Click the "Enhance!" button to apply your selections and view the enhanced prompt.


## Research and Inspiration

Prompt Enhancer incorporates various prompt engineering techniques grounded in the principles from VILA-Lab's [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4 (2024)](https://arxiv.org/pdf/2312.16171.pdf). 
Additionally, the tool offers users the option to incorporate emotional prompts such as "This is very important to my career," inspired by Microsoft's [Large Language Models Understand and Can Be Enhanced by Emotional Stimuli (2023)](https://arxiv.org/pdf/2307.11760.pdf). Users can also choose to include phrases like "Take a deep breath and work on this problem step-by-step," which encourage AI to deliver better responses, which is validated by Google DeepMind's [Large Language Models as Optimizers (2023)](https://arxiv.org/pdf/2309.03409.pdf).


## Technical Stack

1. **Streamlit**: Creates an intuitive user interface for an engaging user experience.
2. **LangChain**: Seamlessly integrates large language models into the application.
3. **OpenAI API**: Connects to the OpenAI models to provide real-time prompt enhancement.


## For Feedback

- **Email**: lim.gadi@gmail.com
- **GitHub**: [@lim-hyo-jeong](https://github.com/lim-hyo-jeong)
- **Linkedin**: https://www.linkedin.com/in/lim-hyo-jeong/