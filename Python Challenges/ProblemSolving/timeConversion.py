def timeConversion(s):
    elements = s.split(':')
    am_pm = elements[-1][-2:]
    print(am_pm)
    minute = elements[1]
    second = elements[2][:-2]
    if am_pm == 'AM':

        if elements[0] == '12':
            hour = '00'
        else:
            hour = elements[0]
    else:
        if elements[0] == '12':
            hour = elements[0]
        else:
            hour = '%s'%(int(elements[0]) + 12)
    return (hour + ':' + minute + ':' + second)

if __name__ == '__main__':
    s = input()
    res = timeConversion(s)
    print(res)