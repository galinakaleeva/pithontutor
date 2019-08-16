n = int(input())
candidates = dict()
for i in range(n):
    cand_str = list(input().split())
    if cand_str[0] in candidates:
        candidates[cand_str[0]] += int(cand_str[1])
    else:
        candidates[cand_str[0]] = int(cand_str[1])
for cand in list(sorted(candidates)):
    print(cand, candidates[cand])
    
