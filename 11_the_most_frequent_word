n = int(input())
my_dict = dict()
for i in range(n):
    line = input().split()
    for word in line:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
most_frequent = []
for key, val in my_dict.items():
    if val == max(my_dict.values()):
        most_frequent.append(key)
print(sorted(most_frequent)[0])
