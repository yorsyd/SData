def createNewNode(data):
    return {'prev': None, 'data': data, 'next': None}

def insertDoublyHead(ll, data):
    newNode = createNewNode(data)
    if ll is None:
        return newNode
    
    newNode['next'] = ll
    ll['prev'] = newNode

    return newNode

def insertDoublyTail(ll, data):
    newNode = createNewNode(data)
    if ll is None:
        return newNode
    
    temp = ll

    while temp['next']:
        temp = temp['next']

    temp['next'] = newNode
    newNode['prev'] = temp

    return ll

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

ll = None
ll = insertDoublyHead(ll, 1)
ll = insertDoublyHead(ll, 4)
print(ll)
cetakBack(ll)
print("")
cetakDepan(ll)