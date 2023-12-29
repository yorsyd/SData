# Kisi-Kisi UTS
# Materi pertemuan 5, 6  7

# Dolby : mencetak (buat fungsi)
# Queue : menambah antrian (eksekusi)
# Stack : hitung data/elemen dalam stack (buat fungsi)

# Kalo perintahnya eksekusi per baris maka tulis per baris, sedangkan kalo disuruh membuat fungsi maka buat saja fungsinya

# Kerjain pelan-pelan dan perhatikan soalnya... santai aja

def insertDoublyHead(ll, data):
    newNode = {'prev': None, 'data': data, 'next': None}
    if ll is None:
        return newNode
    
    newNode['next'] = ll
    ll['prev'] = newNode

    return newNode

#Mencetak Dolby Linked List
def cetakBack(ll):
    templl = ll

    while templl['next'] is not None:
        templl = templl['next']

    while templl is not None:
        print(templl['data'], end='')
        templl = templl['prev']

def cetakDepan(ll):
    while ll:
        print(ll['data'], end="")
        ll = ll['next']

#menambah data queue
def enqueue(queue, queueMaxCapacity, newData):
    frontIndex = -1
    rearIndex = 0

    if queue[frontIndex] is None:
        queue[frontIndex] = newData
        return queue
    
    if queue[rearIndex] is not None:
        print("Full")
        return queue
    
    for i in range(queueMaxCapacity-1, -1, -1):
        if queue[i] == None:
            queue[i] = newData
            return queue

#Hitung data/elemen dalam stack
def countElementStack(maxCapacity, queue):
    counter = 0
    for i in range(0, maxCapacity, 1):
        if queue[i] is not None:
            counter = counter + 1
    return counter

data = [None,None,3,4,5]
data =  enqueue(data,5, 1)
print(data)
# ll = None
# ll = insertDoublyHead(ll, 1)
# ll = insertDoublyHead(ll, 4)
# ll = insertDoublyHead(ll, 9)
# ll = insertDoublyHead(ll, 5)
isi = countElementStack(5, data)
print(isi)
# cetakBack(ll)
# print()
# cetakDepan(ll)