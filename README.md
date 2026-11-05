# Langchain_Ollama_FastAPI

A hands-on LangChain portfolio: a notebook series covering the full **RAG ingestion pipeline** (loaders → splitters → embeddings → vector stores), plus two small apps — a **LangServe/FastAPI** translation API (Groq) and a **Streamlit chat** app running fully local on **Ollama**.

## Contents
| Path | What it shows |
|---|---|
| `dataIngestion.ipynb` | Document loaders: text, PDF, web pages |
| `textsplitter.ipynb` | Recursive character / token text splitting on `attention.pdf` |
| `openAIembedding.ipynb` | OpenAI embeddings + Chroma vector store |
| `ollamaEmbedding.ipynb` | Local embeddings with Ollama |
| `faiss.ipynb` | FAISS similarity search |
| `simpleLangchainApp.ipynb` | End-to-end retrieval chain over a web page |
| `serve.py` | LangServe REST API (`prompt \| ChatGroq \| parser`) |
| `ollama/app.py` | Streamlit chat app on a local Ollama model |
| `ollama/simplellmLCEL.ipynb` | LCEL basics |
| `speech.txt`, `records.xml`, `attention.pdf` | Sample data used by the notebooks |

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # fill in only the keys you need
```

## Run the apps
**LangServe API (Groq)**
```bash
python serve.py          # http://127.0.0.1:8000/docs  and  /chain/playground
```
**Local chat with Ollama** (no API key; install [Ollama](https://ollama.com) first)
```bash
ollama pull llama3
streamlit run ollama/app.py
```

## Notes
- All secrets are read from `.env` (git-ignored). Never commit API keys into notebooks.
- Notebook outputs may reflect package versions at the time they were run.
