import streamlit as st
from deepseek_agent import DeepSeekAgent  # Changed import
import os

# Initialize agent
@st.cache_resource
def init_agent():
    return DeepSeekAgent()  # Changed class name

# Configure UI
st.set_page_config(page_title="Claude AI Assistant", layout="wide")  # Changed title
st.title("🤖 Trojan AI Agent")  # Changed header

# Sidebar Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("sk-10a0cffbb30e42f0a1a18403dd9700e9", type="password", 
                          help="sk-10a0cffbb30e42f0a1a18403dd9700e9")  # Changed key name
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key  # Changed environment variable
    st.markdown("[Get API Key](https://console.anthropic.com/settings/keys)")  # Changed link

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Weti you wan ask me?..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        agent = init_agent()
        response = agent.chat(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

