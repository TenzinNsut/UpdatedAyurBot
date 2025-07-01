# Import necessary modules
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from huggingface_hub import InferenceClient

import re

# Load environment variables
load_dotenv()


# Function to generate bot response
def generateResponse(userQuery):
    
    # ✅ Simple greetings detection
    print("generateResponse called with:", userQuery, flush=True)
    greetings = ["hi", "hello", "hey", "namaste", "hii", "hai"]
    if userQuery.lower().strip() in greetings:
        return (
            "👋 Hi there! I'm **AyurBot**, your friendly assistant for Ayurveda and holistic wellness.\n"
            "Ask me anything about remedies, herbs, diet, body types, or general health!"
        )

    print("Setting up embedding model...", flush=True)
    # ✅ Set up embedding model for document search
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5",
        model_kwargs={'device': 'cpu'}
    )

    print("Setting up Pinecone...", flush=True)
    # ✅ Set up Pinecone vector store
    index_name = "ayur-index"
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(index_name)

    print("Setting up vectorstore...", flush=True)
    vectorstore = PineconeVectorStore(
        index=index,
        embedding=embedding_model
    )
    retriever = vectorstore.as_retriever()

    print(f"User Query: {userQuery}")

    print("Retrieving relevant documents...", flush=True)
    # ✅ Retrieve relevant context from documents
    # docs = retriever.get_relevant_documents(userQuery)
    docs = retriever.invoke(userQuery)
    context_text = "\n".join([doc.page_content for doc in docs]) if docs else "No context found."


    system_prompt = (
    "You are 'AyurBot', a friendly and knowledgeable Ayurveda assistant.\n\n"
    "🎯 Your job is to provide helpful, practical, and easy-to-understand Ayurvedic advice with a warm, approachable tone.\n\n"
    "✅ Vary your language and phrasing to avoid sounding repetitive or robotic.\n"
    "✅ Use emojis naturally to make the response engaging (like 🌿 for herbs, 🚨 for warnings, 🌱 for remedies, etc.).\n"
    "✅ Provide clear, actionable advice on Ayurveda — diet, herbs, remedies, body types (doshas), etc.\n"
    "✅ You can organize information with bullet points, but always keep the tone friendly and conversational.\n"
    "✅ DO NOT over-explain your reasoning or describe your thought process.\n"
    "✅ Do NOT include system tags like '<think>', '<p>', etc. Keep the final response clean.\n"
    "✅ If you lack context or can't answer, politely say: 'I'm sorry, I don't have that information right now.'\n\n"
    "Here is some context from the user's question or documents:\n{context}\n\n"
    "Based on that, reply naturally, clearly, and in a way that feels human and helpful. Vary your style, but keep it friendly and practical."
    )





    # ✅ Raw HuggingFace InferenceClient for chat
    client = InferenceClient(
        provider="novita",
        api_key=os.getenv("HUGGINGFACE_API_KEY")
    )

    completion = client.chat.completions.create(
        model="Qwen/Qwen3-32B",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": userQuery}
        ]
    )

    bot_response = completion.choices[0].message.content
    
    # bot_response = clean_bot_response(bot_response)
    bot_response = re.sub(r"<think>.*?</think>", "", bot_response, flags=re.DOTALL).strip()

    print(f"Bot Response: {bot_response}")

    return bot_response
