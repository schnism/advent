total=0

for line in open("input.txt"):
    points=0
    null, data = line.replace('  ',' ').split(':')
    winning, own = data.split('|')
    winning = winning.strip().split(' ')
    own = own.strip().split(' ')
    for check in own:
        if winning.count(check): 
            if points==0:
                points=1
            else:
                points *=2
    total += points

print(total)
