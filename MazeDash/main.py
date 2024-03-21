Solutions = []
def Move(x,y,round,Motion):
    Possible = False
    for move in Moves: 
        try:
            if Map[y+move[1]][x+move[0]] == "0":
                Possible = True
                Move(x+move[0],y+move[1],round+1,Motion + [move])
        except:
            pass
    if not Possible:
        Solutions.append(round)
        #print(round,Motion)
    return round,Motion


with open("MazeDash\input.txt") as f:
    with open("MazeDash\output.txt","w") as o:
        T = int(f.readline())
        for j in range(T):
            Size, M = f.readline().split(" ")
            Map = []
            for i in range(int(Size)):
                Map.append(f.readline().split(" "))
            Moves = []
            for i in range(int(M)):
                Moves.append([int(x) for x in f.readline().split(" ")])
            Move(0,0,0,[])
            solution = min(Solutions)
            if solution % 2 == 0:
                o.write(f"Case #{j+1}: 2 {min(Solutions)}\n")
            else:
                o.write(f"Case #{j+1}: 1 {min(Solutions)}\n")
            Solutions = []