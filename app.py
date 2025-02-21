import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory

# Step 1: Define the AI Agent’s Goal
# The agent should take a user query, search for relevant web articles and research papers,
# summarize key points, and generate a short report or slides.

# Load API keys securely
load_dotenv()

# Set API keys
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

os.environ["GOOGLE_API_KEY"] = ""
os.environ["SERPAPI_API_KEY"] = ""


# Step 2: Set Up the Agent
# Use LangChain’s AgentExecutor with tools like SerpAPI (for web search) and Gemini (for summarization).

# Initialize LLM
llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.3)

# Initialize Search Tool
search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))
search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Search the web for information on a given topic"
)

# Memory to track conversations
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the Agent
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)


# Step 3: Implement the AI Pipeline
# - Take a user query as input
# - Search the web for relevant articles
# - Summarize each article using LLM
# - Store results in a vector database
# - Generate a final structured response

def research_assistant(query):
    # Search and summarize information
    response = agent.run(query)

    # Store summarized response in vector database
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_db = FAISS.from_texts(response, embedding=embedding_model)
    vector_db.save_local("faiss_index_store")
    # Generate structured response
    summary = {
        "query": query,
        "response": response
    }

    return summary, vector_db


# Step 4: Deploy a Simple UI
# - Create a minimal Streamlit web app
# - Allow users to input queries and get AI-generated reports

st.title("Agentic AI Research Assistant")
query = st.text_input("Enter your research topic:")
if st.button("Generate Summary"):
    result, vector_db = research_assistant(query)
    st.subheader("AI Research Summary:")
    st.write(result["response"])
