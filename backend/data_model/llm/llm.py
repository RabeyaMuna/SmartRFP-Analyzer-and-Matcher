from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import AzureBlobStorageFileLoader
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

container_name = os.getenv("AZURE_BLOB_CONTAINER")
conn_str = os.getenv('AZURE_BLOB_CONNECTOR')

# Define template for prompts
template_rfp_v1_a = """As RFP contact and Head of Executive Leadership find and show {expert_roles} in not more than two three words, for the entire RFP (Request for Proposal) from the given {context}."""
prompt = ChatPromptTemplate.from_template(template_rfp_v1_a)

# LLM Initialization
llm = AzureChatOpenAI(
    model=os.getenv("AZURE_OPENAI_MODEL"),
    azure_endpoint=os.getenv("AZURE_OPENAI_MODEL"), 
    api_key=os.getenv("API_KEY"),
    api_version=os.getenv("API_VERSION")
)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs) 

#RAG Pipeline Creation
def create_rag_chain(blob_name):
    loader = AzureBlobStorageFileLoader(
        conn_str=conn_str,
        container=container_name,
        blob_name=blob_name,
    )

    loader_r = loader.load() 

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    docs = text_splitter.split_documents(loader_r)

    ChromaDB_about_Inspire_RFP_Dexian_DISYS_Response_v1 = Chroma.from_documents(
        documents=docs, 
        embedding=embedding_function, 
        persist_directory='ChromaDB_temp'
    )

    retriever = ChromaDB_about_Inspire_RFP_Dexian_DISYS_Response_v1.as_retriever()

    rag_chain = (
        {"context": retriever | format_docs, "expert_roles": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

def fn_rag_infer(user_query, blob_name):
    rag_chain = create_rag_chain(blob_name)
    result = rag_chain.invoke(user_query)
    return result
