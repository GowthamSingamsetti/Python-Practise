prompt = input(">")
words = prompt.split(' ')
emojis = {
    ":)": "😊",
    ":(": "🙁",
    ":|": "😔",
    ":p": "😁"
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)
