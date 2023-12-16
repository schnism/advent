
lines = open("5/input.txt").readlines()
locations=[]

for seed in lines[0].split(':')[1].strip().split(' '):
    seed=int(seed)
    new=seed
    print("New seed",seed)

    for line in lines:
        if(line[0].isnumeric()):
            dest,start,len = line.split(' ')
            dest=int(dest)
            start=int(start)
            len=int(len)
            if seed>=start and seed<start+len:
                new = dest + seed-start
                skip=True
                print(seed," mapped to ",new)
        
        if(line.find("map")>0):
            print(line)
            seed=new
            

    locations.append(new) 

locations.sort()

print("Solution:" , locations[0])
            

