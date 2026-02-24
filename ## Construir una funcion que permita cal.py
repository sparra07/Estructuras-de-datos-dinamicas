## Construir una funcion que permita calcular el factorial de un numero  (iterativa)
def factorialIterativo ( n : int):
  resultado = 1
  for i in range(1, n+1):
    resultado = resultado * i
  return resultado


def factorial ( n : int):
  ## Caso base o caso de parada
  if(n == 0):
    return 1
  ## Caso recursivo
  return n * factorial (n-1)

def factorial2 ( n : int, acumulador : int = 1):
  if n == 0:
    return acumulador
  else:
    return factorial2(n-1, n * acumulador)
  
## Contar la cantidad de caracteres de un string pero usando recursion. No se puede usar la fn len()

def calcularLongitud( cadena : str, contador : int = 0):
  if cadena == '':
    return contador
  else:
    return calcularLongitud( cadena[1:], contador + 1)

print(calcularLongitud("hola"))

def calcularLongitud2(cadena : str):
  if(cadena == "" ):
    return 0
  else:
    return 1 + calcularLongitud2(cadena[1:])

print(calcularLongitud2("Hola"))

## CL("hola", 0) -> No entra el IF, llama a CL("ola", 1)
## CL("ola", 1) -> No entra al IF, llama CL("la", 2)
## CL("la", 2) -> No entra al IF, llamar CL("a",3)
## CL("a", 3) -> No entra al IF, llamar CL("", 4)
## CL("", 4) -> Si entra al IF y retorna 4

## Crear una funcion recursiva que reciba una lista y un numero y determine si ese numero se encuentra o no en la lista

def numeroEstaEnLista(lista : list , n : int):
  if len(lista) == 0:
    return False
  elif(lista[0] == n):
    return True
  else:
    return numeroEstaEnLista(lista[1:], n)
print(numeroEstaEnLista([1,2,3,4,5,6], 8))
print(numeroEstaEnLista([1,2,3,4,5,6], 5))

## Dada una Lista L y un Elemento E, determinar la
## posicion de la primera ocurrencia dentro de la lista. Si no está devolver -1

def calcularPosicionEnLista(lista: list, element: int, posicion : int = 0) -> int:
  if(lista == []):
    return -1
  elif(lista[0] == element):
    return posicion
  else:
    return calcularPosicionEnLista(lista[1:], element, posicion + 1)

print(calcularPosicionEnLista([1,2,3,4,5,6], 8))
print(calcularPosicionEnLista([1,2,3,4,5,6], 5))

def calcularPosicionEnLista2(lista: list, element: int, posicion : int = 0) -> int:
  if(posicion == len(lista) - 1):
    return -1
  elif(lista[posicion] == element):
    return posicion
  else:
    return calcularPosicionEnLista2(lista, element, posicion + 1)

print(calcularPosicionEnLista2([1,2,3,4,5,6], 8))
print(calcularPosicionEnLista2([1,2,3,4,5,6], 5))

## Dada una Lista L y en Elemento E,
## determinar todas las posiciones en las que se encuentra el elemento. Si no está retornar [-1]

def calcularPosicionesEnLista(lista: list, elemento: int, posicion: int = 0, ocurrencias : list = []) -> list:
  if(lista[posicion] == elemento):
    ocurrencias.append(posicion)
  if (posicion == len(lista)  - 1 ):
    if(ocurrencias == []):
      return [-1]
    else:
      return ocurrencias
  else:
    return calcularPosicionesEnLista(lista, elemento, posicion + 1, ocurrencias)

print(calcularPosicionesEnLista([5,2,5,5,5,6], 5, 0, []))
print(calcularPosicionesEnLista([1,2,3,4,5,6], 8, 0, []))
print(calcularPosicionesEnLista([1,2,3,4,5,6], 4, 0 , []))

def calcularPosicionesEnLista2(lista: list, elemento: int, posicion: int = 0, ocurrencias: list = []) -> list:
  if lista == []:
    if(ocurrencias == []):
      return [-1]
    else:
      return ocurrencias
  elif lista[0] == elemento:
    ocurrencias.append(posicion)
  return calcularPosicionesEnLista2(lista[1:], elemento, posicion + 1, ocurrencias)

