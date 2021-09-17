def emoji_printer(prompt):
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
    return output


prompt = input(">")
print(emoji_printer(prompt))
