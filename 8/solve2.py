def allintarget(positions):
    res=True
    for position in positions:
        if position[2]!='Z': res=False
    return res

lines = open("8/input.txt").readlines()

instructions = lines.pop(0)

lines.pop(0)

positions=[]

map={}

for line in lines:
    line = line.replace(' ','').replace('(','').replace(')','').replace('=',',')
    node,nextl,nextr = line.split(',')
    map[node]=(nextl,nextr.strip())
    if node[2]=='A': positions.append(node)


print(positions)


step=0
while not allintarget(positions):
    newpositions=[]
    if instructions[step%(len(instructions)-1)] == 'L':
        for position in positions:
            newpositions.append(map[position][0])
    else:
        for position in positions:
            newpositions.append(map[position][1])
    print(step,positions)
    positions=newpositions
    step+=1

print("Needed steps:",step)