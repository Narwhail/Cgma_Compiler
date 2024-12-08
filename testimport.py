import streamlit as st # type: ignore

def writeLexicalAnalysis(userInput):
    for x in userInput:
        st.write(x)