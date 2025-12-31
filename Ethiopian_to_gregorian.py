def is_leap(year):
    return (year + 5500) % 4 == 0

months =  [('January', 31),
           ('February', 28),
           ('March', 31),
           ('April', 30),
           ('May', 31),
           ('June', 30),
           ('July', 31),
           ('August', 31),
           ('September', 30),
           ('October', 31),
           ('November', 30),
           ('December', 31)]

def Ethiopian_to_gregorian(date, month, year):
    global gregorian_date, gregorian_month, gregorian_year
    
    if month == 13:
        month_index = month - 5
        gregorian_date = date + 10
        pagume_days = 6 if is_leap(year) else 5
        if gregorian_date > pagume_days:
            month_index += 1
            gregorian_date %= pagume_days
        gregorian_month = months[month_index - 1][0]
        gregorian_year = year + 8
    else:
        if month - 5 >= 0:
            month_index = month - 5
        else:
            month_index = (month + 7) % 12

        gregorian_month = month + 8
        if month <= 5:
            gregorian_year = year + 7
        else:
            gregorian_year = year + 8
        
        if gregorian_month > 12:
            gregorian_month %= 12
        
        gregorian_date = date + (11 if is_leap(year) and months[month_index][1] <= 30 else 10)
        
        if gregorian_date > months[month_index][1]:
            gregorian_date -= months[month_index][1]
            gregorian_month = (gregorian_month % 12) + 1
            if gregorian_month == 1:
                gregorian_year += 1
        gregorian_month
    return [gregorian_date, gregorian_month, gregorian_year]

