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
    if currentWord[0] == 'a' and len(currentWord)>=2:
        if currentWord[1] == 'p' and len(currentWord)>=3:
            if currentWord[2] == 'p' and len(currentWord)>=4:
                if currentWord[3] == 'e' and len(currentWord)>=5:
                    if currentWord[4] == 'n' and len(currentWord)>=6:
                        if currentWord[5] == 'd' and len(currentWord) == 6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'u' and len(currentWord)>=3:
            if currentWord[2] == 'r' and len(currentWord)>=4:
                if currentWord[3] == 'a' and len(currentWord) == 4:
                    return "RESERVED_WORD"

    # LETTER C
    if currentWord[0] == 'c' and len(currentWord)>=2:
        if currentWord[1] == 'a' and len(currentWord)>=3:
            if currentWord[2] == 's' and len(currentWord)>=4:
                if currentWord[3] == 'e' and len(currentWord)>=5:
                    if currentWord[4] == 'o' and len(currentWord)>=6:
                        if currentWord[5] == 'h' and len(currentWord) == 6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'h' and len(currentWord)>=3:
            if currentWord[2] == 'a' and len(currentWord)>=4:
                if currentWord[3] == 't' and len(currentWord) == 4:
                    return "RESERVED_WORD"
            elif currentWord[2] == 'u' and len(currentWord)>=4:
                if currentWord[3] == 'd' and len(currentWord)>=5:
                    if currentWord[4] == 'e' and len(currentWord)>=6:
                        if currentWord[5] == 'l' and len(currentWord)>=7:
                            if currentWord[6] == 'u' and len(currentWord)>=8:
                                if currentWord[7] == 'x' and len(currentWord)>=9:
                                    if currentWord[8] == 'e' and len(currentWord) == 9:
                                        return "RESERVED_WORD"
                elif currentWord[3] == 'n' and len(currentWord)>=5:
                    if currentWord[4] == 'g' and len(currentWord)>=6:
                        if currentWord[5] == 'u' and len(currentWord)>=7:
                            if currentWord[6] == 's' and len(currentWord) == 7:
                                return "RESERVED_WORD"
                            
    # Letter F
    if currentWord[0] == 'f' and len(currentWord)>=2:
        if currentWord[1] == 'a' and len(currentWord)>=3:
            if currentWord[2] == 'l' and len(currentWord)>=4:
                if currentWord[3] == 's' and len(currentWord)>=5:
                    if currentWord[4] == 'e' and len(currentWord) == 5:
                        return "RESERVED_WORD"
        elif currentWord[1] == 'o' and len(currentWord)>=3:
            if currentWord[2] == 'r' and len(currentWord)>=4:
                if currentWord[3] == 's' and len(currentWord)>=5:
                    if currentWord[4] == 'e' and len(currentWord)>=6:
                        if currentWord[5] == 'n' and len(currentWord) == 6:
                            return "RESERVED_WORD"
    
    # Letter G
    if currentWord[0] == 'g' and len(currentWord)>= 2:
        if currentWord[1] == 'e' and len(currentWord)>=3:
            if currentWord[2] == 't' and len(currentWord)>=4:
                if currentWord[3] == 'o' and len(currentWord)>=5:
                    if currentWord[4] == 'u' and len(currentWord)>=6:
                        if currentWord[5] == 't' and len(currentWord)==6:
                            return "RESERVED_WORD"
        elif currentWord[1] == 'n' and len(currentWord)>=3:
            if currentWord[2] == 'g' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter H
    if currentWord[0] == 'h' and len(currentWord)>=2:
        if currentWord[1] == 'a' and len(currentWord)>=3:
            if currentWord[2] == 'w' and len(currentWord)>=4:
                if currentWord[3] == 'k' and len(currentWord)==4:
                    return "RESERVED_WORD"                                  # HAWK TUAH (?)

    # Letter I
    if currentWord[0] == 'i' and len(currentWord)>=2:
        if currentWord[1] == 'n' and len(currentWord)>=3:
            if currentWord[2] == 's' and len(currentWord)>=4:
                if currentWord[3] == 'e' and len(currentWord)>=5:
                    if currentWord[4] == 'r' and len(currentWord)>=6:
                        if currentWord[5] == 't' and len(currentWord)==6:
                            return "RESERVED_WORD"
    
    # Letter J
    if currentWord[0] == 'j' and len(currentWord)>=2:
        if currentWord[1] == 'i' and len(currentWord)>=3:
            if currentWord[2] == 't' and len(currentWord) == 3:
                return "RESERVED_WORD"

    # Letter L
    if currentWord[0] == 'l' and len(currentWord)>=2:
        if currentWord[1] == 'e' and len(currentWord)>=3:
            if currentWord[2] == 't' and len(currentWord)>=4:
                if currentWord[3] == 'h' and len(currentWord)>=5:
                    if currentWord[4] == 'i' and len(currentWord)>=6:
                        if currentWord[5] == 'm' and len(currentWord)>=7:
                            if currentWord[6] == 'c' and len(currentWord)>=8:
                                if currentWord[7] == 'o' and len(currentWord)>=9:
                                    if currentWord[8] == 'o' and len(currentWord)>=10:
                                        if currentWord[9] == 'k' and len(currentWord) == 10:
                                            return "RESERVED_WORD"              
        elif currentWord[1] == 'w' and len(currentWord)>=3:
            if currentWord[2] == 'k' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter N
    if currentWord[0] == 'n' and len(currentWord)>=2:
        if currentWord[1] == 'o' and len(currentWord)>=3:
            if currentWord[2] == 'c' and len(currentWord)>=4:
                if currentWord[3] == 'a' and len(currentWord)>=5:
                    if currentWord[4] == 'p' and len(currentWord)==5:
                        return "RESERVED_WORD"
        if currentWord[1] == 'p' and len(currentWord)>=3:
            if currentWord[2] == 'c' and len(currentWord)==3:
                return "RESERVED_WORD"

    # Letter P
    if currentWord[0] == 'p' and len(currentWord)>=2:
        if currentWord[1] == 'a' and len(currentWord)>=3:
            if currentWord[2] == 'u' and len(currentWord)>=4:
                if currentWord[3] == 's' and len(currentWord)>=5:
                    if currentWord[4] == 'e' and len(currentWord)==5:
                        return "RESERVED_WORD"
        elif currentWord[1] == 'l' and len(currentWord)>=3:
            if currentWord[2] == 'u' and len(currentWord)>=4:
                if currentWord[3] == 'g' and len(currentWord)==4:
                    return "RESERVED_WORD"
                
    # Letter R
    if currentWord[0] == 'r' and len(currentWord)>=2:
        if currentWord[1] == 'e' and len(currentWord)>=3:
            if currentWord[2] == 'm' and len(currentWord)>=4:
                if currentWord[3] == 'o' and len(currentWord)>=5:
                    if currentWord[4] == 'v' and len(currentWord)>=6:
                        if currentWord[5] == 'e' and len(currentWord)==6:
                            return "RESERVED_WORD"

    # Letter S
    if currentWord[0] == 's' and len(currentWord)>=2:
        if currentWord[1] == 'k' and len(currentWord)>=3:
            if currentWord[2] == 'i' and len(currentWord)>=4:
                if currentWord[3] == 'b' and len(currentWord)>=5:
                    if currentWord[4] == 'i' and len(currentWord)>=6:
                        if currentWord[5] == 'd' and len(currentWord)>=7:
                            if currentWord[6] == 'i' and len(currentWord)==7:
                                return "RESERVED_WORD"
        elif currentWord[1] == 't' and len(currentWord)>=3:
            if currentWord[2] == 'u' and len(currentWord)>=4:
                if currentWord[3] == 'r' and len(currentWord)>=5:
                    if currentWord[4] == 'd' and len(currentWord)>=6:
                        if currentWord[5] == 'y' and len(currentWord)==6:
                            return "RESERVED_WORD"

    # Letter T
    if currentWord[0] == 't' and len(currentWord)>=2:
        if currentWord[1] == 'u' and len(currentWord)>=3:
            if currentWord[2] == 'a' and len(currentWord)>=4:
                if currentWord[3] == 'h' and len(currentWord)==4:
                    return "RESERVED_WORD"
        elif currentWord[1] == 'r' and len(currentWord)>=3:
            if currentWord[2] == 'u' and len(currentWord)>=4:
                if currentWord[3] == 'e' and len(currentWord)==4:
                    return "RESERVED_WORD"

    # Letter Y
    if currentWord[0] == 'y' and len(currentWord)>=2:
        if currentWord[1] == 'a' and len(currentWord)>=3:
            if currentWord[2] == 'p' and len(currentWord)==3:
                return "RESERVED_WORD"

    else:
        return "Unknown token"