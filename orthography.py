#orthography.py
#an ascii-to-áthid orthography tool that runs in the terminal

while True:
    text = input("text to romanize: ")
    if text == "quit":
        break
    else:
        for char in text:
            text = text.replace("z", "ʒ")
            text = text.replace("q", "ś")
            text = text.replace("th", "ý")
            text = text.replace("x" "ĺ")
            text = text.replace("v", "ẃ")
        print(text)
