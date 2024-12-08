import streamlit as st
import testimport

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")
st.write("Lexical Analyzer")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        userInput = st.text_input("Enter code")
        st.button("Run Lexical Analyzer")

with col2:
    with st.container(border=True):
        st.write("Test Lexeme and token")

with st.container(border=True):
    testimport.writeTerminal()
    #st.write("Terminal")