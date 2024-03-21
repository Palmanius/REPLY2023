with open("Task1\\input.txt","r") as f:
    with open("Task1\\output.txt","w") as out:
        N = f.readline()
        for i in range(int(N)):
            Case = [int(x) for x in f.readline().strip().split(" ")]
            Min = Case[0]
            Max = Case[1]
            LMia = Case[2]
            LGenga = Case[3]
            W = Case[4]
            Mia = sorted([int(x) for x in f.readline().strip().split(" ")],reverse=True)
            Genga = sorted([int(x) for x in f.readline().strip().split(" ")],reverse=True)

        
            Turns = 0
            Runs = []

            while len(Mia) > 0 and len(Genga) > 0:
                RemMia = []
                RemGenga = []
                if Mia[0] > Genga[0]:
                    RemMia.append(Mia.pop(0))
                    if sum(RemMia) < W:
                        if W - sum(RemMia) in Mia:
                            RemMia.append(Mia.pop(Mia.index(W-(sum(RemMia)))))
                        elif Mia[-1] < W - sum(RemMia):
                            RemMia.append(Mia.pop(-1))
                        else:
                            while True:
                                i=0
                                if sum(RemGenga) == sum(RemMia) or i >= len(Genga):
                                    break
                                if Genga[i] <= sum(RemMia) - sum(RemGenga):
                                    RemGenga.append(Genga.pop(i))
                                else: i+=1
                else:
                    RemGenga.append(Genga.pop(0))
                    if sum(RemGenga) < W:
                        if W - sum(RemGenga) in Genga:
                            RemGenga.append(Genga.pop(Genga.index(W-(sum(RemGenga)))))
                        elif Genga[-1] < W - sum(RemGenga):
                            RemGenga.append(Genga.pop(-1))
                        else:
                            while True:
                                i=0
                                if sum(RemMia) == sum(RemGenga) or i >= len(Mia):
                                    break
                                if Genga[i] <= sum(RemGenga) - sum(RemMia):
                                    RemMia.append(Mia.pop(i))
                                else: i+=1
                Runs.append(RemMia+[0]+RemGenga)
                Turns+=1
                        
                    



            out.writelines(f"Case #{i+1}: {Turns}")
            for run in Runs:
                out.writelines(str(run))






