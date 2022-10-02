def dayOfProgrammer(year):
    date_value = ""
    days_in_february = 28
    if year == 1918:
        days_in_february = 15
    elif year < 1918:
        if year % 4 == 0:
            days_in_february = 29
    else:
        if year % 400 == 0:
            days_in_february = 29

        elif (year % 4 == 0) and not (year % 100 == 0):
            days_in_february = 29

    i = 1
    days_remaining = 256
    while i <= 12:
        if i in [4, 6, 9, 11]:
            days_in_month = 30
        elif i == 2:
            days_in_month = days_in_february
        else:
            days_in_month = 31

        if days_remaining > days_in_month:
            days_remaining -= days_in_month

        else:
            date_value = str(days_remaining) + "."
            if i <= 9 :
                date_value += "0"
            date_value += str(i) + "."
            date_value += str(year)
            break
        i += 1

    return date_value


if __name__ == '__main__':
    result = dayOfProgrammer(1918)
    print(result)


