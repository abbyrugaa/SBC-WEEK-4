def subword_tokenize(word):
    # Define the prefixes and suffixes to be checked
    prefixes = ["un", "in", "dis", "re", "pre", "mis"]
    suffixes = ["able", "ing", "ed", "tion", "ly"]
    
    # Check for prefixes
    for prefix in prefixes:
        if word.startswith(prefix):
            return [prefix, "##" + word[len(prefix):]]
    
    # Check for suffixes
    for suffix in suffixes:
        if word.endswith(suffix):
            return [word[:-len(suffix)], "##" + suffix]
            
    return [word]

# Input word
word = input("Enter a word: ")

# Tokenize the word
tokens = subword_tokenize(word)

# Print the tokens
print(tokens)
