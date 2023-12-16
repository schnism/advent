currline = 0
cards={}

for line in open("4/input.txt"):
    currline += 1
    cards[currline] = cards.get(currline,1)
    null, data = line.replace('  ',' ').split(':')
    winning, own = data.split('|')
    winning = winning.strip().split(' ')
    own = own.strip().split(' ')

    matches =0 
    for check in own:
        if winning.count(check): 
            matches+=1


    for i in range(matches):
        cards[currline+i+1] = cards.get(currline+i+1,1) + cards[currline]


total=0
for v in cards.values():  
    total += v
print(total)
