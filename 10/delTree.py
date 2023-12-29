def createTree(tree, newData):
    newNode = {'L': None, 'data': newData, 'R': None}

    if tree == None:
        tree = newNode
    else:
        if newData < tree['data']:
            if tree['L'] == None:
                tree['L'] = newNode
            else:
                createTree(tree['L'], newData)
        if newData >= tree['data']:
            if tree['R'] == None:
                tree['R'] = newNode
            else:
                createTree(tree['R'], newData)
    return tree

def delNode(tree, key):
    if tree == None:
        return None
    
    if tree['data'] == key:
        #jika simpulnya sendiri
        if tree['L'] == None and tree['R'] == None:
            return None
        #jika simpulnya punya anak satu sebelah kiri
        elif tree['L'] != None and tree['R'] == None:
            return tree['L']
        #Jika simpulnya punya anak satu sebelah kanan
        elif tree['R'] != None and tree['L'] == None:
            return tree['R']
        else:
            successor = findMinVal(tree['RS'])
            tree['data'] = successor['data']
            tree['R'] = delNode(tree['R'], successor['data'])
    elif key < tree['data']:
        tree['L'] = delNode(tree['L'], key)
    else:
        tree['R'] = delNode(tree['R'], key)

    return tree

def findMinVal(tree):
    if tree == None:
        return None
    
    current = tree
    while(current['L'] != None):
        current = current['L']

    return current

def preOrderTransversal(tree):
    if tree == None:
        return None
    
    print(tree['data'], " - ", end="")
    preOrderTransversal(tree['L'])
    preOrderTransversal(tree['R'])

def inOrderTransversal(tree):
    level = level + 1
    if tree == None:
        return None
        
    inOrderTransversal(tree['L'])
    print(tree['data'], " - ", end="")
    inOrderTransversal(tree['R'])

def postOrderTransversal(tree):
    level = level + 1
    if tree == None:
        return None
    
    postOrderTransversal(tree['L'])
    postOrderTransversal(tree['R'])
    print(tree['data'], " - ", end="")


tree = None
tree = createTree(tree, 50)
tree = createTree(tree, 80)
tree = createTree(tree, 45)
tree = createTree(tree, 25)
tree = createTree(tree, 47)
tree = createTree(tree, 72)
tree = createTree(tree, 82)
tree = createTree(tree, 10)
tree = createTree(tree, 90)

print("Before")
preOrderTransversal(tree)
tree = delNode(tree, 80)
tree = delNode(tree, 50)
print()
print("After")
preOrderTransversal(tree)

arr = [1,2,3]
arr.insert(1,4)