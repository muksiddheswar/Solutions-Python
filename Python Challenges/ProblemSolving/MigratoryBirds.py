def migratoryBirds(arr):
    bird_dict = {}
    highest_count = 0
    highest_id = arr[0]
    for i in arr:
        if i not in bird_dict:
            bird_dict[i] = 1
        else:
            bird_dict[i] += 1

        if bird_dict[i] > highest_count:
            highest_count = bird_dict[i]
            highest_id = i

        elif bird_dict[i] == highest_count and i < highest_id:
            highest_id = i

    return highest_id

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
