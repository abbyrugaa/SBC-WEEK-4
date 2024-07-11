def tokenize(text):
    tokens = []
    word = ""
    for char in text:
        if char.isalnum():
            word += char
        else:
            if word:
                tokens.append(word)
            tokens.append(char)
            word = ""
    if word:
        tokens.append(word)
    return tokens

input_text = input("Enter a text: ")
token_list = tokenize(input_text)

print(f"Tokenized list: {token_list}")