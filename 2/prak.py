def createNode(data):
    return{'data':data, 'pointer':None}

def addAtHead(linkedList, data):
    newNode = createNode(data)
    newNode['pointer'] = linkedList
    return newNode

def printLinkedList(linkedList):
    while linkedList:
        print(linkedList['data'])
        linkedList = linkedList['pointer']

def searchNode(linkedList,keySearch):
    while linkedList:
        if linkedList['data'] == keySearch:
            return "Ketemu"
        linkedList = linkedList['pointer']
    return "Tidak Ketemu"

def nodeCount(linkedList):
    counter = 0
    while linkedList:
        linkedList = linkedList['pointer']
        counter += 1
    return counter
        
linkedList = None
data = ["Bambang", "Saputra", "Ardi", "Rizqi","Moch", 2200018232]
for i in data:
    linkedList = addAtHead(linkedList, i)

printLinkedList(linkedList)
print(searchNode(linkedList,"Rizqi"))
print(searchNode(linkedList,2300018232))
jumlah = nodeCount(linkedList) 
print("Jumlah node(simpul) : ", jumlah)