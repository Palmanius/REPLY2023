from copy import deepcopy
with open("path","r") as f:
    f.readline()
    f.writelines()


def Dijsktra(Gar,plants):
    global Solutions
    NewGar = deepcopy(Gar)
    Done = False
    while not Done:
        Done = True
        for y in range(len(Gar)):
            for x in range(len(Gar[0])):
                if Gar[y][x][1] != 0:
                    MyVal = Gar[y][x][1]
                    #look right
                    if x < W -1:
                        if Gar[y][x+1][1] == 0 or Gar[y][x+1][1] > MyVal+1:
                            NewGar[y][x+1][1] = MyVal+1
                            Done = False
                    #look left
                    if x > 0:
                        if Gar[y][x-1][1] == 0 or Gar[y][x-1][1] > MyVal+1:
                            NewGar[y][x-1][1] = MyVal+1
                            Done = False
                    #look up
                    if y > 0:
                        if Gar[y-1][x][1] == 0 or Gar[y-1][x][1] > MyVal+1:
                            NewGar[y-1][x][1] = MyVal+1
                            Done = False
                    #look down
                    if y < H-1:
                        if Gar[y+1][x][1] == 0 or Gar[y+1][x][1] > MyVal+1:
                            NewGar[y+1][x][1] = MyVal+1
                            Done = False
        Gar = deepcopy(NewGar)
                #finds best position to plant
    Best = [[-1,-1,0]]
    for y,row in enumerate(Gar):
        for x,col in enumerate(row):
            if col[1] > Best[0][2] and col[0] == "Y":
                Best = [[y,x,col[1]]]
            elif col[1] == Best[0][2] and col[0] == "Y":
                Best.append([y,x,col[1]])
    if plants >0:
        for p in Best:
            NewGar = deepcopy(Gar)
            NewGar[p[0]][p[1]] = ["P",1]
            #prepare for another plant
            for y,row in enumerate(NewGar):
                for x,col in enumerate(row):
                    if col[0] == "P":
                        NewGar[y][x][1] = 1
                    else: NewGar[y][x][1] = 0
            Dijsktra(NewGar,plants-1)
    else:
        Solutions.append(Best[0][2])
                                                
with open("output.txt","w") as out:
    with open("input.txt","r") as f:
        T = int(f.readline())
        for i in range(T):
            Solutions = []
            intel = f.readline().strip().split(" ")
            intel = [int(j) for j in intel]
            W = intel[0]
            H = intel[1]
            F = intel[2]
            G = intel[3]
            Garden = []
            for j in range(H):
                row = []
                for k in range(W):
                    row.append(["N",0])
                Garden.append(row)
            for j in range(G):
                Rock = f.readline().strip().split(" ")
                Rock = [int(j) for j in Rock]
                Garden[Rock[1]][Rock[0]] = ["Y",0]
            for y,row in enumerate(Garden):
                for x,col in enumerate(row):
                    if col[0] == "Y":
                        Gar = deepcopy(Garden)
                        Gar[y][x][0] = "P"
                        Gar[y][x][1] = 1
                        Dijsktra(Gar,F-1)

            out.writelines(f"Case #{i+1}: {max(Solutions)}\n")