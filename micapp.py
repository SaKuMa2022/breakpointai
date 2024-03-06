import streamlit as st
import pandas as pd

from pandasai import SmartDataframe
from pandasai.llm import OpenAI
llm = OpenAI(api_token="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")


import matplotlib.pyplot as plt
from PIL import Image
st.set_page_config(
    page_title="AI assited app",
    layout="wide",
    initial_sidebar_state="expanded"
)
styles = """
<style>
img {
    max-width: 50%;
}
.sidebar .sidebar-content {
    background-color: #f5f5f5;
}
</style>
"""

st.sidebar.title('Datainsight')    
st.sidebar.subheader('AI Insights')
header = st.container()

with header:
    st.title("AI-Analysis App")
    st.markdown("Use this  app to analyze your MIC data in one shot. You can upload your data and ask questions about it. The app will answer your questions and provide you with insights about your data.")
    
# Define main content
content = st.container()
with content:
    # Load sales dataset
    sale_file = st.file_uploader('Upload a CSV file', type=['csv'])
    if sale_file is not None:
        df = pd.read_csv(sale_file, encoding='latin-1')
        sdf = SmartDataframe(df, config={"llm": llm})
        st.dataframe(df)
        query = st.text_input(label='Enter your query')
        Analyze = st.button(label='Analyze')
        if Analyze:
            result = sdf.chat(query)
            print(result)
            st.write(result)
    else:
        st.warning("Please select a CSV file to continue.")
        st.stop()
