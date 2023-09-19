# improve_prompt.py

import streamlit as st

from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

def improve_prompt():

    if 'improved_content' not in st.session_state:
        st.session_state.improved_content = ""
    
    if 'last_user_input' not in st.session_state:
        st.session_state.last_user_input = ""

    template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                """
As a prompt engineer, you know the best practices for prompt engineering. You create precise, detailed and accurate prompts while giving a guidance what to do and what not. Most of the time you use a few-shot example to make your prompts even better, this is specially valuable for achieving correctly formatted result.
You are given one prompt at a time and improve it while keeping all of its meaning. Preffer JSON as output format. Describe the importance to suppress all explanations or anything else but the JSON output.

Prompting best practices:
# Guide to Prompt Perfection with OpenAI API

## Rules of Thumb and Examples

- **Instruction Placement**: 
  - Less effective ❌: "Translate the following English text into French: 'Hello, how are you?'"
  - Better ✅: 
    ```
    ###
    Translate the following English text into French
    'Hello, how are you?'
    ```

- **Detail & Specificity**: 
  - Less effective ❌: "Write about cats."
  - Better ✅: "Write a 150-word article about the domestication history of cats."

- **Show & Tell**: 
  - Less effective ❌: "Provide a summary."
  - Better ✅: "Summarize the content in 3 sentences, highlighting the main points."

- **Prefer Few-shot where possible**: 
  - ✅ Zero-shot 
  - ✅ Few-shot - provide one or a couple of examples

- **Avoid Fluff**: 
  - Less effective ❌: "Can you maybe, if it's not too much trouble, write a poem about the sea?"
  - Better ✅: "Write a 4-line poem about the sea."

- **State the Positive**: 
  - Less effective ❌: "Don't write a sad story."
  - Better ✅: "Write a joyful story."

- **Code Generation Hints**: 
  - Less effective ❌: "Write a function to add numbers."
  - Better ✅: 
    ```
    import
    Write a Python function to add two numbers.
    ```

## Additional Tips

- **Prompt Formats**: Different formats may align better with tasks. For instance, a conversational format might work best for chatbots, while a directive format suits data extraction.

Your output is always just an improved prompt.
Example input prompt to improve: Extract dates from the text.
Example improved prompt (your output):
###
Task: Extract Dates from Text

You are given a document that contains dates. Extract all the dates from the document and return them as a JSON array.

Example document:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum convallis elit enim, eu congue velit porta et. Mauris nec rutrum velit, non eleifend sapien. From 2020-01-05 to now.

Investors:
1. Investor 1 (2022/11/01)
2. Investor 2 (1.7.2008)
3. Tři (03/03/1980)
Example output: {"dates":["2020-01-05", "2022/11/01", "1.7.2008", "03-03/1980"]}
```

Please make sure that you accurately extract the dates from the document and return them as an array.
"""
            )
        ),
        HumanMessagePromptTemplate.from_template("'{text}'"),
    ])

    models = [
        "gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613", 
        "gpt-4", "gpt-4-0613", "gpt-4-32k", "gpt-4-32k-0613"
    ]
    
    st.markdown(f'<h3 style="border-bottom: 2px solid #288CFC; ">{"Improve"}</h3>', 
                unsafe_allow_html=True)
    st.text(" ")
    st.write('Already have ideas but still not sure about the wording of your current prompt?')
    
    with st.chat_message("user", avatar="💬"):
        col1, col2 = st.columns([7, 1])
        with col1: 
            user_input = st.text_input("", label_visibility="collapsed")
        with col2: 
            improve = st.button("Improve", use_container_width=True)
        
        with st.expander("__Improve prompt parameters setting__"):
            col1,col2,col3 = st.columns(3) 
            model_prompt = col1.selectbox("Model", models)
            tokens_prompt = col2.number_input("Max tokens", min_value=0, value=150)
            temp_prompt = col3.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2) 
        
        if improve:
            if user_input:
                llm = ChatOpenAI(model=model_prompt, temperature=temp_prompt, max_tokens=tokens_prompt)
                improved_input = llm(template.format_messages(text=user_input))
                
                st.session_state.improved_content = improved_input.content
                st.session_state.last_user_input = user_input
            
        if "improved_content" in st.session_state:
            st.write(st.session_state.improved_content)
