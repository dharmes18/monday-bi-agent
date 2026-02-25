import streamlit as st
import requests

st.set_page_config(page_title="Monday BI Agent", layout="wide")

st.title("📊 Monday.com Business Intelligence Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask a business question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI backend
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"q": prompt}
    )

    answer = response.json()["answer"]

    # Clean formatting for UI
    answer = answer.replace("\\n", "\n")

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)