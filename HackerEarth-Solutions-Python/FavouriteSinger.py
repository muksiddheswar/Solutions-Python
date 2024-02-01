songs = int(input())
singer_list = input().split(' ')

database = {}
for singer in singer_list:
    # singer = input()
    if singer in database.keys():
        database[singer] += 1
    else:
        database[singer] = 1

count = 0

values = list(database.values())
max_value = max(values)
for i in values:
    if i == max_value:
        count += 1
print(count)
