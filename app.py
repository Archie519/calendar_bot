# app.py
import streamlit as st

st.title("📅 AI Calendar Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    bot_reply = f"📅 Got it! You said: {user_input}"  # Mock response
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}**: {msg}")
