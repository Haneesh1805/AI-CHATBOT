import streamlit as st
from chatbot import get_chain

st.set_page_config(page_title="ChatGPT Lite", page_icon="🤖")
st.title("🤖 AI Chatbot with Memory")

if "chain" not in st.session_state:
    st.session_state.chain = get_chain()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history[::-1]:
    st.write(f"**{sender}:** {message}")
