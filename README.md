# AyurBot: AI-Powered Ayurveda Chatbot

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models & Technologies Used](#models--technologies-used)

## Introduction
AyurBot is an interactive AI-powered chatbot designed to provide users with practical, friendly, and easy-to-understand advice on Ayurveda and holistic wellness. Leveraging Retrieval-Augmented Generation (RAG), semantic search, and large language models (LLMs), AyurBot analyzes user queries and retrieves relevant information from a curated knowledge base of Ayurvedic texts and resources.

The core components of AyurBot include:
- A knowledge base built from authentic Ayurvedic documents (e.g., medical books in PDF format)
- Embedding and semantic indexing of the knowledge base for efficient search
- Pinecone, a cloud vector database for similarity search
- A query embedding and search module to find the most relevant information
- An LLM for generating clear, actionable, and engaging responses

## System Overview and Methodology

### 1. Knowledge Base Creation
Text content is extracted from Ayurvedic documents (PDFs) and split into manageable chunks for efficient processing using LangChain utilities.

### 2. Embedding and Semantic Indexing
Text chunks are converted into vector representations using a state-of-the-art embedding model. These vectors are stored in Pinecone for fast similarity search.

### 3. User Query Processing
User queries are embedded and matched against the indexed knowledge base to find the most relevant information.

### 4. Answer Retrieval and Generation
Relevant chunks are retrieved and passed to a large language model, which generates a concise, user-friendly, and engaging response based on the user's question and the retrieved context.

## Features
- Friendly, conversational Ayurveda assistant (AyurBot)
- Natural language understanding and processing
- Semantic search for relevant information retrieval from Ayurvedic texts
- Generative, actionable responses using a large language model
- User-friendly web interface with real-time chat
- Engaging responses with emojis and practical advice

## Installation
To run AyurBot locally, follow these steps:

1. Clone the repository:
   ```
   git clone <your-repo-url>
   ```

2. Install the required dependencies:
   ```
   # Create a virtual environment (optional but recommended)
   python -m venv ayurbotEnv
   # Activate the environment and install dependencies
   pip install -r requirements.txt
   ```

3. Set up the necessary environment variables in a `.env` file:
   - `PINECONE_API_KEY` and `PINECONE_ENV`: For Pinecone vector database access
   - `HUGGINGFACE_API_KEY`: For HuggingFace Inference Endpoint access

4. Index the documents (if not already indexed):
   ```
   python index_documents.py
   ```

5. Run the application:
   ```
   python main.py
   ```

6. Access the web interface through the provided URL (default: http://localhost:8080).

## Usage
Interact with AyurBot by typing your questions about Ayurveda, such as:
- "What are the best herbs for immunity?"
- "Suggest Ayurvedic remedies for stress."
- "Explain the three doshas."
- "What is a good Ayurvedic diet for Pitta body type?"

AyurBot will analyze your query, retrieve relevant information from its knowledge base, and provide a friendly, practical, and engaging response.

## Models & Technologies Used
- **Embedding Model:** [`BAAI/bge-large-en-v1.5`](https://huggingface.co/BAAI/bge-large-en-v1.5) (HuggingFace)
- **LLM:** [`Qwen/Qwen3-32B`](https://huggingface.co/Qwen/Qwen3-32B) (HuggingFace Inference Endpoint)
- **Vector Database:** [Pinecone](https://www.pinecone.io/)
- **Frameworks/Libraries:** Flask, LangChain, dotenv, sentence-transformers, PyPDF

---

AyurBot makes Ayurveda accessible, engaging, and easy to explore. For any questions or contributions, please open an issue or pull request!
