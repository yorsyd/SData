def createTree(tree, newData):
    newNode = {'left': None, 'data': newData, 'right': None}

    if tree == None:
        tree = newNode
    else:
        if newData < tree['data']:
            if tree['left'] == None:
                tree['left'] = newNode
            else:
                createTree(tree['left'], newData)
        if newData >= tree['data']:
            if tree['right'] == None:
                tree['right'] = newNode
            else:
                createTree(tree['right'], newData)
    return tree

def preTransversal(tree):
    if tree == None:
        return None
    print(tree['data'], end=' ')
    preTransversal(tree['left'])
    preTransversal(tree['right'])

def searchData(tree, key, level):
    if tree == None:
        return None
    if tree['data'] is key:
        print ("Data", tree['data'], "ditemukan pada level", level)
        exit 
    else:
        level = level + 1
        searchData(tree['left'], key, level)
        searchData(tree['right'], key, level)

# def inOrderTransversal(tree):
#     if tree == None:
#         return None
#     inOrderTransversal(tree['left'])
#     print(tree['data'], end=' ')
#     inOrderTransversal(tree['right'])

# def postOrderTransversal(tree):
#     if tree == None:
#         return None
#     postOrderTransversal(tree['left'])
#     postOrderTransversal(tree['right'])
#     print(tree['data'], end=' ')

def binarySearchTree(tree, searchKey, level):
    if tree == None:
        print(searchKey, 'tidak ditemukan')
        return
    if tree['data'] == searchKey:
        print(searchKey,'ditemukan', 'pada level', level)
        return
    level = level + 1
    if searchKey < tree['data']:
        binarySearchTree(tree['left'], searchKey, level)
    if searchKey > tree['data']:
        binarySearchTree(tree['right'], searchKey, level)

searchKey = 16


tree = None
tree = createTree(tree, 19)
tree = createTree(tree, 17)
tree = createTree(tree, 16)
tree = createTree(tree, 14)
# tree = createTree(tree, 18)
# tree = createTree(tree, 20)
# print(tree)

#searchData(tree, 16, 0)
binarySearchTree(tree, searchKey, 0)
#print(hasil)