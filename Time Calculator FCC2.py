def day_clean(day):
    alps = 0
    l1d = []
    if day != '':
        for char in day:
            if alps == 0:
                char = char.upper()
            else:
                char = char.lower()
            alps += 1
            l1d.append(char)
        day = ''.join(l1d)
    return day


def change_ap(ap):
    return 'PM' if ap == 'AM' else 'AM'


def add_hour(m3, h3):
    return h3 + 1 if m3 > 60 else h3


def add_lead(m3):
    return '0' + str(m3) if m3 < 10 else m3


def add_day(h1, d_int):
    return d_int+1 if h1 + d_int > 12 else d_int


def day_count(day, d_num=0):
    i, actual = 0, 0
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day in days:
        i = days.index(day)
        actual = d_num + i
        return days[actual % 7] if actual > 6 else days[actual]


def add_time(start, duration, day=''):
    day = day_clean(day) if day != '' else ''
    if ':' in start:
        start = start.replace(':', ' ')
    lis1 = start.split()
    lis2 = duration.split(':')
    # print(lis1, lis2)
    h1, h2 = int(lis1[0]), int(lis2[0])
    m1, m2 = int(lis1[1]), int(lis2[1])
    ap = lis1[2]
    finh, finm, finap, d_late, d_int, d_mod = 0, 0, '', '', 0, 0
    h3 = h1 + h2
    m3 = m1 + m2
    if h2 == 00:
        h3 = add_hour(m3, h3)
        ap = change_ap(ap) if h3 == 12 else ap
        m3 = m3 % 60
        m3 = add_lead(m3)
        finap = ap
        finh = str(h3)
        finm = str(m3)
        if day == '':
            return f'{finh}:{finm} {ap}' if d_late == '' else f'{finh}:{finm} {ap} {d_late}'
        else:
            return f'{finh}:{finm} {ap}, {day}' if d_late == '' else f'{finh}:{finm} {ap}, {day} {d_late}'
    if h2 == 24:
        if m3 < 60:
            h3 = h1
            ap = lis1[2]
            d_late = '(next day)'
            day = day_count(day, 1) if day != '' else ''
        else:
            h3 = add_hour(m3, h3)
            h3 = h3 % 24 if h3 > 24 else h3
            m3 = m3 % 60
            m3 = add_lead(m3)
            if h3 == 12:
                ap = change_ap(ap)
                d_late = '(2 days later)'
                day = day_count(day, 2) if day != '' else ''
        finap = ap
        finh = str(h3)
        finm = str(m3)
        if day == '':
            return f'{finh}:{finm} {ap}' if d_late == '' else f'{finh}:{finm} {ap} {d_late}'
        else:
            return f'{finh}:{finm} {ap}, {day}' if d_late == '' else f'{finh}:{finm} {ap}, {day} {d_late}'
    if h2 > 24:
        if h2 % 24 == 0:
            # print('here1')
            d_int = (h2 // 24)
            # if h1 + d_mod:
        elif h2 % 24 != 0:
            d_int = (h2 // 24)
            d_mod = h2 % 24
            d_int = add_day(h1, d_int)
            if h1 + d_mod < 12:
                # print('here2')
                h3 = h1 + d_mod
                h3 = add_hour(m3, h3)
                m3 = m3 % 60 if m3 > 60 else m3
                ap = lis1[2]
            elif h1 + d_mod == 12:
                # print('here3')
                h3 = h1 + d_mod
                h3 = add_hour(m3, h3)[0]
                m3 = m3 % 60 if m3 > 60 else m3
                ap = change_ap(ap)
            elif 12 < h1 + d_mod < 24:
                # print('yes')
                h3 = h1 + d_mod
                m3 = m1 + m2
                if h3 == 24:
                    # print('here4')
                    h3 = h1
                    m3 = add_lead(m3)
                    ap = lis1[2]
                else:
                    # print('here5')
                    h3 = h3 % 12
                    h3 = add_hour(m3, h3)
                    m3 = m3 % 60 if m3 > 60 else m3
                    m3 = add_lead(m3)
                    ap = change_ap(ap)
                    #
        finh = str(h3)
        finm = str(m3)
        # print(d_int)
        d_late = f'({str(d_int)} days later)'
        day = day_count(day, d_int) if day != '' else ''
        if day == '':
            return f'{finh}:{finm} {ap}' if d_late == '' else f'{finh}:{finm} {ap} {d_late}'
        else:
            return f'{finh}:{finm} {ap}, {day}' if d_late == '' else f'{finh}:{finm} {ap}, {day} {d_late}'
    if h3 < 12:
        finh = str(h3)
        finm = str(m3)
        ap = lis1[2]
    if h3 >= 12:
        # print('yes')
        h3 = h3 % 12
        h3 = add_hour(m3, h3)
        m3 = m3 % 60 if m3 > 60 else m3
        m3 = add_lead(m3)
        ap = change_ap(ap)
        day = day_count(day) if day != '' else ''
        finh = str(h3)
        finm = str(m3)
        d_late = '(next day)' if ap == 'AM' else ''
    if day == '':
        return f'{finh}:{finm} {ap}' if d_late == '' else f'{finh}:{finm} {ap} {d_late}'
    else:
        return f'{finh}:{finm} {ap}, {day}' if d_late == '' else f'{finh}:{finm} {ap}, {day} {d_late}'

print(add_time('3:00 PM', '3:10'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
