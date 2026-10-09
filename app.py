
import os
import streamlit as st
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

st.set_page_config(page_title="Ektha AI", page_icon="💬")
st.title("💬 Ektha AI")
st.caption("Your personal AI assistant")

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("API key not found. Please set OPENROUTER_API_KEY in PowerShell.")
    st.stop()

@st.cache_resource
def create_chatbot(key):
    return ChatOpenRouter(
        model="openai/gpt-4o-mini",
        api_key=key,
        temperature=0.7,
        max_tokens=500
    )

bot = create_chatbot(api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Message Ektha...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    history = [
        SystemMessage(
            content="You are Ektha, a friendly and helpful AI assistant."
        )
    ]

    for message in st.session_state.messages:
        if message["role"] == "user":
            history.append(HumanMessage(content=message["content"]))
        else:
            history.append(AIMessage(content=message["content"]))

    with st.chat_message("assistant"):
        with st.spinner("Ektha is thinking..."):
            try:
                response = bot.invoke(history)
                answer = response.content
                if not isinstance(answer, str):
                    answer = str(answer)

                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as error:
                st.error(f"Something went wrong: {error}")
