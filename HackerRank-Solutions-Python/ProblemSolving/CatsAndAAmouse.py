# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a = abs(z-x)
    cat_b = abs(z - y)
    if cat_a == cat_b:
        return 'Mouse C'
    elif cat_b > cat_a:
        return 'Cat A'
    else:
        return 'Cat B'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)


