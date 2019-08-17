n = int(input())
gen_tree = dict()
for i in range(n - 1):
    line = input().split()
    son, parent = line[0], line[1]
    gen_tree[son] = parent
height = dict()
for person in set(gen_tree.keys()).union(set(gen_tree.values())):
    height[person] = 0
    son = person
    while son in gen_tree.keys():
        son = gen_tree[son]
        height[person] += 1
k = int(input())
answer = []
for i in range(k):
    line = input().split()
    person1, person2 = line[0], line[1]
    if height[person1] == height[person2]:
        answer.append(0)
    elif height[person1] < height[person2]:
        while height[person2] > height[person1]:
            person2 = gen_tree[person2]
        if person1 == person2:
            answer.append(1)
        else:
            answer.append(0)
    else:
        while height[person1] > height[person2]:
            person1 = gen_tree[person1]
        if person1 == person2:
            answer.append(2)
        else:
            answer.append(0)
print(*answer)
