"""Streamlit chat demo backed by a local Ollama model (no cloud API key needed)."""
import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

load_dotenv()

# Optional LangSmith tracing - only enabled when a key is provided.
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_TRACKING_V2"] = "true"
    os.environ.setdefault("LANGCHAIN_PROJECT", "langchain-ollama-demo")

MODEL = os.getenv("OLLAMA_MODEL", "llama3")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question:{question}"),
    ]
)

st.title(f"LangChain Demo with {MODEL}")
input_text = st.text_input("What question do you have in mind?")

chain = prompt | OllamaLLM(model=MODEL, base_url=BASE_URL) | StrOutputParser()

if input_text:
    try:
        with st.spinner("Thinking..."):
            st.write(chain.invoke({"question": input_text}))
    except Exception as exc:  # connection refused, model not pulled, ...
        st.error(f"Could not get a response from Ollama at {BASE_URL} (model '{MODEL}'): {exc}\n\n"
                 f"Is `ollama serve` running and `ollama pull {MODEL}` done?")
