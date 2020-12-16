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


def valid_for_fields(value):
    fields = set()
    for field in field_ranges:
        from1, to1, from2, to2 = field_ranges[field]
        if from1 <= value <= to1 or from2 <= value <= to2:
            fields.add(field)
    return fields


def get_error_rate(ticket):
    return sum([value for value in ticket if not valid_for_fields(value)])


print(sum(map(get_error_rate, tickets)))

# part 2

valid_tickets = list(filter(lambda t: all(map(valid_for_fields, t)), tickets))

possible_fields = []
for i in range(len(your_ticket)):
    fields = valid_for_fields(your_ticket[i])
    for ticket in valid_tickets:
        fields &= valid_for_fields(ticket[i])
    possible_fields.append(fields)

field_position_map = {}
for _ in range(len(your_ticket)):
    for i, fields in enumerate(possible_fields):
        if len(fields) == 1:
            field = next(iter(fields))
            field_position_map[field] = i
            for position in possible_fields:
                position.discard(field)
            break

dep_fields = [your_ticket[field_position_map[field]]
              for field in field_position_map if field.startswith('departure')]
print(math.prod(dep_fields))
