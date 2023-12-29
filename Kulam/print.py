def printLL(LL):
    if LL:
        while LL:
            print(LL['data'],end=' > ')
            LL = LL['next']
        print()
    else:
        print('none')

def deleteN(LL, target):
    temp = LL
    while temp['next']:
        if temp['next']['data'] == target:
            temp['next'] = temp['next']['next']
            return LL
        temp = temp['next']

target = "dahlan"
LL = {'data': 'universitas', 'next': {'data': 'ahmad', 'next': {'data': 'dahlan', 'next': {'data': 'ptm', 'next': None}}}}

printLL(LL)
huh = deleteN(LL, target)
print(huh)