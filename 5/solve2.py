
import sys
lines = open("5/input.txt").readlines()
locations=[]
seeds=[]
solution=0
loops=0

seedline = lines[0].split(':')[1].strip().split(' ')


total=0

for i in range(0,len(seedline),2):
    total+=int(seedline[i+1])

print(total)

exit


for i in range(0,len(seedline),2):
    for seed in range(int(seedline[i]),int(seedline[i])+int(seedline[i+1])):
        new=seed
        loops += 1

        for line in lines:
            if(line[0][0] in ('0','1','2','3','4','5','6','7','8','9')):
                dest,start,len = line.split(' ')
                dest=int(dest)
                start=int(start)
                len=int(len)
                if seed>=start and seed<start+len:
                    new = dest + seed-start
                    skip=True
            
            if(line[0] in ('s','f','w','l','t','h')):
                seed=new

        if new<solution or solution==0: solution=new
        if loops%10000==0: print(loops/total*100 , "% done")
        



print("Solution:" , solution)
