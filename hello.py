import streamlit as st # type: ignore
import testimport
import lexer

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")
st.write("Lexical Analyzer")

column_height = 400
col1, col2 = st.columns(2)
with col1:
    with st.container(height=column_height, border=True):
        textAreaInput = st.text_area(height=column_height-120, label="Code", placeholder="Enter code...")
        st.button("Run Lexical Analyzer")

with col2:
    with st.container(height=column_height, border=True):
        st.write("Lexical Analyzer")
        lexicalOutput = [lexer.analyzeLexical(textAreaInput)]
        for line in lexicalOutput:
            st.write = (lexicalOutput[line])

with st.container(border=True):
    st.write("Syntax Analyzer")
    #st.write("Terminal")