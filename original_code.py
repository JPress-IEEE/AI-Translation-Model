import os
import json
import pandas as pd
from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from IPython.display import Markdown
import google.generativeai as genai

# Set up the Google API key for generative AI
os.environ['GOOGLE_API_KEY'] = "AIzaSyAy8zc0RgndnNyINoM2YAOBEgGpgf-_Onk"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Initialize the language model for chat
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Initialize Flask app
app = Flask(__name__)

# Define the prompt template for translation
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following text to English:\n\n{input_text}"
)

# Create a chain for the translation task
chain_one = LLMChain(llm=llm, prompt=first_prompt, output_key="English_Review")


# Function to translate text
def translate_text(text_to_translate):
    if not text_to_translate:
        print("No input text provided")
    else:
        # Run the translation chain
        result = chain_one.run(input_text=text_to_translate)
        print("Translated text:", result)

# Main function to get user input and print the result
if __name__ == '__main__':
    text_to_translate = input("Enter text to translate: ")
    translate_text(text_to_translate)