import streamlit as st
import pandas as pd
import os
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI CSV Analyst", layout="wide")
st.title("🤖 CSV Data Analyst with AI")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Save CSV temporarily
    csv_path = "uploaded.csv"
    with open(csv_path, "wb") as f:
        f.write(uploaded_file.read())
    
    # Load CSV with pandas
    df = pd.read_csv(csv_path)
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("💬 Ask questions about your data")

    # Create agent
    if openai_api_key:
        llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
        agent = create_csv_agent(llm, csv_path, verbose=False)

        user_query = st.text_input("Type your question (e.g. 'Which month had highest sales?')")

        if user_query:
            with st.spinner("Analyzing..."):
                response = agent.run(user_query)
                st.success(response)
    else:
        st.warning("⚠️ OpenAI API key not found. Add it to .env file.")
