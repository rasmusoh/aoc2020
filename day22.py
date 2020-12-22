import fileinput
import operator

player1, player2 = [group for group in
                    ''.join(fileinput.input(
                        'data/day22.test.txt')).split('\n\n')
                    if group]
player1 = [int(x) for x in player1.split('\n') if x.isnumeric()]
player2 = [int(x) for x in player2.split('\n') if x.isnumeric()]


def play(player1, player2, subgame=1):
    rounds = 0
    history = set()
    gamestate = (tuple(player1), tuple(player2))
    while player1 and player2 and gamestate not in history:
        rounds += 1
        history.add(gamestate)

        p1_card = player1.pop(0)
        p2_card = player2.pop(0)
        winner = None
        if len(player1) >= p1_card and len(player2) >= p2_card:
            winner, _ = play(player1[:p1_card],
                             player2[:p2_card], subgame+1)
        else:
            winner = 1 if p1_card > p2_card else 2
        if winner == 1:
            player1.append(p1_card)
            player1.append(p2_card)
        else:
            player2.append(p2_card)
            player2.append(p1_card)
        gamestate = (tuple(player1), tuple(player2))

    if player2 and not player1:
        return 2, player2
    return 1, player1


winner_p, winner_deck = play(player1, player2)
print(winner_p, winner_deck)
score = sum(map(operator.mul, winner_deck,
                reversed(range(1, 1+len((winner_deck))))))
print(score)
