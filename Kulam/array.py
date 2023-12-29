def addDataArray(arr, newData):
    # Membuat array baru dengan ukuran yang lebih besar
    newArr = [None] * (len(arr) + 1)

    # Menyalin data dari array lama ke array baru
    for i in range(len(arr)):
        newArr[i] = arr[i]

    # Menambahkan data baru ke akhir array
    newArr[-1] = newData

    return newArr

def addMidArray(arr, newData, postion):
    # Membuat array baru dengan ukuran yang lebih besar
    newArr = [None] * (len(arr) + 1)

    # Menyalin data dari array lama ke array baru
    for i in range(len(arr)):
        newArr[i] = arr[i]

    # Mengisi kekosongan array terakhir
    for i in range(len(arr), postion, -1):
        newArr[i] = arr[i-1]

    # Menambahkan data baru ke pisisi tertentu
    newArr[postion] = newData

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
arr = addMidArray(arr, 8, 2)
print(arr)
arr = addDataArray(arr, 5)
print(arr)
delDataArr(arr, 5, 2)
print(arr)
