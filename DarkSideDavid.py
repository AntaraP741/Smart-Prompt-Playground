from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.9
)

st.title("Dark Side David Chatbot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content=(
                "You are sweet Dark Side David who gets upset when called "
                "Dark Side David or David. Your real name is Vortex. "
                "You answer in minimal words."
            )
        )
    ]


for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)


prompt = st.chat_input("Say something")

if prompt:
    
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.chat_history.append(HumanMessage(content=prompt))

    
    result = model.invoke(st.session_state.chat_history)
    response = result.content

    st.session_state.chat_history.append(AIMessage(content=response))

    with st.chat_message("      "):
        st.markdown(response)
