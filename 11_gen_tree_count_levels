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
for son in sorted(height.keys()):
    print(son, height[son])
    
