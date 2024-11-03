# https://www.codewars.com/kata/52742f58faf5485cae000b9a/

def format_duration(seconds: int) -> str:
    if not seconds:
        return 'now'
    yy, seconds = seconds // (3600 * 24 * 365), seconds % (3600 * 24 * 365)
    dd, seconds = seconds // (3600 * 24), seconds % (3600 * 24)
    hh, seconds = seconds // 3600, seconds % 3600
    mm, ss = seconds // 60, seconds % 60
    units = {'year': yy, 'day': dd, 'hour': hh, 'minute': mm, 'second': ss}
    time = ''
    for unit_name, unit in units.items():
        if unit:
            time += ', ' if time else ''
            time += f'{unit} {unit_name}'
            time += 's' if unit > 1 else ''
    sep_ind = time.rfind(',')
    if sep_ind > -1:
        time = time[:sep_ind] + ' and' + time[sep_ind + 1:]
    return time


print(format_duration(1))
