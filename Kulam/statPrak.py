import statistics
import numpy

def stdDeviasi():
    array = input().split(",")
    for i in range(len(array)): 
        array[i] = int(array[i])

    jumlah = 0
    for i in range(len(array)):
        jumlah += array[i]
    rata = jumlah / len(array)

    sigma = 0
    for i in range(len(array)):
        hitung = (array[i]-rata)**2
        sigma += hitung
    pembagian = sigma / len(array)

    standarDeviasi = pembagian ** 0.5
    print(standarDeviasi)

def stdDevAndVariance():
    # Creating a simple data-set
    # Adjust the input data according to case 1 and 2
    data = [70, 88, 87, 98, 69, 90, 60, 70, 78,88]

    # Printing standard deviation
    print("Standard Deviation of the data is %s" %(statistics.stdev(data)))

    # Variance is approximately the squared result of what stdev is
    print("Variance of the data is %s" %(statistics.variance(data)))
    
def mean():
    data = [1, 2, 3, 4, 5]

    jumlah = 0
    for i in range(len(data)):
        jumlah += data[i]
    rata = jumlah / len(data)
    print("Mean dari data tersebut adalah ", rata)
    #print("Mean dari data tersebut adalah", statistics.mean(data))

def modus():  
    data =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
    print("Modus data % s" % (statistics.mode(data)))

def kuartil():
    data = [20, 2, 7, 1, 34]
    
    print("data : ", data) 
    print("Q2 : ", numpy.quantile(data, .50))
    print("Q1 : ", numpy.quantile(data, .25))
    print("Q3 : ", numpy.quantile(data, .75))

stdDeviasi()
print()
stdDevAndVariance()
print()
mean()
print()
modus()
print()
kuartil()