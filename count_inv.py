import random
import time


INVERSIONS_SORT = 0
INVERSIONS_BRUTE = 0


def mergeArray(start, split, end, masterArray, tempArray):
    global INVERSIONS_SORT
    leftCount = start
    rightCount = split+1
    tempCount = start

    while((leftCount <= split) and (rightCount <= end)):
        if(masterArray[leftCount] <= masterArray[rightCount]):
            tempArray[tempCount] = masterArray[leftCount]
            leftCount += 1
        else:
            tempArray[leftCount] = masterArray[rightCount]
            INVERSIONS_SORT += (split + 1 - leftCount)
            rightCount +=1
        tempCount +=1
    
    if(leftCount > split):
        while(rightCount < end):
            tempArray[tempCount] = masterArray[rightCount]
            tempCount +=1
            rightCount +=1
    else:
        while(leftCount < split):
            tempArray[tempCount] = masterArray[leftCount]
            tempCount +=1
            leftCount +=1

    masterArray = tempArray


def sortArray(start, end, masterArray, tempArray):
    split = (start + end)/2

    if(start < end):
        sortArray(start, split, masterArray, tempArray)
        sortArray(split + 1, end, masterArray, tempArray)
        mergeArray(start, split, end, masterArray, tempArray)

def bruteCount(masterArray):
    global INVERSIONS_BRUTE
    i=0
    while(i<len(masterArray)):
        j = i + 1
        while(j < len(masterArray)):
            if(masterArray[i] > masterArray[j]):
                INVERSIONS_BRUTE += 1
        i+=1


size = int(input('Informe o tamanho do vetor: '))

masterArray = []
tempArray = []

if(size < 1000000):
    for i in range(size):
       masterArray.append(random.randint(0,1000))
       continue

if(size < 20):
        print(masterArray)

inicio1 = time.time()
bruteCount(masterArray)
fim1 = time.time()

inicio2 = time.time()
sortArray(0, size - 1, masterArray, tempArray)
fim2 = time.time()

print('\n')

if(size <= 20):
    print(masterArray)

print('Numero de inversoes por forca bruta: ', INVERSIONS_BRUTE)
print('Tempo por forca bruta: ', fim1 - inicio1)
print('\n')

print('Numero de inversoes pelo merge sort')
print('Tempo pelo merge sort: ', fim2 - inicio2)
print('\n')