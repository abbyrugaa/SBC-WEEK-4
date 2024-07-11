letters = ["M", "B", "D", "R", "N", "C"]

n = len(letters)
for i in range(n - 1):
    for j in range(n - i - 1):
        if letters[j] > letters[j + 1]:
            letters[j], letters[j + 1] = letters[j + 1], letters[j]
            print(letters)

print("Sorted array:", letters)
