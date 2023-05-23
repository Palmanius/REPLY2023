with open("output.txt","r",encoding="UTF16") as f:
    File = []
    for l in f:
        File.append(l.strip())

print(File)