print(calcularPosicionesEnLista2([5,2,5,5,5,6], 5, 0, []))
print(calcularPosicionesEnLista2([1,2,3,4,5,6], 8, 0, []))
print(calcularPosicionesEnLista2([1,2,3,4,5,6], 4, 0 , []))

## De una lista de numeros enteros determinar cuantos numeros pares hay en ella

def contarParesEnLista(lista: list, contador: int = 0):
  if lista == []:
    return contador
  elif lista[0] % 2 == 0:
    contador = contador + 1
  return contarParesEnLista(lista[1:], contador)

print(contarParesEnLista([1,2,3,4,5,6,7,8]))

## Contar la cantidad de digitos de un numero entero, sin convertirlo a String


def calcularLongitudNumero( numero : int, contador : int = 0):
  if numero < 10:
    return contador + 1
  else:
    return calcularLongitudNumero( numero // 10, contador + 1)

print(calcularLongitudNumero(287631))

## Invertir una cadena de texto EJ: Hola -> aloH

def invertirCadena(cadena : str) -> str:
  if len(cadena) <= 1:
    return cadena
  else:
    return invertirCadena(cadena[1:]) + cadena[0] ## Recursion No de Cola
## No de cola: Significa que ademas de la recursion hay otras operaciones pedneintes

print(invertirCadena("Hola"))
## Primer llamado cadena = Hola, no entra al if, ejecuta el else
## Segundo llamado cadena ola + H, no entra al if, ejecuta el else -> aloH
## Tercer llamado cadena la + o, no entra el if entra al else -> alo
## Cuearto llamado cadena = a + l, entra el if y retorna a -> al


def invertirCadena2(cadena: str, acumulador :str = "") -> str:
  if(len(cadena) == 0):
    return acumulador
  else:
    return invertirCadena2(cadena[1:] , cadena[0] + acumulador) ## Recursion de cola
## De Cola: Cuando el llmado recursivo es la unica operacion pendiente

print(invertirCadena2("Hola"))


def funcion_a():
    print("Entrando en funcion_a")
    funcion_b()
    print("Saliendo de funcion_a")

def funcion_b():
    print("Entrando en funcion_b")
    funcion_c()
    print("Saliendo de funcion_b")

def funcion_c():
    print("Entrando en funcion_c")
    print("Saliendo de funcion_c")

# Llamamos a la primera función
funcion_a()

import sys

a = [1, 2, 3]
print(a)
b = a ## b = [1,2,3]
print(b)
c = a ## c = [1,2,3]
print(c)

#b = [1,2,3]
#c =[1,2,3]

c.append(4) ## c = [1,2,3,4]
print(c)

print(a)
print(b)

## REFERECNIAS EN MEMORIA
print(sys.getrefcount(a))  # ¿Cuántas referencias existen a la lista en este punto?

del a  # Eliminamos una referencia
print(sys.getrefcount(b))  # ¿Cuántas referencias quedan?

#c = None  # Otra referencia eliminada
#print("¿La lista sigue existiendo en memoria?")

def count_down(n):
    if n == 0:
        print("Fin de la recursión")
        return
    print(f"Llamada con n={n}")
    count_down(n - 1)
    print(f"Retornando n={n}")

count_down(5)

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

a = 5
b = a ## b = 5

b = b + 2 ## b = 7
print(a)
print(b)

## Cuanto vale a
## Cuanto vale b


p1 = Persona("Juan", 20)
p2 = p1
p2.edad = 23

print(p1.nombre)
print(p1.edad)
print(p2.nombre)
print(p2.edad)


palabra1 = "Como estas"
palabra2 = palabra1
palabra2 = palabra2 + "?"

print(palabra1)
print(palabra2)

## Calcular el n-esimo numero Fibonacci, consierando que la sucesion Fibonacci empieza con 0 y 1
## y los siguientes terminos se calculan como la suma de los terminos anteriores
## 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
## 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

def calcularFibonacci(n : int) -> int:
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return calcularFibonacci(n-1) + calcularFibonacci(n-2)

print(calcularFibonacci(1))
print(calcularFibonacci(2))
print(calcularFibonacci(3))
print(calcularFibonacci(4))
print(calcularFibonacci(5))
print(calcularFibonacci(6))

## Usando solo recursion de cola

def calcularFibonacciCola(n : int, a : int = 0, b : int = 1):
  if  n == 1 :
    return a
  elif n == 2:
    return b
  else:
    return calcularFibonacciCola(n -1, b, a + b)

print(calcularFibonacciCola(1))
print(calcularFibonacciCola(2))
print(calcularFibonacciCola(3))
print(calcularFibonacciCola(4))
print(calcularFibonacciCola(5))
print(calcularFibonacciCola(6))

## dado un array de numeros calcular la suma de sus elementos usando recursion
## Ej :[ 1,4, 9, 2] -> 16

def calcularSumaArreglo(arreglo: list, acumulador : int = 0):
  if arreglo == []:
    return acumulador
  else:
    return calcularSumaArreglo(arreglo[1:], acumulador + arreglo[0])

print(calcularSumaArreglo([1,4,9,2]))

## Calcular el resultado de n (diferenete de cero) elevado a la m utilizando recursion sin utilizar el operador ** ni pow

## Pista: La potenciacion se puede expresar como una cantidad definida de multiplicaciones
## cola y no de cola

def calcularPotencia(n: int, m: int) -> int:
  if m == 0:
    return 1
  else:
    return n * calcularPotencia(n, m - 1)
  ## calcularPotencia(3,4) = 81
  ## 3* calculcarPotencia(3, 3) = 81
  ## 3 * cauclularPotencia(3, 2) = 27
  ## 3 * calcularPotencia(3, 1) = 9
  ## 3 * calcularPotencia(3, 0) = 3
  ## 1
print(calcularPotencia(3,4))

def calcularPotenciaCola(n : int, m: int, acumulador: int = 1) -> int:
  if m == 0:
    return acumulador
  else:
    return calcularPotenciaCola(n, m -1, acumulador * n)
print(calcularPotenciaCola(3,4))

## calcularPotenciaCola(3,4,1) =
##  calcularPotenciaCola (3, 3, 3)
##    calcularPotenciaCola( 3, 2, 9)
##      calcularPotenciaCola(3, 1, 27)
###.       calcularPotenciaCola(3, 0, 81)
####.         return 81

def encontrarMaximo(arreglo : list)->int:
  if len(arreglo) == 1:
    return arreglo[0]

  maximoResto = encontrarMaximo(arreglo[1:])

  if(arreglo[0] > maximoResto):
    return arreglo[0]
  else:
    return maximoResto

print(encontrarMaximo([123, 200, 320, 45]))

def contar_elementos(lista: list)-> int :
  if lista == []:
    return 0
  if isinstance(lista[0], list): ## Validar si es o no es una lista
    return contar_elementos(lista[0]) + contar_elementos(lista[1:])
  else:
    return 1 + contar_elementos(lista[1:])

print(contar_elementos([1, [2, 3], [4, [5, 6]]]))
## contar_elementos( lista = [1, [2, 3], [4, [5, 6]]]  )
## lista[0] es una lista ?  1 es una lista? -> NO
## 1 + contar_elementos( lista = [[2, 3], [4, [5, 6]]] ) == 1 + 5 = 6
## lista[0] es una lista ?  [2, 3] es una lista? -> SI
## contar_elementos([2, 3]) +  contar_elementos([4, [5, 6] ) = 5
## 1 + contar_elementos(3) +   1 + contar_elementos([5, 6] ) = 5
## 1 + 1 + contar_elementos([]) + 1 + 1 + contar_elementos([6]) = 5
## 1 + 1 + 0 + 1 + 1 + 1 + contar_elementos([]) = 5
## 1 + 1 + 0 + 1 + 1 + 1 + 0 = 5

print(contar_elementos([[], [1, [2, 3]], 4]))
print(contar_elementos([[[]], [1, [2,[3,9,[]], 3]], 4]))
print(contar_elementos([]))

## Dado un string S con caracteres alfabéticos en minúscula, devuelva un string sin vocales
## s = "hola" -> hl
## Recursion de cola como no de cola.

def eliminarVocales(cadena : str, acumulador : str = "") -> str:
  if cadena == "":
    return acumulador
  elif cadena[0] in ['a', 'e', 'i', 'o', 'u'] :
    return eliminarVocales(cadena[1:], acumulador)
  else:
    return eliminarVocales(cadena[1:], acumulador + cadena[0] )

print(eliminarVocales("hola"))

## Escribe una función recursiva que determine si una cadena es un palíndromo.
## somos es palindromo, somos al reves es somos
## hola no es palindromo, hola al reves aloh
## acacia

def esPalindromo(cadena : str) -> bool :
  if len(cadena) == 0 or len(cadena) == 1:
    return True
  elif cadena[0] == cadena[-1] : ## Cadena en posicion cero es igual a cadena en ultima posicion
    return esPalindromo(cadena[1:-1]) ## Elimina de la cadena el primer y el ultimo caracter
  else:
    return False

print(esPalindromo("somos"))
print(esPalindromo("hola"))
print(esPalindromo("acacia"))
print(esPalindromo("acaci"))
print(esPalindromo("sommos"))

def esPrimo(n: int, i: int = 2) -> bool:
  if n == 1 or n == 2:
    return True
  elif n == i: ## i llego hasta el valor de n, es decir que en todo el recorrido no encontro divisores
    return True
  elif n % i == 0: ## si i es divisor de n
    return False
  else:
    return esPrimo(n, i + 1) ## incrementamos i para seguir buscando divisores

print(1, esPrimo(1))
print(2, esPrimo(2))
print(3, esPrimo(3))
print(4, esPrimo(4))
print(5, esPrimo(5))
print(6, esPrimo(6))
print(7, esPrimo(7))
print(8, esPrimo(8))
print(9, esPrimo(9))
print(10, esPrimo(10))
print(11, esPrimo(11))
print(12, esPrimo(12))


def eliminarRepetidosConsecutivos(cadena: str) -> str:

  if len(cadena) < 2:
    return cadena
    
  if cadena[0] == cadena[1]: ## Si el primer y el segundo caracter son iguales
    return eliminarRepetidosConsecutivos(cadena[1:]) ## elimino el primero , me quedo con el segundo y repito el proceso en el resto de la cadena
  else:
    return cadena[0] + eliminarRepetidosConsecutivos(cadena[1:]) ## no puedo descartar el primero, me quedo con el primero y repito el proceso en el resto de cadena

print(eliminarRepetidosConsecutivos("hhoolllllaaaaaaas"))

## Dada una matriz cuadrada NxN, rota la matriz en 90 grados hacia la derecha utilizando recursión.
def rotarMatriz(matriz: list[list]) -> list[list]:
  # Casos base: matriz vacía o sin columnas
  if matriz == [] or matriz[0] == []:
    return []

  # 1) Primera fila del resultado = primera columna de m, pero de abajo hacia arriba
  primeraFila = columnaPrimeraInvertida(matriz, len(matriz) - 1)

  # 2) Resto de columnas = matriz sin la primera columna
  resto = quitarPrimeraColumna(matriz, 0)
  return [primeraFila] + rotarMatriz(resto)

def columnaPrimeraInvertida(matriz: list[list], i: int) -> list:
  # Devuelve [m[i][0], m[i-1][0], ..., m[0][0]]
  if i < 0:
      return []
  return [matriz[i][0]] + columnaPrimeraInvertida(matriz, i - 1)

def quitarPrimeraColumna(matriz: list[list] , i : int) -> list[list]:
  # Devuelve una nueva matriz sin la primera columna, fila por fila
  if i == len(matriz):
      return []
  return [matriz[i][1:]] + quitarPrimeraColumna(matriz, i + 1)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


import numpy as np
print(np.array(matriz)) ## Lo imprimo con Numpy para mostrar mas facilmente la matriz



