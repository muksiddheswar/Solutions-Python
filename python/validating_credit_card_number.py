import re

def validity_test(number):
    match = re.match(r'[456][0-9]{15}$', number)
    h_match = re.match(r'[456][0-9]{3}[-][0-9]{4}[-][0-9]{4}[-][0-9]{4}$', number)
    if not match and not h_match:
        return 'Invalid'
    match = re.findall(r'(([0-9])\2{3,})', re.sub('-', '', number))
    if match:
        return 'Invalid'
    return 'Valid'


if __name__ == '__main__':
    n = input()
    for i in range(int(n)):
        number = input()
        res = validity_test(number)
        print(res)