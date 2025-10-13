from datetime import datetime, timedelta


data_file_path = '/Users/nadzeya/PythonAutomation/nadzeya/homework/eugene_okulik/hw_13/data.txt'

with open(data_file_path) as data_file:
    for line in data_file:
        line = line.strip()

        number_and_date, action_text = line.split(' - ', 1)
        number_str, date_str = number_and_date.split('.', 1)
        number = int(number_str.strip())
        date = datetime.strptime(date_str.strip(), '%Y-%m-%d %H:%M:%S.%f')

        if number == 1:
            new_date = date + timedelta(weeks=1)
            print(new_date)
        elif number == 2:
            weekday = date.strftime('%A')
            print(weekday)
        elif number == 3:
            now = datetime.now()
            delta_days = (now - date).days
            print(f'{delta_days} days ago')
