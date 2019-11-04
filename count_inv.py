import array as arr
import random
import time

INVERSIONS_SORT = 0
INVERSIONS_BRUTE = 0


# Python program for implementation of MergeSort 
def mergeSort(arr):
    global INVERSIONS_SORT
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j]
                INVERSIONS_SORT = INVERSIONS_SORT + (len(L) + 1 - j);
                j+=1
            k+=1

        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
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
mergeSort(masterArray)
fim2 = time.time()

print('\n')

if(size <= 20):
    print(masterArray)

print('Numero de inversoes por forca bruta: ', INVERSIONS_BRUTE)
print('Tempo por forca bruta: ', fim1 - inicio1)
print('\n')

print('Numero de inversoes pelo merge sort: ', INVERSIONS_SORT)
print('Tempo pelo merge sort: ', fim2 - inicio2)
print('\n')
