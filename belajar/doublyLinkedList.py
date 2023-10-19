#create new node doubly 
def createNewNode(data):
    return {'prev': None, 'data': data, 'next': None}

#Insert new node at head doubly linked list
def insertDoublyHead(ll, data):
    newNode = createNewNode(data)
    if ll is None:
        return newNode
    
    newNode['next'] = ll
    ll['prev'] = newNode

    return newNode

#Insert new node at tail doubly linked list
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

#print doubly linked list from backward
def printBack(ll):
    templl = ll

    while templl['next']:
        templl = templl['next']

    while templl:
        print(templl['data'], end='')
        templl = templl['prev']

#print doubly linked list from forward
def printFront(ll):
    while ll:
        print(ll['data'], end="")
        ll = ll['next']

#data
ll = None
ll = insertDoublyHead(ll, 2)
ll = insertDoublyTail(ll, 1)
ll = insertDoublyTail(ll, 4)
print(ll)
printkBack(ll)
printFront(ll)
