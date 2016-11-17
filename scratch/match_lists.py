#!/usr/bin/env python3

a = set('abc')
b = set('bcd')

combie = a.union(b)

for i in combie:
    value = [
        i,
        str(i in a),
        str(i in b)
    ]
    print(','.join(value))
