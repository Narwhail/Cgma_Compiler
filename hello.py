import streamlit as st # type: ignore
import testimport

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")
st.write("Lexical Analyzer")

test = ["""helloo
        worlddd
        aaaa"""]

column_height = 800
col1, col2 = st.columns(2)
with col1:
    with st.container(height=column_height, border=True):
        userInput = st.text_area(label="lexicalAnalyzer", placeholder="Enter code...")
        st.button("Run Lexical Analyzer")

with col2:
    with st.container(height=column_height, border=True):
        testimport.writeLexicalAnalysis(userInput)

with st.container(border=True):
    st.write("Terminal")
    #st.write("Terminal")