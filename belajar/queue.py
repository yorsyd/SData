def queueIsFull(rearIndex, queue):
    return queue[rearIndex] != None

def queueIsEmpty(frontIndex, queue):
    return queue[frontIndex] == None

def enqueue(queue, queueMaxCapacity, newData):
    frontIndex = -1
    rearIndex = 0

    if queueIsEmpty(frontIndex, queue):
        queue[frontIndex] = newData
        return queue
    
    if queueIsFull(rearIndex, queue):
        print("Full")
        return queue
    
    for i in range(queueMaxCapacity-1, -1, -1):
        if queue[i] == None:
            queue[i] = newData
            return queue
        
queueMaxCapacity = 4
queue = [None] * queueMaxCapacity

queue = enqueue(queue, queueMaxCapacity, 5)
print(queue)
queue = enqueue(queue, queueMaxCapacity, 2)
print(queue)
queue = enqueue(queue, queueMaxCapacity, 7)
print(queue)
queue = enqueue(queue, queueMaxCapacity, 6)
print(queue)

newData = 13
queue = enqueue(queue, queueMaxCapacity, newData)
# if queue[0]:
#     print("Full")

