def insertDoublyHead(ll, data):
    newNode = {'prev': None, 'data': data, 'next': None}
    if ll is None:
        return newNode
    
    newNode['next'] = ll
    ll['prev'] = newNode

    return newNode

def insertDoublyKey(ll, data, key):
    newNode = {'prev': None, 'data': data, 'next': None}
    if ll is None:
        return newNode
    
    temp = ll

    while temp['next']:
        if temp['data'] == key:
            break
        temp = temp['next']
    newNode['next'] = temp['next']
    if temp['next']: 
        temp['next']['prev'] = newNode
    newNode['prev'] = temp
    temp['next'] = newNode
    return ll

def cetakBack(ll):
    templl = ll
    if templl is None:
        return "Linkedlist kosong"
    
    while templl['next']:
        templl = templl['next']

    while templl:
        print(templl['data'], end='')
        templl = templl['prev']

def cetakDepan(ll):
    if ll is None:
        return "Linkedlist kosong"
    
    while ll:
        print(ll['data'], end="")
        ll = ll['next']

ll = None
ll = insertDoublyHead(ll, 1)
ll = insertDoublyHead(ll, 4)
print(ll)
ll = insertDoublyKey(ll, 6, 1)
ll = insertDoublyKey(ll, 8, 4)
print(ll)
cetakBack(ll)
print("")
cetakDepan(ll)