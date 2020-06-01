import numpy as np
import math

csvFile = "iris.data"
myCollection = np.loadtxt(csvFile, delimiter=',', usecols=range(4))
myCollectionk = np.genfromtxt(csvFile, delimiter=',', dtype=None)

def precision(result, tipo):
    objRP = 0
    i = 1
    for obj in result:
        objResLine = str(obj[0]) + ',' + str(obj[1]) + "," + str(obj[2]) + "," + str(obj[3])
        with open(csvFile, "r") as fdata:
            for line in fdata:
                if objResLine in line:
                    csvLine = line.strip()
                    tipoF = csvLine.split(',')[4]
                    if tipo == tipoF:
                        #print(csvLine)
                        objRP += 1
                        break
    totalRecuperados = len(result)
    print("Total:", totalRecuperados)
    print("Objetos Relevantes Recuperados:", objRP)
    print(objRP, "/", totalRecuperados)
    return objRP/totalRecuperados

def ED(x, y):
    return(math.sqrt(sum((x - y)**2)))

def rangeSearch(Q, r, numObj):
    i = 1
    result = []
    for objectIris in myCollection:
        if i == numObj:     # el objeto consultado es omitido de la colección
            i += 1
            continue
        dist = ED(Q, objectIris)
        if dist < r:
            result.append(objectIris)
        i += 1
    return result

def knnSearch(Q, k, numObj):
    print("--- knnSearch ---")
    result = []
    dicRes = {}
    i = 0
    for objectIris in myCollection:
        if i == numObj:     # el objeto consultado es omitido de la colección
            i += 1
            continue
        dist = ED(Q, objectIris)
        dist = dist
        result.append(dist)
        dicRes[dist] = myCollectionk[i]
        i += 1
    result.sort()
    for i in range(k):
        print("Distancia: ", result[i])
        print("Objeto detalles: ", dicRes[result[i]])

## Q15 ##
print(" --- Q 15 ----")
result = rangeSearch(myCollection[15], 2.5, 15)
prec = precision(result, "Iris-setosa")
print("Precision: ", prec)

result = rangeSearch(myCollection[15], 4, 15)
prec = precision(result, "Iris-setosa")
print("Precision: ", prec)

result = rangeSearch(myCollection[15], 5, 15)
prec = precision(result, "Iris-setosa")
print("Precision: ", prec)

## Q82 ##
print(" --- Q 82 ----")
result = rangeSearch(myCollection[82], 2.5, 15)
prec = precision(result, "Iris-versicolor")
print("Precision: ", prec)

result = rangeSearch(myCollection[82], 4, 15)
prec = precision(result, "Iris-versicolor")
print("Precision: ", prec)

result = rangeSearch(myCollection[82], 5, 15)
prec = precision(result, "Iris-versicolor")
print("Precision: ", prec)

## Q121 ##
print(" --- Q 121 ----")
result = rangeSearch(myCollection[121], 2.5, 15)
prec = precision(result, "Iris-virginica")
print("Precision: ", prec)

result = rangeSearch(myCollection[121], 4, 15)
prec = precision(result, "Iris-virginica")
print("Precision: ", prec)

result = rangeSearch(myCollection[121], 5, 15)
prec = precision(result, "Iris-virginica")
print("Precision: ", prec)


## KSearch ##
knnSearch(myCollection[15], 2, 15)
knnSearch(myCollection[15], 4, 15)
knnSearch(myCollection[15], 8, 15)
knnSearch(myCollection[15], 16, 15)
knnSearch(myCollection[15], 32, 15)