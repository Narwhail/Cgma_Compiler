import streamlit as st # type: ignore

def analyzeLexical(textInput):
    lines = textInput.splitlines()  # Split input into lines
    tokens = []
    
    for line_num, line in enumerate(lines, 1):  # line_num starts at 1
        temp_str = ""
        column_num = 1  # Start column at 1 for each line
        
        for char in line:
            if char == " ":
                if temp_str:  # Only add token if temp_str is not empty
                    tokens.append((temp_str, "Identifier", line_num, column_num - len(temp_str)))
                    temp_str = ""  # Reset for the next token
                # Skip the space, no token to append
            else:
                temp_str += char  # Build the current token
            column_num += 1  # Move to the next character (column)
        
        # After processing the line, check if there is any leftover token
        if temp_str:
            tokens.append((temp_str, "Identifier", line_num, column_num - len(temp_str)))
    
    return tokens

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

        lexicalText = analyzeLexical(textAreaInput)

        for lexeme, token, line, column in lexicalText:
            st.write(f"Line {line}, Column {column}. Lexeme **{lexeme}** has a token of **{token}**.")

with st.container(border=True):
    # st.write("Code has no error!")


    