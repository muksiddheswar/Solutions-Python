if __name__ == '__main__':
    S = input()
    lower_case = []
    upper_case = []
    odd_digits = []
    even_digits = []

    for i in S:
        if i.islower() is True:
            lower_case.append(i)
        elif i.isupper() is True:
            upper_case.append(i)
        else:
            if int(i) % 2 == 0:
                even_digits.append(i)
            else:
                odd_digits.append(i)

    lower_case.sort()
    upper_case.sort()
    odd_digits.sort()
    even_digits.sort()
    lower_case = ''.join(lower_case)
    upper_case = ''.join(upper_case)
    odd_digits = ''.join(odd_digits)
    even_digits = ''.join(even_digits)
    print(lower_case + upper_case + odd_digits + even_digits)





