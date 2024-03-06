
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

load_dotenv()

API_KEY = os.environ["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"]

llm = OpenAI(api_token=API_KEY)

import matplotlib.pyplot as plt
from PIL import Image
st.title("Prompt-driven analysis with OpenAI")


uploaded_file = st.file_uploader("Upload a csv file to analysis", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
     
    prompt = st.text_area("Enter Your Prompt:")
    
    generate = st.button("Generate")
    
    if generate:
        if prompt:
            #st.write("OpenAI is generating an answer, please wait...")
            with st.spinner("OpenAI is generating an answer, please wait..."):
                #st.write(pandas_ai.run(df, prompt=prompt))
                df = SmartDataframe(df, config={"llm": llm})
                st.write(df.chat(prompt))
            
        else:
            st.warning("Please upload a csv file and enter your prompt")

