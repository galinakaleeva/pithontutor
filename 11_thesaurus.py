n = int(input())
thesaurus = dict()
for i in range(n):
    words = list(input().split())
    thesaurus[words[0]] = words[1]
    thesaurus[words[1]] = words[0]
print(thesaurus[input()])
