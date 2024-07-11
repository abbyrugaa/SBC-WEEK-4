def sent_tokenize(text):
    tokens = []
    sentence = ""
    for char in text:
        sentence += char
        if char in ".!?":
            tokens.append(sentence.strip())
            sentence = ""
    if sentence.strip():
        tokens.append(sentence.strip())
    return tokens

input_text = input("Enter a text: ")
token_list = sent_tokenize(input_text)

print(f"Tokenized list: {token_list}")