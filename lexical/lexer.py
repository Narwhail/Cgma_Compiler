import streamlit as st # type: ignore

def analyzeLexical(textInput):
    lines = textInput.splitlines()  # Split input into lines
    tokens = []
    token_type = ""
    
    for line_num, line in enumerate(lines, 1):  # line_num starts at 1
        temp_str = ""
        column_num = 1  # Start column at 1 for each line
        
        for char in line:
            if char == " ":
                if temp_str:
                    token_type = checkToken(temp_str)
                    tokens.append((temp_str, token_type, line_num, column_num - len(temp_str)))
                    temp_str = ""
            else:
                temp_str += char
            column_num += 1

        # After processing the line, check for any leftover token
        if temp_str:
            token_type = checkToken(temp_str)
            tokens.append((temp_str, token_type, line_num, column_num - len(temp_str)))

    return tokens


def checkToken(currentWord):
    # LETTER A
    if currentWord[0] == 'a':
        if currentWord[1] == 'p':
            if currentWord[2] == 'p':
                if currentWord[3] == 'e':
                    if currentWord[4] == 'n':
                        if currentWord[5] == 'd' and len(currentWord) == 6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'u':
            if currentWord[2] == 'r':
                if currentWord[3] == 'a' and len(currentWord) == 4:
                    return "RESERVED_WORD"

    # LETTER C
    if currentWord[0] == 'c':
        if currentWord[1] == 'a':
            if currentWord[2] == 's':
                if currentWord[3] == 'e':
                    if currentWord[4] == 'o':
                        if currentWord[5] == 'h' and len(currentWord) == 6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'h':
            if currentWord[2] == 'a':
                if currentWord[3] == 't' and len(currentWord) == 4:
                    return "RESERVED_WORD"
            elif currentWord[2] == 'u':
                if currentWord[3] == 'd':
                    if currentWord[4] == 'e':
                        if currentWord[5] == 'l':
                            if currentWord[6] == 'u':
                                if currentWord[7] == 'x':
                                    if currentWord[8] == 'e' and len(currentWord) == 9:
                                        return "RESERVED_WORD"
                elif currentWord[3] == 'n':
                    if currentWord[4] == 'g':
                        if currentWord[5] == 'u':
                            if currentWord[6] == 's' and len(currentWord) == 7:
                                return "RESERVED_WORD"
                            
    # Letter F
    if currentWord[0] == 'f':
        if currentWord[1] == 'a':
            if currentWord[2] == 'l':
                if currentWord[3] == 's':
                    if currentWord[4] == 'e' and len(currentWord) == 5:
                        return "RESERVED_WORD"
        elif currentWord[1] == 'o':
            if currentWord[2] == 'r':
                if currentWord[3] == 's':
                    if currentWord[4] == 'e':
                        if currentWord[5] == 'n' and len(currentWord) == 6:
                            return "RESERVED_WORD"
    
    else:
        return "Unknown token"