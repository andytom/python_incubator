def group_runs(iterable, test_func):
    my_iter = iter(iterable)

    run = [next(my_iter)]

    for i in my_iter:
        if test_func(run[-1], i):
            run.append(i)
        else:
            yield run
            run = [i]
    yield run


# - Tests with Numbers -------------------------------------------------------#
numbers = [1, 2, 2, 3, 5, 6, 9, 10, 11, 15, 16]

def test_within_one(prev, current):
    return current - prev <= 1


print list(group_runs(numbers, test_within_one))

for i in group_runs(numbers, test_within_one):
    print "{}: {}".format(len(i), i)

print '-' * 80


# - Tests with Dates ---------------------------------------------------------#
from datetime import date, timedelta

dates = [
    date(2015, 1, 1),
    date(2015, 1, 2),
    date(2015, 1, 3),
    date(2015, 1, 4),

    date(2015, 1, 6),
    date(2015, 1, 7),

    date(2015, 1, 10),

    date(2015, 2, 6),
    date(2015, 2, 7),
    date(2015, 2, 8),

    date(2015, 2, 10),
    date(2015, 2, 11),
    date(2015, 2, 12),
    date(2015, 2, 13),
]

def test_date(prev, current):
    return current - prev <= timedelta(1)

runs = list(group_runs(dates, test_date))

for i in runs:
    print "{}: {}".format(len(i), i)

print 'max: {}'.format(max(*runs, key=len))
