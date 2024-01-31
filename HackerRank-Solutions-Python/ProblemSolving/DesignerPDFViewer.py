
def designerPdfViewer(h, word):
    breadth = 0
    max_height = 0
    for i in word:
        breadth += 1
        index = ord((i.lower())) - 97
        max_height = max(max_height, h[index])

    return max_height * breadth


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
