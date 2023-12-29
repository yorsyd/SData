def pushStack(stack, maxCapacity, newData):
    bottomIndex = -1
    topIndex = 0

    #jika kosong melompong
    if stack[bottomIndex] == None:
        stack[bottomIndex] = newData
        return stack
    
    #ngecek penuh apa ngaa
    if stack[topIndex] != None:
            return stack
    
    for i in range(maxCapacity-1, -1, -1):
        if stack[i] == None:
            stack[i] = newData
            return stack

def popStack(stack, maxCapacity):
     bottom = -1
     topIndex = 0

     for i in range(0, maxCapacity, 1):
          if stack[bottom] == None:
               print("Kosong")
               break
          
          if stack[i] != None:
               stack[i] = None
               return stack
