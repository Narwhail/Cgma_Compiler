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