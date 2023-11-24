import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn import linear_model
import pandas #Permite leer archivos csv y devolver un objeto DataFrame

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

media = numpy.mean(speed) #Media
mediana = numpy.median(speed) #Mediana (el valor del medio,si hay 2 se divide)
moda = stats.mode(speed) #Moda (El valor que mas veces aparece)

des_est = numpy.std(speed) #Desviación estándar (Que tan alejado están los valores del promedio)
varianza = numpy.var(speed) #Varianza (Raíz cuadrada de varianza = desviacion tipica)

x = numpy.percentile(ages, 75) #La edad que tiene el 75% de los mas jovenes


x = numpy.random.uniform(0.0, 5.0, 100000) #Crea una matriz que contenga 250 flotantes aleatorios entre 0 y 5:

x = numpy.random.normal(5.0, 1.0, 100000) #Distribucion de datos normal tipica (Valor medio es 5 y desviacion estandar es 1)

# plt.hist(x, 100) #Muestra un histograma de x de 100 barras
# plt.show()

#Grafico de dispersion
x = numpy.random.normal(5.0, 1.0, 1000) #Generar valores aleatorios
y = numpy.random.normal(10.0, 2.0, 1000) #Generar valores aleatorios

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] #Edad coches
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #Velocidad

# plt.scatter(x, y) #Dibuja el diagrama de dispersión original
# plt.show()


#Regresion lineal
slope, intercept, r, p, std_err = stats.linregress(x, y) #Pendiente, intercepcion, coeficiente de correlacion, vapor "p", error estandar

def myfunc(x):
  return slope * x + intercept

# mymodel = list(map(myfunc, x)) #Ejecuta cada valor de la matriz x a través de la función. Esto dará como resultado una nueva matriz con nuevos valores para el eje y

# print(r) #Relacion
# plt.scatter(x, y)
# plt.plot(x, mymodel) #Dibuja la línea de regresión lineal
# plt.show()

# speed = myfunc(10) #Predecir velocidad de un coche de 10 años
# print(speed)

#Regresión polinomial
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] #Hora
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100] #Velocidad coche

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3)) #Modelo polinomial

# myline = numpy.linspace(1, 22, 100) #La línea comienza en 1 y termina en 22

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# print(r2_score(y, mymodel(x))) #varía de 0 a 1, donde 0 significa que no hay relación y 1 significa 100% relacionado.
# speed = mymodel(17) #Predecir un resultado
# print(speed)

#Regresión múltiple
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#Predice la emision de CO2  de un coche donde el peso es 2.3k kg y volumen de 1300 cm3
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)