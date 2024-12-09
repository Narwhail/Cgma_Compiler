import streamlit as st # type: ignore
import lexical.lexer as lexer

error = None

st.set_page_config(page_title="Cgma Compiler", layout="wide")
st.title("Cgma Compiler")
st.write("A lexical analyzer and syntax analyzer for a new programming language based on C. In compliance for the Automata Theory & Formal Languages.")

column_height = 400
col1, col2 = st.columns(2)
with col1:
    with st.container(height=column_height, border=True):
        st.subheader("Code")
        textAreaInput = st.text_area(height=column_height-120, label="", placeholder="Enter code...")

with col2:
    with st.container(height=column_height, border=True):
        st.subheader("Lexical Analyzer")
        # array tuple format: lexeme(string), token(string), line(int), column(line)
        # textExample = [("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0),("chungus", "data_type", 0, 0),("x", "identifier", 0, 8),("=", "assign_op", 0, 9),("10", "int_literal", 0, 10),("hello", "string", 1, 0)]

        result, error = lexer.run("<file>",textAreaInput)


        st.write(result)

with st.container(border=True):
    st.subheader("Syntax Analyzer")

    if error:
        st.write(f"Error: {error}")
    else:
        st.write("Code has no error!")