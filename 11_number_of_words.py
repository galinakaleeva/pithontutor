text = {}
for word in list(input().split()):
    if word not in text:
        print(0, end=' ')
        text[word] = 1
    else:
        print(text[word], end=' ')
        text[word] += 1
        
