def clean(instring):
    after_space = True
    new_string = ""
    a = len(instring)
    for i in range(0,len(instring)):
        next_char = instring[i]
        if after_space == True:
            if next_char != ' ':
                new_string += next_char
                after_space = False
        else:
            new_string += next_char
            if next_char == ' ':
                after_space = True
                    
    return new_string

print(clean('   A B  C'))
