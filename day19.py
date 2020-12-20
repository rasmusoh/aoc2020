import fileinput
import itertools

rules, messages = list(map(lambda x: x.split('\n'), ''.join(
    fileinput.input('data/day19.txt')).split("\n\n")))

grammar = [None]*len(rules)
for rule in rules:
    ruleid, rule = rule.split(': ')
    if '"' in rule:
        grammar[int(ruleid)] = rule[1]
    else:
        grammar[int(ruleid)] = [list(
            map(lambda x: int(x), pair.strip().split(' '))) for pair in rule.split('|')]


def validate(message):
    def dovalidation(msg, rule):
        if isinstance(grammar[rule], str):
            if msg.startswith(grammar[rule]):
                return True, msg[1:]
            else:
                return False, None
        else:
            for alt in grammar[rule]:
                rest = msg
                valid = True
                for part in alt:
                    valid, rest = dovalidation(rest, part)
                    if not valid:
                        break
                if valid:
                    return True, rest
            return False, None
    result, rest = dovalidation(message, 0)
    return result and not rest


def expand(rule):
    if isinstance(grammar[rule], str):
        return grammar[rule]
    else:
        alts = []
        for alt in grammar[rule]:
            tot = ['']
            for part in alt:
                partalts = expand(part)
                tot = [''.join(x) for x in itertools.product(tot, partalts)]
            alts += tot
        return alts


rule31 = expand(31)
rule42 = expand(42)


def validate_part2(msg):
    rest = msg
    l = len(rule42[0])
    while len(rest) > l and rest[:l] in rule42:
        rest = rest[l:]
    if len(rest) >= len(msg)/2:
        return False
    while rest[:l] in rule31:
        rest = rest[l:]
        if len(rest) == 0:
            return True
    return False


print(sum(map(validate, messages)))
print(sum(map(validate_part2, messages)))
