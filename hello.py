import streamlit as st

st.set_page_config(page_title="Cgma Compiler", layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.title("Cgma Compiler")
    st.write("Lexical Analyzer")

    st.button("Run Lexical Analyzer")

with col2:
    with st.container(border=True):
        st.write("Test Lexeme and token")