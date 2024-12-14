from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_qdrant import QdrantVectorStore


def generateResponse(data,userQuery):
    embedding_model = OllamaEmbeddings(model="llama3.2") 
    qdrant = QdrantVectorStore.from_documents(
    documents=data,
    embedding=embedding_model,
    path="./tmp/local_qdrant",
    collection_name="pdf_data",
    force_recreate = "true"
    )
    retriever = qdrant.as_retriever()
    llm = ChatOllama(model="llama3.2")
    query = userQuery
    system_prompt = (
    "You are a helpful AI assistant called AyuBuddy, you specialize in answer ayurveda related questions."
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentence maximum and keep the answer concise. "
    "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),])
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)

    result = chain.invoke({"input": query})
    print(result['answer'])
    return result['answer']



