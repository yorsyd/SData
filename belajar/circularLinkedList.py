def addCircuralTail(ll, newData):
  newNode = {'data': newData, 'next': None}

  if not ll:
    newNode['next'] = newNode
    return newNode
  else:
    tempLL = ll
    while tempLL['next'] != ll:
      tempLL = tempLL['next']
    tempLL['next'] = newNode
    newNode['next'] = ll

    return ll

def addCircuralHead(ll, newData):
  newNode = {'data': newData, 'next': None}

  if not ll:
    newNode['next'] = newNode
    return newNode
  else:
    tempLL = ll
    while tempLL['next'] != ll:
      tempLL = tempLL['next']
    newNode['next'] = ll
    tempLL['next'] = newNode

    return newNode

def addCircuralMid(ll, newData, key):
    newNode = {'data': newData, 'next': None}
    tempLL = ll

    while tempLL and tempLL['next']:
        if tempLL['next']['data'] == key:
            newNode['next'] = tempLL['next']
            tempLL['next'] = newNode
            return ll
        tempLL = tempLL['next']

def delCircularMid(ll, key):
    tempLL = ll
    while tempLL['next']:
        if tempLL['next']['data'] == key:
            tempLL['next'] = tempLL['next']['next']
            return ll
        tempLL = tempLL['next']

def delCircularTail(ll):
    tempLL = ll

    while tempLL['next']['next'] != ll:
       tempLL = tempLL['next']
    tempLL['next'] = ll
    return ll

def delCircularHead(ll):
    tempLL = ll
    while tempLL['next'] != ll:
       tempLL = tempLL['next']
    tempLL['next'] = ll['next']
    return tempLL

def printCircularFromFront(ll):
    if not ll:
        print("Linked list is empty")
        return

    tempLL = ll
    while True:
        print(tempLL['data'], end=" ")
        tempLL = tempLL['next']
        if tempLL == ll:
            break

def printCircularFromBack(ll):
    if not ll:
        print("Linked list is empty")
        return

    tempLL = ll
    while tempLL['next'] != ll:
        tempLL = tempLL['next']

    while True:
        print(tempLL['data'], end=" ")
        if tempLL == ll:
            break
        tempLL2 = ll
        while tempLL2['next'] != tempLL:
            tempLL2 = tempLL2['next']
        tempLL = tempLL2

ll = None
ll = addCircuralTail(ll,1)
print(ll)
ll = addCircuralTail(ll,6)
print(ll)
ll = addCircuralHead(ll,3)
print(ll)
ll = addCircuralHead(ll,4)
print(ll)
ll = addCircuralHead(ll,2)
print(ll)
ll = addCircuralMid(ll, 8, 1)
print(ll)
ll = delCircularMid(ll, 8)
print(ll)
ll = delCircularTail(ll)
print(ll)
ll = delCircularHead(ll)
print(ll)
printCircularFromFront(ll)
print(' ')
printCircularFromBack(ll)
