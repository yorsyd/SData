#Fungsi push data pada queue
def enqueue(queue, maxCapacity, newData):
    #Jika queue penuh
    if queue[0] is not None:
        print ("Queue Penuh")
        return queue
    for i in range(maxCapacity - 1, -1, -1):
        if queue[i] is None:
            queue[i] = newData
            return queue

#Fungsi pop data pada queue
def dequeue(queue, maxCapacity):
    tempQueue = queue
    queue = [None] * maxCapacity

    for i in range (maxCapacity-2, -1, -1):
        if tempQueue[-1] is None:
            print("Queue kosong")
            return queue
        queue[i+1] = tempQueue[i]

    print("Data Terhapus")
    return queue

#check
def check(maxCapacity, capacity, queue):
    isi = 0
    for i in range(maxCapacity - 1, -1, -1):
        if queue[i] is None:
            isi = isi + 1
    if capacity > isi:
        print ("Tidak Bisa Menambah Data Sebanyak itu")
        return False
    return True

def checkAvailable(queue):
    count = 0
    for data in queue:
        if data is None:
            count = count + 1
    return count

maxCapacity = 4
queue = [None] * maxCapacity

while(True):
    print('======================')
    print("MENU")
    print('======================')
    print("1. enqueue")
    print("2. dequeue")
    print("3. cetak")
    print("0. exit")
    pilih = int(input("Pilih: "))
    print('======================')
    if pilih == 1:
        capacity = int(input("Banyak data yang ingin diisi: "))
        if capacity > checkAvailable(queue):
            print("Tidak ada slot")
        else:
            for i in range(capacity):
                newData = input("Data Baru : ")
                queue = enqueue(queue, maxCapacity, newData)
    if (pilih == 2):
        queue = dequeue(queue, maxCapacity)
    if (pilih == 3):
        print(queue)
    if (pilih == 0):
        break
