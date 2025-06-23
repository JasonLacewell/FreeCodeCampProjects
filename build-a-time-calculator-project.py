** start of main.py **

def add_time(start, duration, starting_day = ''):
    
    #Get hours, minutes and meridian from start (24 hour clock)

    start_hours = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1].split(' ')[0])
    meridian = start.split(':')[1].split(' ')[1].upper()
    if meridian == 'PM':
        start_hours += 12
    
    #Get duration hours and minutes (24 hour clock)
    
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])


    #add up resulting new time

    new_time = ''
    new_day = ''
    new_hours = start_hours + duration_hours
    days_later = 0
    new_minutes = start_minutes + duration_minutes

                #modulus math and get day set meridian
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_index = 0
    if starting_day:
        days_index = [day.lower() for day in days].index(starting_day.lower())

    if new_minutes >= 60:
        new_minutes = new_minutes % 60
        new_hours += 1

    if (new_hours // 12) % 2 == 0:
        new_meridian = 'AM' 
    else:
        new_meridian = 'PM'
        

    if new_hours > 12:
        if new_hours >= 24:
            days_later = new_hours // 24
            days_index = (days_index + (days_later)) % 7
            new_hours = new_hours % 12
        new_hours = new_hours % 12
    new_day = days[days_index]

    #0 hours goes to 12
    
    if new_hours < 12:
        if new_hours == 0:
            new_hours += 12
   
        # put everything into result string and format
  
    result_string = str(new_hours)
    if new_minutes < 10:
        result_string += ':0' + str(new_minutes)
    else:
        result_string += ':' + str(new_minutes)
    
    result_string += ' ' + new_meridian

    if starting_day:
        result_string += ', ' + new_day
    
    if days_later == 1:
        result_string += ' (next day)'
    elif days_later != 0:
        result_string += ' (' + str(days_later) + ' days later)'
    
    #return new_time
    return result_string

print(add_time('11:59 PM', '24:05'))


** end of main.py **

