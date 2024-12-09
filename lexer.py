def analyzeLexical(textInput):
    lines = textInput.splitlines()

    for line in lines:
        currentChar = list(line)        #splits the current line into separate characters
        tokens = []
        temp_str = ""
        
        for char in currentChar:
            if char == " ":
                tokens.append(temp_str)
            else:
                temp_str += char
    
    tokens.append(temp_str)