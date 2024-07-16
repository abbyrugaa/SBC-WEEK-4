input_string = "apple,banana,orange,grape"
output_list = custom_tokenize(input_string)
print(output_list)

def custom_tokenize(input_string):
    tokens = []
    current_token = ""
    
    for char in input_string:
        if char == ",":
            if current_token:
                tokens.append(current_token)
                current_token = ""
        else:
            current_token += char
    
    if current_token:
        tokens.append(current_token)
    
    return tokens