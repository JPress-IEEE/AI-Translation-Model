import os
import pandas as pd
import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Set up the Google API key for generative AI
os.environ['GOOGLE_API_KEY'] = "AIzaSyAy8zc0RgndnNyINoM2YAOBEgGpgf-_Onk"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Initialize the language model for chat
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Define the prompt template for translation
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following text to English:\n\n{input_text}"
)

# Create a chain for the translation task
chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")

# Set up the Streamlit app
st.title("Text Translation App")

# Text area for user input
text_to_translate = st.text_area("Enter text to translate:")

# Button to trigger translation
if st.button("Translate"):
    if not text_to_translate:
        st.error("No input text provided")
    else:
        # Run the translation chain
        result = chain_one.run(input_text=text_to_translate)
        st.write("Translated text:", result)
