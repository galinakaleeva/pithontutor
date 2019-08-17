n = int(input())
my_dict = dict()
for i in range(n):
    line = input().split()
    file_name = line[0]
    for operation in line[1:]:
        if file_name in my_dict:
            my_dict[file_name].append(operation)
        else:
            my_dict[file_name] = [operation]
m = int(input())
for i in range(m):
    line = input().split()
    if line[0] == 'read':
        operation = 'R'
    if line[0] == 'write':
        operation = 'W'
    if line[0] == 'execute':
        operation = 'X'
    file_name = line[1]
    if operation in my_dict[file_name]:
        print('OK')
    else:
        print('Access denied')
