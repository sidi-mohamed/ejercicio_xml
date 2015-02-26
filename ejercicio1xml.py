# -*- coding: utf-8 -*-
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
numero=raw_input("dime una raza").upper()
razas=[]
arbol=etree.parse('perros.xml')
lista=arbol.getroot()

for n in xrange(len(lista)):
	if numero == lista[n][0].text:
		print "raza:",lista[n][0].text
		print "tamano:",lista[n][1].text
		print "codigo_postal:",lista[n][2].text
		print "barrio:",lista[n][3].text
		print "numero:",lista[n][4].text
		
		
	





