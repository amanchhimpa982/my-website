import streamlit as st
import requests
import os

# Page Config
st.set_page_config(page_title="AI Chatbot", layout="wide")

# Sidebar - Language Selection
st.sidebar.title("Chat Settings")
language = st.sidebar.radio("Select Output Language:", ("English", "Hindi"))

# UI Text based on language
title_text = "🤖 AI Chatbot Created by aman chhimpa" if language == "English" else "🤖 AI चैटबॉट असिस्टेंट"
placeholder_text = "Type your message..." if language == "English" else "अपना संदेश लिखें..."

st.title(title_text)

# Secret fetch
API_KEY = os.getenv("SARVAM_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input(placeholder_text):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if API_KEY:
        try:
            # Direct Answer Logic: We tell the AI to be concise and direct
            system_instruction = (
                f"Give direct and concise answers in {language}. "
                "Do not introduce yourself or use filler words. "
                "Answer the user's question immediately."
            )

            headers = {"api-subscription-key": API_KEY}
            payload = {
                "model": "sarvam-m",
                "messages": [
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": prompt}
                ]
            }
            
            with st.spinner("Thinking..."):
                response = requests.post("https://api.sarvam.ai/v1/chat/completions", json=payload, headers=headers)
            
            if response.status_code == 200:
                answer = response.json()['choices'][0]['message']['content']
                with st.chat_message("assistant"):
                    st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("Error: Could not reach AI server.")
        except Exception as e:
            st.error(f"System Error: {e}")
    else:
        st.warning("sk_fp9o826m_3u0qiuDROrxXBt4OX7xygLa5")