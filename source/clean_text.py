with open('text.txt') as f:
    text = f.read()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~”“’'''
    no_punct = ""

    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char

    no_punct.lower()

    words_array = no_punct.split()
