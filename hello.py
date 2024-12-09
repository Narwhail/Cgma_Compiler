import streamlit as st # type: ignore
import testimport
import lexer

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")

column_height = 400
col1, col2 = st.columns(2)
with col1:
    with st.container(height=column_height, border=True):
        textAreaInput = st.text_area(height=column_height-120, label="Code", placeholder="Enter code...")
        st.button("Run Lexical Analyzer")

with col2:
    with st.container(height=column_height, border=True):
        # st.write("Lexical Analyzer")
        # array tuple format: lexeme(string), token(string), line(int), column(line)
        # textExample = [("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0),("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0)]
        textExample = lexer.analyzeLexical(textAreaInput)
        for lexeme, token, line, char in textExample:
            st.write(f"Line {line}, Column {char}. Lexeme **{lexeme}** has a token of **{token}**.")

with st.container(border=True):
    st.write("Code has no error!")