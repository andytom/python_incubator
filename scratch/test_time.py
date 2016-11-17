"""
Select an item from a list based on the time (so the same item is selected for
the same second)
"""
import time

a = list(range(6))

print a

i = int(time.time()) % len(a)

print "selected item:",  a[i]
