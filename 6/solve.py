def solutions(time,distance):
    winners=0
    for ms in range(time):
        if ms*(time-ms) > distance: winners += 1
    return winners


print("Example a:",solutions(7,9)*solutions(15,40)*solutions(30,200))

print("Input a:",solutions(44,283)*solutions(70,1134)*solutions(70,1134)*solutions(80,1491))


print("Example b:",solutions(71530,940200))
print("Input b:",solutions(44707080,283113411341491))

