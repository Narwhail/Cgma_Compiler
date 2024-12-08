import streamlit as st # type: ignore

def writeLexicalAnalysis(tttext):
    for x in tttext:
        st.write(x)