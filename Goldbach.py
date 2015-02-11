import math
#Funcion para saber si un numero es 3 o no
def es_primo(a):
  contador = 0
  verificar= False
  for i in range(1,a+1):
    if (a% i)==0:
       contador = contador + 1
    if contador >= 3:
        verificar=True
        break
  if contador==2 or verificar==False:
    return True
  return False


#Creacion de un lista con todos los primos del 1 al 10,000
def lista_primos():
	primos = list();
	for i in range (1,10000):
		if es_primo(i):
			primos.append(i)
	return primos

def lista_impares():
	impares = list();
	for i in range (1,10000,2):
		if not es_primo(i):
			impares.append(i)

primos = lista_primos()
impares = lista_impares()
a = 0
impar = 1
for primo in primos:
	for n in range (1,10000):
		a = primo + (2)*(math.pow(n,2))
		if a != impar and n > 500000:
			print (impar)
		impar += 2
