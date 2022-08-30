def add_time(start, duration, starting_day=None):
    #Vars
    start_numbers, day_half = start.split()
    colon1, colon2 = start_numbers.find(':'), duration.find(':')
        
    hours1, minutes1 = int(start_numbers[: colon1]), int(start_numbers[colon1 + 1:])
    hours2, minutes2 = int(duration[: colon2]), int(duration[colon2 + 1:])
    days_passed = 0
    lst_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    #Sum
    hours1 += hours2
    minutes1 += minutes2
    
    while minutes1 > 60:
        minutes1 -= 60
        hours1 += 1
    while hours1 > 12:
        hours1 -= 12
        if day_half == 'AM':
            day_half = 'PM'
        elif day_half == 'PM':
            day_half = 'AM'
            days_passed += 1
    if hours1 == 12 and minutes1 > 0:
        if day_half == 'AM':
            day_half = 'PM'
        elif day_half == 'PM':
            day_half = 'AM'
            days_passed += 1
    
    #Formating
    if len(str(minutes1)) == 1:
        minutes1 = f'0{minutes1}'
    if not starting_day:
        if days_passed == 0:
            return f'{hours1}:{minutes1} {day_half}'
        elif days_passed == 1:
            return f'{hours1}:{minutes1} {day_half} (next day)'
        else:
            return f'{hours1}:{minutes1} {day_half} ({days_passed} days later)'
    
    if starting_day:
        starting_day = starting_day.lower()
        first_letter = starting_day[0].upper()
        starting_day = first_letter + starting_day[1:]
        
        idx_day = lst_days.index(starting_day)
        day = 0
        while day < days_passed:
            idx_day += 1
            if idx_day == len(lst_days):
                idx_day = 0
            day += 1
        
        if days_passed == 0:
            return f'{hours1}:{minutes1} {day_half}, {lst_days[idx_day]}'
        elif days_passed == 1:
            return f'{hours1}:{minutes1} {day_half}, {lst_days[idx_day]} (next day)'
        else:
            return f'{hours1}:{minutes1} {day_half}, {lst_days[idx_day]} ({days_passed} days later)'
