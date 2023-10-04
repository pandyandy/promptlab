# improve_prompt.py

import streamlit as st

from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models import ChatOpenAI

from functions.best_practices import best_practices_var

MODEL_NAME = "gpt-4"
MAX_TOKENS = 2000
DEFAULT_TEMP = 0.25

# Improve user input
def get_improved_input(user_input, temperature):
    llm = ChatOpenAI(model=MODEL_NAME, temperature=temperature, max_tokens=MAX_TOKENS)
    messages = [
        SystemMessage(
<<<<<<< Updated upstream
            content=(
                """
You create precise, detailed and accurate prompts containing a guidance what to do and what not. Most of the time you use a few-shot example to make your prompts even better, this is specially valuable for achieving correctly formatted result.
You are given one prompt at a time and improve it while keeping all of its meaning. Prefer JSON as output format. Describe the importance to suppress all explanations or anything else but the JSON output.

Your output is always just an improved prompt starting with ###Task: and ending with single ``` to allow for appending the input. Provide a few shot example (100 - 500 words) in the improved prompt if you see fit.

Here are two examples of request response.
prompt:'Extract dates from the text.'
response:'###Task: Extract Dates from Text
You are given a document that contains dates. Extract all the dates from the document and return them as a JSON array. 

Example document:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum convallis elit enim, eu congue velit porta et. Mauris nec rutrum velit, non eleifend sapien. From 2020-01-05 to now.

Investors:
1. Investor 1 (2022/11/01)
2. Investor 2 (1.7.2008)
3. Three (03/03/1980)
Example output: {"dates":["2020-01-05", "2022/11/01", "1.7.2008", "03/03/1980"]}
```
'
##
prompt:'Extract dates from the text.',
response:'###Task: Extract Dates from Text
You are given a document that contains dates. Extract all the dates from the document and return them as a JSON array. 
Example document:
From 2020-01-05 everything should be in blue color. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum convallis elit enim, eu congue velit porta et. Mauris nec rutrum velit, non eleifend sapien. Till 03/03/1980 it was all just fun.
Example output: {"dates":["2020-01-05", "03/03/1980"]}
```'

You follow prompting best practices in your responses.
Prompting best practices:
## Rules of Thumb and Examples

- **Instruction Placement**: 
  - Less effective: "Translate the following English text into French: 'Hello, how are you?'"
  - Better: 
    ```
    ###
    Translate the following English text into French
    'Hello, how are you?'
    ```

- **Detail & Specificity**: 
  - Less effective: "Write about cats."
  - Better: "Write a 150-word article about the domestication history of cats."

- **Show & Tell**: 
  - Less effective: "Provide a summary."
  - Better: "Summarize the content in 3 sentences, highlighting the main points."

- **Prefer Few-shot where possible**: 
  - Zero-shot 
  - Few-shot - provide one or a couple of examples

- **Avoid Fluff**: 
  - Less effective: "Can you maybe, if it's not too much trouble, write a poem about the sea?"
  - Better: "Write a 4-line poem about the sea."

- **State the Positive**: 
  - Less effective: "Don't write a sad story."
  - Better: "Write a joyful story."

- **Code Generation Hints**: 
  - Less effective: "Write a function to add numbers."
  - Better: 
    ```
    import
    Write a Python function to add two numbers.
    ```
"""
            )
        ),
        HumanMessagePromptTemplate.from_template("'{text}'"),
    ])

    models = [
        "gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613", 
        "gpt-4", "gpt-4-0613", "gpt-4-32k", "gpt-4-32k-0613"
    ]
    
=======
            content=best_practices_var
            ),
         HumanMessage(
             content=user_input
             ),
    ]    
    return llm(messages)

def clear_text():
    st.session_state["text_improve"] = ""

# Get user input and return improved
def improve_prompt_ui():
>>>>>>> Stashed changes
    st.markdown(f'<h3 style="border-bottom: 2px solid #288CFC; ">{"Improve"}</h3>', 
                unsafe_allow_html=True)
    st.text(" ")
    st.markdown("🛠️ Already have ideas but still unsure about the wording of your current prompt? Enter your idea, hit the __'Improve'__ button and voilà! You'll get an improved version that follows prompt engineering best practices.")
    
    with st.chat_message("user", avatar="💬"):
        col1, col2 = st.columns([7, 1])
        with col1: 
            user_input = st.text_area("User input", label_visibility="collapsed", key="text_improve")
        with col2: 
            improve = st.button("Improve", use_container_width=True)
            reset = st.button("Reset", use_container_width=True, on_click=clear_text)
        
        with st.expander("__Set the temperature__"):
            col1, _, _ = st.columns(3)
            temp_prompt = col1.slider("Temperature", min_value=0.0, max_value=1.0, value=DEFAULT_TEMP, 
                                        help="Lower values for temperature result in more consistent outputs, while higher values generate more diverse and creative results. Select a temperature value based on the desired trade-off between coherence and creativity for your specific application.", 
    ) 
    
        if improve and user_input:
            improve_state = st.text("")
            improved_input = get_improved_input(user_input, temp_prompt)
            st.session_state.improved_content = improved_input.content
            improve_state.warning("If you use the improved prompt, the best practice is to place your input data after the backticks.", icon="💡")
                
        if reset: 
            st.session_state.improved_content = ""

        if "improved_content" in st.session_state:
            st.code(st.session_state.improved_content, language="http")
<<<<<<< Updated upstream
=======

def improve_prompt():
    if 'improved_content' not in st.session_state:
        st.session_state.improved_content = ""
    
    improve_prompt_ui()
>>>>>>> Stashed changes
