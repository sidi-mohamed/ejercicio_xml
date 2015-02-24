# -*- coding : utf -8 -*-
from lxml import etree

# 
#1. programa que lista todas las razas de los perros

arbol=etree.parse('perros.xml')
nombres = arbol.findall ('animal/descripcion')
for nombre in nombres :
	print nombre.text

#2. programa que muestre el total de razas de perros programa que le indiques un numero y te imprima todos los datos 












#3. programa que lea por teclado un nombre de raza y muestre  los datos
#4. indicarle el nombre de la raza y decirte si aparece mas de uno 






