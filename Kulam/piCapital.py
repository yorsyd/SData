def bikinNode(data):
    return{'data' : data, 'next' : None}

def insertKepala(ll, data):
    newNode = bikinNode(data)
    newNode['next'] = ll
    return newNode

def kali(ll):
    hasil = 1
    while ll:
        hasil = hasil * ll['data']
        ll = ll['next']
    return hasil

data = [2,3,4]
ll = None
for i in data:
    ll = insertKepala(ll, i)

#hasil = kali(ll)
print(ll)
hasil = kali(ll)
print(hasil)