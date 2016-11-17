import parsley

main_grammar = r"""
year = <digit{4}>:Y -> int(Y)
month = <digit{2}>:m -> int(m)
day = <digit{2}>:d -> int(d)
"""


def format_maker(name, pattern):
    replacement_list = [
        ('day', "' day:day '"),
        ('month', "' month:month '"),
        ('year', "' year:year '"),
    ]

    for original, replacement in replacement_list:
        pattern = pattern.replace(original, replacement)
        if pattern.startswith(replacement):
            pattern = pattern.lstrip("' ")
        if pattern.endswith(replacement):
            pattern = pattern.rstrip(" '")
    pattern = ' = '.join([name, pattern])
    pattern += ' -> dict(day=day, month=month, year=year)'
    return pattern


assert(format_maker('date_uk', 'day-month-year') == "date_uk = day:day '-' month:month '-' year:year -> dict(day=day, month=month, year=year)")
assert(format_maker('date_us', 'month-day-year') == "date_us = month:month '-' day:day '-' year:year -> dict(day=day, month=month, year=year)")
assert(format_maker('date_iso', 'year-month-day') == "date_iso = year:year '-' month:month '-' day:day -> dict(day=day, month=month, year=year)")


format_grammar = "\n".join([
    format_maker('date_uk', 'day-month-year'),
    format_maker('date_us', 'month-day-year'),
    format_maker('date_iso', 'year-month-day'),
])


grammar = main_grammar + format_grammar
parser = parsley.makeGrammar(grammar, {})


if __name__ == '__main__':
    print 'UK: 11-22-1234 ->', parser('11-22-1234').date_uk()
    print 'US: 11-22-1234 ->', parser('11-22-1234').date_us()
    print 'ISO: 1234-22-11 ->', parser('1234-22-11').date_iso()
    assert(parser('11-22-1234').date_uk() == dict(day=11, month=22, year=1234))
    assert(parser('11-22-1234').date_us() == dict(day=22, month=11, year=1234))
    assert(parser('1234-22-11').date_iso() == dict(day=11, month=22, year=1234))
