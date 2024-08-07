# pip install streamlit langchain lanchain-openai beautifulsoup4 python-dotenv chromadb

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
# Logic of chatbot
def get_response(user_input):
   return "I don't know"


# app config
st.set_page_config(page_title="Kino Screenings Scheduler AI", page_icon="🎬")
st.title("Kino AI")
if "chat_history" not in st.session_state:
 st.session_state.chat_history = [
   AIMessage(content="Hello, I'm your Cinema AI, how can I help you?"),
 ]

# sidebar
with st.sidebar:
    st.header("Chat options")
    website_url = st.text_input("What is the name of your Cinema?")


# User input
user_query = st.chat_input("Ask your question here")
if user_query is not None and user_query != "":
 response = get_response(user_query)
 st.session_state.chat_history.append(HumanMessage(content=user_query))
 st.session_state.chat_history.append(AIMessage(content=response))


# CONVERSATION 

for message in st.session_state.chat_history:
 if isinstance(message, AIMessage):
    with st.chat_message("AI"):
      st.write(message.content)
 elif isinstance(message, HumanMessage):
     with st.chat_message("Human"):
      st.write(message.content)