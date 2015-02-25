# -*- coding : utf -8 -*-
from lxml import etree

# 
#1. programa que lista todas las razas de los perros
razas=[]
arbol=etree.parse('perros.xml')
nombres = arbol.findall ('animal/descripcion')
for nombre in nombres:
	if not nombre.text in razas:
		razas.append(nombre.text)
for raza in razas:
	print raza 
	





#2. programa que muestre el total de razas de cada perro 
razas=[]
arbol=etree.parse('perros.xml')
nombres = arbol.findall ('animal/descripcion')
for nombre in nombres:
	if not nombre.text in razas:
		razas.append(nombre.text)
for raza in razas:
	print len(raza)
















#3. programa que lea por teclado un nombre de raza y muestre  los datos
#4. indicarle el nombre de la raza y decirte si aparece mas de uno 






