message = input("> ")
words = message.split(" ")
emojis = {
    "I" : "saurabh",
    "am" : "is",
    ":)" : "😃",
    ":(" : "😫",
    ":|" : "🤕"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
