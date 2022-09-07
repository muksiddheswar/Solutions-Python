def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    amount = -1
    for keyboard in keyboards:
        if keyboard < b:
            for drive in drives:
                if b >= drive + keyboard > amount:
                    amount = drive + keyboard
    return amount


if __name__ == '__main__':
    b = 10
    keyboards = [3, 1]
    # drives = [5, 2, 6]
    drives = [5, 2, 8]
    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
