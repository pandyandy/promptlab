### DISCLAIMER: I never said it was good code, it just somehow works 🫠
 
import streamlit as st
import pandas as pd
import openai
import base64
import os

from functions.show_data_info import show_data_info
from functions.improve_prompt import improve_prompt
from functions.run_prompts_app import run_prompts_app

from src.st_aggrid.st_aggrid import interactive_table

image_path = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="PromptLab",
    layout="wide"
    )

logo_image = image_path+"/static/keboola_logo.png"
logo_html = f'<div style="display: flex; justify-content: flex-end;"><img src="data:image/png;base64,{base64.b64encode(open(logo_image, "rb").read()).decode()}" style="width: 100px; margin-left: -10px;"></div>'

st.title('PromptLab 👩🏻‍🔬')
 
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key:',
    help= """
    You can get your own OpenAI API key by following these instructions:
    1. Go to https://platform.openai.com/account/api-keys.
    2. Click on the __+ Create new secret key__ button.
    3. Enter an identifier name (optional) and click on the __Create secret key__ button.
    """,
    type="password",
    )

os.environ["OPENAI_API_KEY"] = openai_api_key
openai.api_key = openai_api_key

upload_option = st.sidebar.selectbox('Select an upload option:', 
                                    ['Upload a CSV file'
                                     # 'Use Demo Dataset'
                                     ]
 )

if upload_option == 'Upload a CSV file':
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if 'uploaded_file' not in st.session_state:
        st.session_state['uploaded_file'] = None
    uploaded_file = st.session_state['uploaded_file'] 

def main():

    if uploaded_file:
        
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("The table has been successfully uploaded.")
        
        show_data_info(df)
        if st.session_state['uploaded_file'] is not None:
            interactive_table()

        if not openai_api_key:
            st.warning("To continue, please enter your OpenAI API Key.", icon="⚠️")
            
        improve_prompt()
        run_prompts_app(df)
        
        st.text(" ")
        st.markdown(f"{logo_html}", unsafe_allow_html=True)
    
    else:
        st.warning("Please upload a table.", icon="⚠️")
    
if __name__ == "__main__":
    main()