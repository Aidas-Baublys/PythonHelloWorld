msg = input("> ")
words = msg.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😢",
    ":o": "😮"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)
