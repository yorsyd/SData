def addDataArray(arr, newData):
    # Membuat array baru dengan ukuran yang lebih besar
    newArr = [None] * (len(arr) + 1)

    # Menyalin data dari array lama ke array baru
    for i in range(len(arr)):
        newArr[i] = arr[i]

    # Menambahkan data baru ke akhir array
    newArr[-1] = newData

    return newArr
    
def delDataArr(arr, arrSize, position):
    for i in range(position, arrSize-1, 1):
        arr[i] = arr[i+1]
    tempArr = [None] * (arrSize-1)
    print(tempArr)
    for i in range(0, arrSize-1,1):
        tempArr[i] = arr[i]
    return tempArr

arr = [1,2,3,4,5]
arr = addDataArray(arr,5)
# print(arr)
# addDataArray(arr,2)
delDataArr(arr, 5, 2)
print(arr)

def kali(ll):
    hasil = 1
    while ll:
        hasil = hasil * ll['data']
        ll = ll['next']
    return hasil

def addCircuralHead(ll, newData):
    newNode = {'data': newData, 'next': None}

    if ll is None:
        newNode['next'] = newNode
    else:
        tempLL = ll
        while tempLL['next'] != ll:
            tempLL = tempLL['next']
        newNode['next'] = ll
        tempLL['next'] = newNode

    return newNode

def dotProduct(ll):
    hasil = 1
    while ll is not None:
        data = ll['data']
        hasil = hasil * (data * data)
        ll = ll['next']
    return hasil

def delEvenData(ll):
    tempLL = ll
    while tempLL['next']:
        if tempLL['next']['data'] % 2 == 0:
            tempLL['next'] = tempLL['next']['next']
        else:
            tempLL = tempLL['next']
    return ll

# newData = [2,3,5,8,1]
# ll = None
# ll = {'data': 2, 'next': {'data': 5, 'next': {'data': 3, 'next': {'data': 8, 'next': {'data': 1, 'next':None}}}}}
# ll = delEvenData(ll)
# print(ll)
# for i in range(0, len(newData), 1):
    #print(i)
    # ll = addCircuralHead(ll, newData[i])
# print(ll)
# total = dotProduct(ll)
# print(total)
