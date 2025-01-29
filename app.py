import streamlit as st
from deepseek_agent import DeepSeekAgent
import os

# Initialize agent
@st.cache_resource
def init_agent():
    return DeepSeekAgent()

# Configure UI
st.set_page_config(page_title="DeepSeek Assistant", layout="wide")
st.title("🤖 DeepSeek AI Agent")

# Sidebar Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("API Key", type="password")
    if api_key:
        os.environ["DEEPSEEK_API_KEY"] = api_key
    st.markdown("[Get API Key](https://platform.deepseek.com/api-keys)")

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        agent = init_agent()
        response = agent.chat(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

