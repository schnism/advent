def sortkey(hand):
    res=""
    for h in hand[0]:
        res += alpha[cards.find(h)]
    return res


cards = '23456789TJQKA'
alpha = 'ABCDEFGHIJKLM'

lines = open("7/input.txt").readlines()
hands = []

for line in lines:

    hand,bet = line.split(' ')
    bet=int(bet)


    counter={}
    for c in cards:
        for h in hand:
            if c==h: counter[c] = counter.get(c,0)+1

    x = list(counter.values())
    x.sort(reverse=True)

    if x[0]==5: hclass=8
    if x[0]==4: hclass=7
    if x[0]==3 and x[1]==2: hclass=6
    if x[0]==3 and x[1]<2: hclass=5
    if x[0]==2 and x[1]==2: hclass=4
    if x[0]==2 and x[1]<2: hclass=3
    if x[0]==1: hclass=2
    hand = str(hclass) + hand

    hands.append((hand,bet))




rank=0
winning=0
for hand in sorted(hands,key=sortkey):
    rank += 1 
    winning += rank*hand[1]

print(winning)




