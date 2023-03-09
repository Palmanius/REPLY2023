with open("input.txt","r") as f:
    with open("output.txt","w") as out:
        T = int(f.readline().strip())
        for i in range(int(T)):
            intel = f.readline().strip().split(" ")
            N = int(intel[0])
            BF = int(intel[1])
            BI = int(intel[2])
            play = 0
            Games = 0
            Slots = []
            Budget = BI
            for j in range(N):
                slot = f.readline().strip().split(" ")
                slot = [int(k) for k in slot]
                slot.append(slot[1]-slot[0])
                Slots.append(slot)
            Slots.sort(key=lambda a:-a[2])


            while Budget < BF:
                if Slots[play][0] <= Budget:
                    if play > 0:
                        Budget += Slots[play][2]
                        Games += 1
                        play-=1
                    else:
                        Games += (BF - Budget) // Slots[play][2]
                        if (BF - Budget) % Slots[play][2] > 0:
                            Games +=1
                        break
                else: play +=1
            out.writelines("Case #"+str(i+1)+": "+str(Games))
            out.writelines("\n")
