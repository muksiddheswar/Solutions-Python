def timeConversion(s):
    am_pm = s[-2:]
    if am_pm == "PM" and s[:2]!= '12':
        hour = int(s[:2])
        s = str(hour + 12) + s[2:-2]
    elif am_pm == "AM" and s[:2] == '12':
        s = "00" + s[2:-2]
    else:
        s = s[:-2]
    return s


if __name__ == '__main__':
    s = "12:45:54PM"
    result = timeConversion(s)
    print(result)