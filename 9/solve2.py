def allzero(data):
    ret=True
    for d in data:
        if d!=0: ret=False
    return ret



total=0


for line in open("9/input.txt").read().splitlines():
    data=[]
    data.append([int(s) for s in line.split(' ')])
        
    y=0
    while not(allzero(data[y])):
        data.append([])
        for x in range(len(data[y])-1):
            data[y+1].append(data[y][x+1] - data[y][x])
        y+=1


    data[y].append(0)

    for y in range(y,0,-1):
        data[y-1].append(data[y-1][-1] + data[y][-1])
    
    total += data[0][-1]


print(total)


