import numpy as np
import math

csvFile = "iris.data"
myCollection = np.loadtxt(csvFile, delimiter=',', usecols=range(4))

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