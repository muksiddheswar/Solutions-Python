import re
if __name__ == '__main__':
    n, s = input(), input()
    elements = set(s.split())
    subsets = 0
    for element in elements:
        subsets += 2 ** len(re.findall(re.compile(element), s)) - 1
    print(subsets % (10 ** 9 + 7))

