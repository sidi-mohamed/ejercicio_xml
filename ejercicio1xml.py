# -*- coding : utf -8 -*-
from lxml import etree
arbol=etree.parse('perros.xml')
nombres = arbol.findall ('animal/descripcion')
for nombre in nombres :
	print nombre.text







