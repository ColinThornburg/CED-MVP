import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.agents import Tool
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pydantic.v1 import BaseModel, Field
import pandas as pd
import os

# Define the input model for documents
class DocumentInput(BaseModel):
    question: str = Field()
st.set_page_config(layout="wide")
# Streamlit app title
st.title('CED Development for Southeastern Indiana Regional Planning Commission')

# Initialize the language model
### models: https://platform.openai.com/docs/models/gpt-3-5-turbo
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)  # Ensure this model supports OpenAI Tools

# Define the files to load
files = [
    {
        "name": "SIDC",
        "path": "multi_pdf/CED-SIDC.pdf",
    },
    {
        "name": "SIRPC",
        "path": "CED-SIRPC.pdf",
    },
    {
        "name": "Template",
        "path": "SWOT-Template.pdf",
    },
]

tools = []

# Load and process each file
for file in files:
    loader = PyPDFLoader(file["path"])
    pages = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    retriever = FAISS.from_documents(docs, embeddings).as_retriever()

    # Create a Custom Document Retrieval Tool for each file
    tools.append(
    Tool(
        args_schema=DocumentInput,
        name=file["name"],
        description=f"useful when you want to answer questions about {file['name']}",
        func=RetrievalQA.from_chain_type(llm=llm, retriever=retriever),
    )
)

# Get the prompt for the OpenAI Tools agent
### https://smith.langchain.com/hub/hwchase17/openai-tools-agent --> I don't have a deep understanding of this
prompt = hub.pull("hwchase17/openai-tools-agent")

# Construct the OpenAI Tools agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Function to invoke the agent with the user's question
def get_response(question):
    response = agent_executor.invoke({"input": question})
    return response

# Labor Force Assessment Button
if st.button('Labor Force Assessment'):
    # Display the hardcoded analysis
    analysis_text = """
    The area's labor force represents 7.8% of the state's total, indicating it's a significant contributor to Indiana's economy. Both the total resident labor force and employment rates align with this percentage, showing a proportional representation in the state's overall employment landscape.

    Notably, the area has a lower unemployment rate compared to the state average, suggesting a relatively strong labor market. The area ranks first in these metrics, reflecting a leading position in employment health relative to other regions in Indiana.
    """
    st.write(analysis_text)

# Layout for text editor and LLM chat
col1, col2 = st.columns([3, 1])

# Large text editor in the first column
with col1:
    user_report = st.text_area('Write your SWOT Analysis here:', height=300)  # Increase height as needed

# LLM chat in the second column
with col2:
    # User input for the question
    user_question = st.text_input('Enter your question:', 'Compare and contrast the economic regional strengths between the SIRPC and SIDC?')

    # When the user submits a question
    if st.button('Submit'):
        with st.spinner('Fetching the answer...'):
            # Get the response from the agent
            response = get_response(user_question)
            # Display the response
            st.write('### Response:')
            st.json(response)  # Format and display the JSON response