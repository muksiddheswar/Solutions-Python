
def bonAppetit(bill, k, b):
    actual_bill = 0
    for i in range(n):
        if i != k:
            actual_bill += bill[i] / 2
    if b > actual_bill:
        print(int(b - actual_bill))
    else:
        print("Bon Appetit")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
