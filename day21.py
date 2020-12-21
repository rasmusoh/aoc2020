import fileinput

possible_ingredients = {}
all_ingredients = set()
ingredient_lists = []
for line in fileinput.input('data/day21.txt'):
    ingredients, alergens = line.split('(contains')
    alergens = alergens.strip().rstrip(')').split(', ')
    ingredients = set(ingredients.strip().split(' '))
    all_ingredients = all_ingredients | ingredients
    ingredient_lists.append(ingredients)
    for alergen in alergens:
        if alergen in possible_ingredients:
            possible_ingredients[alergen] = possible_ingredients[alergen] & ingredients
        else:
            possible_ingredients[alergen] = ingredients

# part 1
safe_ingredients = all_ingredients
for alergen in possible_ingredients:
    safe_ingredients -= possible_ingredients[alergen]
print(len([ingredient for ingredients in ingredient_lists
           for ingredient in ingredients
           if ingredient in safe_ingredients]))

# part 2
alergens = {}
for _ in range(len(possible_ingredients)):
    for alergen in possible_ingredients:
        if len(possible_ingredients[alergen]) == 1:
            alergens[alergen] = next(iter(possible_ingredients[alergen]))
            for alergen2 in possible_ingredients:
                possible_ingredients[alergen2].discard(alergens[alergen])
            break

canonical = list(alergens.keys())
canonical.sort()
print(','.join(map(lambda x: alergens[x], canonical)))
