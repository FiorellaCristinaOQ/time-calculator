def add_time(start_time,duration,start_day = ''):
    # Establecer valores de ingreso
    time_lst = start_time.split()
    hour_lst = time_lst[0].split(':')
    start_hour = int(hour_lst[0])
    start_minute = int(hour_lst[1])
    start_stage = time_lst[1]
    duration_lst = duration.split(':')
    duration_hour = int(duration_lst[0])
    duration_minute = int(duration_lst[1])
    # Establecer valores de salida
    end_minute = start_minute + duration_minute # Variable final minutos
    plus_hour = 0
    if end_minute >= 60:
        plus_hour = int(end_minute/60)
        end_minute = end_minute - plus_hour*60
    end_hour = start_hour + duration_hour + plus_hour # Variable final hora
    plus_stage = 0
    if end_hour >= 12:
        plus_stage = int(end_hour/12)
        end_hour = end_hour - plus_stage*12
    # Establecer estado de salida
    end_stage = '' # Variable final AM o PM
    if plus_stage%2 == 0:
        end_stage = start_stage
    else:
        if start_stage == 'PM':
            end_stage = 'AM'
        else:
            end_stage = 'PM'
    # Calcular tiempo faltante para completar un día
    days_later = ''
    days_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if start_day != '':
        start_day = start_day.lower()
        start_day = start_day[0].upper() + start_day[1:]
    total_hour = duration_hour + plus_hour 
    if start_stage == 'AM':
        needed_hour = 24 - start_hour
    else:
        needed_hour = 12 - start_hour 
    # Calcular tiempo después
    counter = 0
    if needed_hour <= total_hour:
        counter += 1
    counter += int((total_hour - needed_hour)/24)
    if counter == 0 and start_day != '':
        days_later = ', ' + start_day
    elif counter == 1 and start_day == '':
        days_later = ' (next day)'
    elif counter == 1 and start_day != '':
        i = days_week.index(start_day)
        days_later = ', ' + days_week[i+1] + ' (next day)'
    elif counter > 1 and start_day == '':
        days_later = ' (' + str(counter) + ' days later)'
    elif counter > 1 and start_day != '':
        i = days_week.index(start_day)
        ind = i + counter
        if ind > 6:
            ind = ind - 7*int(counter/6)
        days_later = ', ' + days_week[ind] + ' (' + str(counter) + ' days later)'
    # String de salida
    if end_minute < 10:
        end_minute = '0' + str(end_minute)
    else:
        end_minute = str(end_minute)
    if end_hour < 10 and end_hour != 0:
        end_hour = str(end_hour)
    elif end_hour == 0:
        end_hour = '12'
    else:
        end_hour = str(end_hour)
    end_time = end_hour + ':' + end_minute + ' ' + end_stage + days_later
    return end_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))