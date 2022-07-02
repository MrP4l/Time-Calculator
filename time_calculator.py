def add_time(start, duration, day=None):
    days_array = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Get the start time splitted
    o = start.split()
    ampm = o[1]
    a = o[0].split(':')
    HourS = a[0]
    MinuteS = a[1]

    # Get the duration time splitted
    h = duration.split()
    b = h[0].split(':')
    HourD = b[0]
    MinuteD = b[1]

    # Counting the hour
    MinuteDD = (int(HourD) * 60) + int(MinuteD)
    
    # Duration time in minutes
    MinFin = (int(MinuteS) + int(MinuteD)) % 60
    HouFin = ((int(HourS) * 60 + int(MinuteS) + MinuteDD) // 60) % 12

    # AM or PM
    HH = ((int(HourS) * 60 + int(MinuteS) + MinuteDD) // 60) % 24
    HB = ((int(HourS) * 60 + int(MinuteS) + MinuteDD) // 60)
    AMPM = ampm
    AMPM = 'AM' if HH < 12 else "PM"
    if ampm == 'PM':
        AMPM = 'PM' if HH < 12 else "AM"
    if MinFin < 10:
        MinFin = '0' + (str(MinFin))
    if HouFin == 0:
        HouFin = 12

    # Counting the days
    ND = '(next day)'
    days_later = 0
    if ampm == 'PM' and HB > 12:
        if HB % 24 >= 1.0:
            days_later += 1
    if HB >= 12:
        hours_left = HB / 24
        days_later += int(hours_left)

    if day is not None:
        day = day.strip().lower()
        selected_day = int((days_array.index(day) + days_later) % 7)
        current_day = days_array[selected_day]
        if days_later < 1:
            new_time = ''.join(str(HouFin) + ':' + str(MinFin) + ' ' + AMPM + ',' + ' ' + current_day.capitalize())
            return new_time
        if days_later == 1:
            new_time = ''.join(
                str(HouFin) + ':' + str(MinFin) + ' ' + AMPM + ',' + ' ' + current_day.capitalize() + ' ' + ND)
            return new_time
        if days_later > 1:
            new_time = ''.join(
                str(HouFin) + ':' + (str(MinFin)) + ' ' + AMPM + ',' + ' ' + current_day.capitalize() + ' ' + '(' + str(
                    days_later) + ' ' + 'days later' + ')')
            return new_time

    if day is None:
        if days_later < 1:
            new_time = ''.join(str(HouFin) + ':' + str(MinFin) + ' ' + AMPM)
            print(new_time)
        if days_later == 1:
            new_time = ''.join(str(HouFin) + ':' + str(MinFin) + ' ' + AMPM + ' ' + ND)
            print(new_time)
        if days_later > 1:
            new_time = ''.join(
                str(HouFin) + ':' + (str(MinFin)) + ' ' + AMPM + ' ' + '(' + str(days_later) + ' ' + 'days later' + ')')
            print(new_time)

        return new_time










