import streamlit as st # type: ignore
import lexical.lexer as lexer

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")
st.write("A lexical analyzer and syntax analyzer for a new programming language based on C. In compliance for the Automata Theory & Formal Languages.")

column_height = 400
col1, col2 = st.columns(2)
with col1:
    with st.container(height=column_height, border=True):
        textAreaInput = st.text_area(height=column_height-120, label="Code", placeholder="Enter code...")
        if st.button("Run Lexical Analyzer"):
            buttonInput = textAreaInput

with col2:
    with st.container(height=column_height, border=True):
        st.subheader("Lexical Analyzer")
        # array tuple format: lexeme(string), token(string), line(int), column(line)
        # textExample = [("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0),("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0)]

        lexicalResult = lexer.analyzeLexical(buttonInput)

        for lexeme, token, line, column in lexicalResult:
            st.write(f"Line {line}, Column {column}. Lexeme **{lexeme}** has a token of **{token}**.")

with st.container(border=True):
    st.subheader("Syntax Analyzer")
    st.write("Code has no error!")