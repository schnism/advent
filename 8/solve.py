lines = open("8/input.txt").readlines()

instructions = lines.pop(0)

lines.pop(0)

position = 'AAA'

map={}

for line in lines:
    line = line.replace(' ','').replace('(','').replace(')','').replace('=',',')
    node,nextl,nextr = line.split(',')
    map[node]=(nextl,nextr.strip())



step=0
while position!='ZZZ':
    if instructions[step%(len(instructions)-1)] == 'L':
        position=map[position][0]
    else:
        position=map[position][1]
    step+=1

print("Needed steps:",step)