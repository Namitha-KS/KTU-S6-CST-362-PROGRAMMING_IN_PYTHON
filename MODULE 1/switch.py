def days(day):
    switcher ={
        0:'SUNDAY',
        1:'MONDAY',
        2:'TUESDAY',
        3:'WEDNESDAY',
        4:'THURSDAY',
        5:'FRIDAY',
        6:'SATURDAY'
    }
    return switcher[day]

day = int(input())
print(days(day))