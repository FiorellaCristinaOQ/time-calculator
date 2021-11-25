def add_time(start_time,duration,start_day = None):
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
    end_minute = start_minute + duration_minute
    plus_hour = 0
    if end_minute >= 60:
        plus_hour = int(end_minute/60)
        end_minute = end_minute - plus_hour*60
    end_hour = start_hour + duration_hour + plus_hour
    plus_stage = 0
    if end_hour > 12:
        plus_stage = int(end_hour/12)
        end_hour = end_hour - plus_stage*12
    # Establecer estado de salida
    end_stage = ''
    if plus_stage%2 == 0:
        end_stage = start_stage
    else:
        if start_stage == 'PM':
            end_stage = 'AM'
        else:
            end_stage = 'PM'
    # Calcular tiempo después
    days_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    stage_minute = 60 - start_minute
    if start_stage == 'AM':
        stage_hour = 24 - start_hour
    else:
        stage_hour = 12 - start_hour
    number_days_after = (start_hour + duration_hour + plus_hour)
    end_time = str(end_hour) + ':' + str(end_minute) + ' ' + end_stage
    return end_time
print(add_time("6:30 PM", "205:12"))