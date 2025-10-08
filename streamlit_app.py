import streamlit as st
import requests

st.set_page_config(page_title="Streamlit Chat with API", page_icon="💬")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 AI Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter full name of the person you want to find..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    data = ""

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        url = f"http://127.0.0.1:8000/ai-assistant/help?query={prompt}"
        response = requests.post(
            url,
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        reply = f"❌ API Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": data})
    with st.chat_message("assistant"):
        st.json(data)
