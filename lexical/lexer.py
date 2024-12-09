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
    
    # Letter G
    if currentWord[0] == 'g':
        if currentWord[1] == 'e':
            if currentWord[2] == 't':
                if currentWord[3] == 'o':
                    if currentWord[4] == 'u':
                        if currentWord[5] == 't' and len(currentWord)==6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'n':
            if currentWord[2] == 'g' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter H
    if currentWord[0] == 'h':
        if currentWord[1] == 'a':
            if currentWord[2] == 'w':
                if currentWord[3] == 'k' and len(currentWord)==4:
                    return "RESERVED_WORD"                                  # HAWK TUAH (?)

    # Letter I
    if currentWord[0] == 'i':
        if currentWord[1] == 'n':
            if currentWord[2] == 's':
                if currentWord[3] == 'e':
                    if currentWord[4] == 'r':
                        if currentWord[5] == 't' and len(currentWord)==6:
                            return "RESERVED_WORD"
    
    # Letter J
    if currentWord[0] == 'j':
        if currentWord[1] == 'i':
            if currentWord[2] == 't' and len(currentWord) == 3:
                return "RESERVED_WORD"

    # Letter L
    if currentWord[0] == 'l':
        if currentWord[1] == 'e':
            if currentWord[2] == 't':
                if currentWord[3] == 'h':
                    if currentWord[4] == 'i':
                        if currentWord[5] == 'm':
                            if currentWord[6] == 'c':
                                if currentWord[7] == 'o':
                                    if currentWord[8] == 'o':
                                        if currentWord[9] == 'k' and len(currentWord) == 10:
                                            return "RESERVED_WORD"              
        elif currentWord[1] == 'w':
            if currentWord[2] == 'k' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter N
    if currentWord[0] == 'n':
        if currentWord[1] == 'o':
            if currentWord[2] == 'c':
                if currentWord[3] == 'a':
                    if currentWord[4] == 'p' and len(currentWord)==5:
                        return "RESERVED_WORD"
        if currentWord[1] == 'p':
            if currentWord[2] == 'c' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter P
    if currentWord[0] == 'p':
        if currentWord[1] == 'a':
            if currentWord[2] == 'u':
                if currentWord[3] == 's':
                    if currentWord[4] == 'e' and len(currentWord)==5:
                        return "RESERVED_WORD"
        elif currentWord[1] == 'l':
            if currentWord[2] == 'u':
                if currentWord[3] == 'g' and len(currentWord)==4:
                    return "RESERVED_WORD"
                
    # Letter R
    if currentWord[0] == 'r':
        if currentWord[1] == 'e':
            if currentWord[2] == 'm':
                if currentWord[3] == 'o':
                    if currentWord[4] == 'v':
                        if currentWord[5] == 'e' and len(currentWord)==6:
                            return "RESERVED_WORD"

    # Letter S
    if currentWord[0] == 's':
        if currentWord[1] == 'k':
            if currentWord[2] == 'i':
                if currentWord[3] == 'b':
                    if currentWord[4] == 'i':
                        if currentWord[5] == 'd':
                            if currentWord[6] == 'i' and len(currentWord)==7:
                                return "RESERVED_WORD"
        elif currentWord[1] == 't':
            if currentWord[2] == 'u':
                if currentWord[3] == 'r':
                    if currentWord[4] == 'd':
                        if currentWord[5] == 'y' and len(currentWord)==6:
                            return "RESERVED_WORD"


    # Letter T
    if currentWord[0] == 't':
        if currentWord[1] == 'u':
            if currentWord[2] == 'a':
                if currentWord[3] == 'h' and len(currentWord)==4:
                    return "RESERVED_WORD"
        elif currentWord[1] == 'r':
            if currentWord[2] == 'u':
                if currentWord[3] == 'e' and len(currentWord)==4:
                    return "RESERVED_WORD"

    # Letter Y
    if currentWord[0] == 'y':
        if currentWord[1] == 'a':
            if currentWord[2] == 'p' and len(currentWord)==3:
                return "RESERVED_WORD"




    else:
        return "Unknown token"