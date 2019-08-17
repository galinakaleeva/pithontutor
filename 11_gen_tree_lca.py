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
for i in range(k):
    line = input().split()
    person1, person2 = line[0], line[1]
    while person1 != person2:
        if height[person1] < height[person2]:
            person2 = gen_tree[person2]
        else:
            person1 = gen_tree[person1]
    print(person1)
    
