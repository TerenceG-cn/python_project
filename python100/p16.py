import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))

    myDate = datetime.date(1941, 1, 5)
    print(myDate.strftime('%d/%m/%Y'))

    myDate_nextDay = myDate + datetime.timedelta(days=1)
    print(myDate_nextDay.strftime('%d:%m:%Y'))

    myDate_changeYear = myDate.replace(year=myDate.year + 1)
    print(myDate_changeYear.strftime('%d-%m-%Y'))
