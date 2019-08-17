n = int(input())
my_dict = dict()
for i in range(n):
    for word in list(input().split()):
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
my_list = []
for word in my_dict:
    my_list.append((-1 * my_dict[word], word))
my_list.sort()
for pair in my_list:
    print(pair[1])
    
