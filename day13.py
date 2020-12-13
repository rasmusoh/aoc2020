import math
from functools import reduce
from itertools import count
from fileinput import input

inputdata = [line.rstrip() for line in input('data/day13.txt')]

# part 1
time = int(inputdata[0])
buses = [int(bus) for bus in inputdata[1].split(',') if bus.isnumeric()]
departures = list(map(lambda bus: next(
    filter(lambda x: x >= time, count(0, bus))), buses))
earliest_bus_leave = min(departures)
print('earliest bus to catch:')
print((earliest_bus_leave - time)*buses[departures.index(earliest_bus_leave)])

# part 2

buses = [(int(bus), offset) for offset, bus in enumerate(
    inputdata[1].split(',')) if bus.isnumeric()]
earliest = 0
period = 1
for bus_period, bus_offset in buses:
    for departure in count(earliest, period):
        if (departure + bus_offset) % bus_period == 0:
            earliest = departure
            period = period*bus_period//math.gcd(period, bus_period)
            break
print('earliest consecutive:')
print(earliest)
