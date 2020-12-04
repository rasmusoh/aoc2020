import re
import fileinput

req_fields = (
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
)  # (Country ID)

r = re.compile(r'([^\s\\]+):([^\s\\]+)')
passports = []
current = []
for line in fileinput.input():
    if not line.rstrip():
        if current:
            passports.append({kv[0]: kv[1] for kv in current})
            current = []
    else:
        current += r.findall(line)
if current:
    passports.append({kv[0]: kv[1] for kv in current})

valids = 0
for passport in passports:
    present = all([field in passport for field in req_fields])
    if not present:
        continue
    valid = {}
    valid['byr'] = 1920 <= int(passport['byr']) <= 2002
    valid['iyr'] = 2010 <= int(passport['iyr']) <= 2020
    valid['eyr'] = 2020 <= int(passport['eyr']) <= 2030

    hgt_cm = re.match(r'([0-9]+)cm$', passport['hgt'])
    hgt_in = re.match(r'([0-9]+)in$', passport['hgt'])
    hgt_cm_valid = hgt_cm and 150 <= int(hgt_cm.group(1)) <= 193
    hgt_in_valid = hgt_in and 59 <= int(hgt_in.group(1)) <= 76
    valid['hgt'] = hgt_cm_valid or hgt_in_valid
    valid['hcl'] = bool(re.match('#[0-9|a-f]{6}$', passport['hcl']))
    valid['ecl'] = passport['ecl'] in (
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    valid['pid'] = bool(re.match('[0-9]{9}$', passport['pid']))
    if all(valid.values()):
        valids += 1
    else:
        for field in valid:
            if not valid[field]:
                print(f'{field}: {passport[field]}')
print(valids)
