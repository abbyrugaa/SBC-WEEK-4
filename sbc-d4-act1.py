user_sentence = input("Enter a sentence: ")
keyword = input("Enter keyword: ")

start_index = -1
end_index = -1

sentence_length = len(user_sentence)
keyword_length = len(keyword)

for i in range(sentence_length - keyword_length + 1):
    if user_sentence[i:i + keyword_length] == keyword:
        start_index = i
        end_index = i + keyword_length - 1
        break

if start_index != -1:
    print(f"The word '{keyword}' is in '{user_sentence}' from index {start_index} to {end_index}.")
else:
    print(f"The word '{keyword}' was not found in the sentence.")