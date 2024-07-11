def char_tokenize(text):
    return list(text)

input_text = input("Enter a text: ")
token_list = char_tokenize(input_text)

print(f"Tokenized list: {token_list}")