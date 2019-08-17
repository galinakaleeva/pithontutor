n = int(input())
dictionary = dict()
for i in range(n):
    line = input().replace('-', ' ').replace(',', ' ').split()
    eng_word = line[0]
    for latin_word in line[1:]:
        if latin_word not in dictionary:
            dictionary[latin_word] = [eng_word]
        else:
            dictionary[latin_word].append(eng_word)
print(len(dictionary.keys()))
for latin_word in sorted(dictionary.keys()):
    translations = sorted(dictionary[latin_word])
    print(latin_word + ' - ' + ', '.join(translations))
    
