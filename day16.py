import re
import math
import fileinput

fields, your_ticket, tickets = [group.split('\n') for group in ''.join(
    fileinput.input('data/day16.txt')).split('\n\n')]

field_ranges = {}
for row in fields:
    field, *fromto = re.match(
        r'(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', row).groups()
    field_ranges[field] = list(map(lambda x: int(x), fromto))


def parse_ticket(ticket_row):
    return list(map(lambda x: int(x), ticket_row.split(',')))


your_ticket = parse_ticket(your_ticket[1])
tickets = [parse_ticket(x) for x in tickets[1:] if x.strip()]


def validate_field(field):
    for from1, to1, from2, to2 in field_ranges.values():
        if from1 <= field <= to1 or from2 <= field <= to2:
            return True
    return False


def get_error_rate(ticket):
    return sum([field for field in ticket if not validate_field(field)])


print(sum(map(get_error_rate, tickets)))

# part 2


def get_valid_fields(value):
    fields = set()
    for field in field_ranges:
        from1, to1, from2, to2 = field_ranges[field]
        if from1 <= value <= to1 or from2 <= value <= to2:
            fields.add(field)
    return fields


valid_tickets = list(filter(lambda t: all(map(validate_field, t)), tickets))
valid_fields = [0]*len(your_ticket)
for i in range(len(your_ticket)):
    valid_fields[i] = set(field_ranges.keys())
    for ticket in valid_tickets:
        valid_fields[i] &= get_valid_fields(ticket[i])


field_position_map = {}


def determine_next_field():
    for i, fields in enumerate(valid_fields):
        if i not in field_position_map.values() and len(fields) == 1:
            field_position_map[next(iter(fields))] = i
            for j in range(len(valid_fields)):
                if i != j:
                    valid_fields[j] -= fields
            return


for i in range(len(your_ticket)):
    determine_next_field()

dep_fields = [your_ticket[field_position_map[field]]
              for field in field_position_map if field.startswith('departure')]
print(math.prod(dep_fields))
