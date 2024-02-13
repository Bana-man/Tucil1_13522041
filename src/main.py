import random
import time

def countPoint(arrPos):
    counter = 0
    arraySeqBaru = [x[0] for x in arrSeq]
    currSeq = [0 for x in arraySeqBaru]

    for i in range(len(arrPos)):
        for j in range(len(currSeq)):
            if currSeq[j] == "Done":
                continue
            if (matriks[arrPos[i][0]][arrPos[i][1]] == arraySeqBaru[j][currSeq[j]]):
                currSeq[j] += 1
                if currSeq[j] == len(arraySeqBaru[j]):
                    currSeq[j] = "Done"
                    counter += arrSeq[j][1]
            else:
                currSeq[j] = 0
    return counter

print("1. Read from File \n2. Generate Random by Input \n")
pilihan = input("Choose 'Initialize Game' Method: ") 

if (pilihan == '1'):
    namaFile = input("Masukkan nama file: ")
    file = open("test/" + namaFile, "r")

    bufSize = int(file.readline())
    matSize = file.readline().split()

    matriks = []
    for i in range(int(matSize[1])):
        row = file.readline().split()
        matriks.append(row)
    
    nSeq = int(file.readline())
    arrSeq = []
    for i in range(nSeq):
        seq = file.readline().split()
        rew = int(file.readline())
        arrSeq.append([seq, rew])

    file.close()

elif (pilihan == '2'):
    nToken = input("Jumlah Token Unik: ")
    listToken = input("Token Unik: ").split()

    bufSize = int(input("Ukuran Buffer: "))
    matSize = input("Ukuran Matriks: ").split()

    matriks = []
    for i in range(int(matSize[1])):
        row = []
        for j in range(int(matSize[0])):
            elmt = random.choice(listToken)
            row.append(elmt)
        matriks.append(row)

    nSeq = int(input("Jumlah Sekuens: "))
    lenMaxSeq = int(input("Panjang Maksimal Sekuens: "))

    arrSeq = []
    for i in range(nSeq):
        lenSeq = random.randint(2, lenMaxSeq)
        seq = []
        while (seq == [] or [seq] in arrSeq): # Prevent same sequence to appear
            for j in range(lenSeq):
                elmt = random.choice(listToken)
                seq.append(elmt)
        arrSeq.append([seq])
        
    for i in range(nSeq):
        rew = random.randint(-50, 50)
        arrSeq[i].append(rew)

    print("\nSekuens: ")
    for i in arrSeq:
        print(i)
    print("\nMatriks: ")
    for i in matriks:
        print(i)
else:
    print("Invalid Input")
    exit()

arrSeq.sort(key=lambda x: x[1], reverse=True)

awal = time.time()

maxPoint = 0
maxSeq = []

def bruteforce(arrP):
    global maxPoint
    global maxSeq
    arrPos = [a for a in arrP]
    for i in range(int(matSize[1])):
        currCol = arrPos[-1][1]
        if (len(arrPos) == bufSize):
            continue
        elif ([i, currCol] in arrPos):
            continue
        else:
            arrPos.append([i, currCol])
            poin = countPoint(arrPos)

            if (poin == maxPoint and len(maxSeq) > len(arrPos)):
                maxSeq = [a for a in arrPos]
            elif poin>maxPoint:
                maxPoint = poin
                maxSeq = [a for a in arrPos]

        for j in range(int(matSize[0])):
            if (len(arrPos) == bufSize):
                continue
            elif ([i, j] in arrPos):
                continue   
            else:
                arrPos.append([i, j])
                poin = countPoint(arrPos)

                if (poin == maxPoint and len(maxSeq) > len(arrPos)):
                    maxSeq = [a for a in arrPos]
                elif poin>maxPoint:
                    maxPoint = poin
                    maxSeq = [a for a in arrPos]
                
                bruteforce(arrPos)

                arrPos.pop()

        arrPos.pop()

for i in range(int(matSize[0])):
    bruteforce([[0, i]])

akhir = time.time()

print("\nOutput: ")
strMaxSeq = ""
for [x,y] in maxSeq:
    strMaxSeq += (matriks[x][y] + " ")
strLocSeq = ""
for [x,y] in maxSeq:
    strLocSeq += (str(y+1)+", "+str(x+1)+"\n")

print(maxPoint)
print(strMaxSeq)
print(strLocSeq)

print(str(int((akhir - awal)*1000)) + " ms")

saveState = input("\nApakah ingin menyimpan solusi? (y/n)  ")
if (saveState == 'y'):
    filename = input("Masukkan nama file: ")
    file = open("test/"+filename, "w")
    file.write(str(maxPoint))
    file.write('\n')
    file.write(strMaxSeq)
    file.write('\n')
    file.write(strLocSeq)
    file.close()