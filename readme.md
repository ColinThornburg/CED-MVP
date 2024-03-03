# Comprehensive Economic Development Strategy (CEDS) Assistant

## Overview
This project aims to streamline the creation of a Comprehensive Economic Development Strategy (CEDS) for the Southeastern Indiana Regional Planning Commission. Utilizing advanced AI and language processing technologies, the tool enhances the efficiency of data analysis from multiple regional planning documents.

## Features
- **Document Retrieval**: Automates the extraction of relevant information from multiple PDF documents.
- **Natural Language Processing**: Interprets and answers questions related to economic development strategies using a Large Language Model (LLM) agent.
- **SWOT Analysis Support**: Assists in generating insights into strengths, weaknesses, opportunities, and threats based on regional economic data.

## Technical Details
The project employs the LangChain library, integrating various tools and agents to process and analyze economic data. The LLM agent specifically aids in handling complex queries across multiple documents, ensuring comprehensive and coherent synthesis of information.

## Usage
1. Initialize the Streamlit application.
2. Upload the necessary regional planning PDF documents.
3. Utilize the 'Labor Force Assessment' and other features to extract and analyze economic data.
4. Input queries to receive AI-generated responses based on the uploaded documents.

## Installation
#### Add manual pdf docs (see basecamp chat)
#### pip install -r requirements.txt
#### need to export openai api key as environment variable
#### streamlit run app.py

## Contribution
TODO: Guidelines for contributing to the project, including coding standards, pull request process, etc.



## Resources
https://ibrc.kelley.iu.edu/data-resources/index.html
https://www.stats.indiana.edu/
SIRPC Data Input Source --> https://www.stats.indiana.edu/profiles/profiles.asp?scope_choice=b&county_changer2=Rscied:1

## Colin's thoughts on things that need to get done
#### It's really slow, no caching and it's having to embed the text with each run
#### Prompting is some boilerplate template from langchain docs, prompting is bad
#### More analysis options - right now it's just looking at labor force and it's hardcoded
#### Streamlit is not a robust enough frontend - will need to look at a modern frontend like react/NextJS
#### FAISS is unknown to me - do we need a vector database?
#### Research Perplexity AI for source references?
#### Template Selection - use previous CED or start with best practice