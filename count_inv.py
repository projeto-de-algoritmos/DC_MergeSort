import random
import time


INVERSIONS_SORT = 0
INVERSIONS_BRUTE = 0


def mergeArray(start, split, end, masterArray, tempArray):
    global INVERSIONS_SORT
    leftCount = start
    rightCount = split+1

    while((leftCount <= split) and (rightCount <= end)):
        print('leftCount: ', leftCount)
        print('rightCount: ', rightCount)
        print('\n')
        if(masterArray[leftCount] < masterArray[rightCount]):
            tempArray.append(masterArray[leftCount])
            leftCount += 1
        else:
            tempArray.append(masterArray[rightCount])
            INVERSIONS_SORT += (split + 1 - leftCount)
            rightCount +=1
    
    while(rightCount < end):
            tempArray.append(masterArray[rightCount])
            rightCount +=1
    while(leftCount < split):
            tempArray.append(masterArray[leftCount])
            leftCount +=1

    print('tempArray: ',tempArray)

    masterArray = tempArray
    print('masterArray: ',masterArray)


def sortArray(start, end, masterArray, tempArray):
    split = (start + end)//2

    if(start < end):
        sortArray(start, split, masterArray, tempArray)
        sortArray(split + 1, end, masterArray, tempArray)
        mergeArray(start, split, end, masterArray, tempArray)
        print(masterArray)

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

if(size < 20):
        print(masterArray)

inicio1 = time.time()
# bruteCount(masterArray)
fim1 = time.time()

inicio2 = time.time()
print('size: ',size)
sortArray(0, size - 1, masterArray, tempArray)
fim2 = time.time()

print('\n')

if(size <= 20):
    print(masterArray)

print('Numero de inversoes por forca bruta: ', INVERSIONS_BRUTE)
print('Tempo por forca bruta: ', fim1 - inicio1)
print('\n')

print('Numero de inversoes pelo merge sort', INVERSIONS_SORT)
print('Tempo pelo merge sort: ', fim2 - inicio2)
print('\n')