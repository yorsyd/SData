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

def preOrderTransversal(tree, level):
    if tree == None:
        return None
    
    print('Level', level, '=', tree['data'])
    level = level + 1
    preOrderTransversal(tree['L'], level)
    preOrderTransversal(tree['R'], level)

#alternatif
def preOrderTransversalAlter(tree, level):
    if tree == None:
        return None
    
    print('Level', level, '=', tree['data'])
    preOrderTransversal(tree['L'], level+1)
    preOrderTransversal(tree['R'], level+1)

def inOrderTransversal(tree, level):
    level = level + 1
    if tree == None:
        return None
        
    inOrderTransversal(tree['L'], level)
    print('Level', level-1, '=', tree['data'])
    inOrderTransversal(tree['R'], level)

#alternatif
def inOrderTransversalAlter(tree, level):
    if tree == None:
        return None
        
    inOrderTransversal(tree['L'], level+1)
    print('Level', level-1, '=', tree['data'])
    inOrderTransversal(tree['R'], level+1)

def postOrderTransversal(tree, level):
    level = level + 1
    if tree == None:
        return None
    
    postOrderTransversal(tree['L'], level)
    postOrderTransversal(tree['R'], level)
    print('Level', level, '=', tree['data'])

#alternatif
def postOrderTransversalAlter(tree, level):
    if tree == None:
        return None
    
    postOrderTransversal(tree['L'], level+1)
    postOrderTransversal(tree['R'], level+1)
    print('Level', level, '=', tree['data'])

tree = None
#print(tree)
tree = createTree(tree, 25)
tree = createTree(tree, 21)
tree = createTree(tree, 19)
tree = createTree(tree, 26)
tree = createTree(tree, 20)

print("Pre Order")
preOrderTransversal(tree, 0)
print()

print("In Order")
inOrderTransversal(tree, 0)
print()

print("Post Order")
postOrderTransversal(tree, 0)