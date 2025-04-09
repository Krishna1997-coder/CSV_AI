import streamlit as st
import os
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI

# Read API key from Streamlit secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

def main():
    st.set_page_config(page_title="CSV Analyst AI", layout="wide")
    st.title("📊 CSV Analyst with AI")

    uploaded_file = st.file_uploader("Upload your CSV", type="csv")
    if uploaded_file:
        with st.spinner("Analyzing CSV..."):
           agent = create_csv_agent(
    OpenAI(temperature=0, openai_api_key=openai_api_key),
    uploaded_file,
    verbose=True,
    allow_dangerous_code=True
)


        st.success("CSV Loaded. Ask me anything!")
        query = st.text_input("Ask a question about your data:")
        if query:
            with st.spinner("Thinking..."):
                response = agent.run(query)
                st.write(response)

if __name__ == "__main__":
    main()
