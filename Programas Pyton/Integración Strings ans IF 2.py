# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:15:58 2020

@author: Jorge
"""

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
lugar=input("Ingrese localizacion: ")
edad=int(input("Ingresa tu edad:"))
space=""
print("Hola que tal como estas espero que hayas tenido un buen dia",nombre,space,apellido,
      space,"Vives en ",lugar,space,"es un lugar muy agradable con un muy buen clima",
      "La edad es una parte importante de la vida ya que a medida que los años avanzan sigues teniendo un mejor criterio de la vida con la edad actual que tengas que es "
      ,edad,"Años")
if edad >=1 and edad <=10:
    print("eres un niño ")
elif edad >=10 and edad <=18:
    print("Eres un adolescente")
else:
    print("Eres una persona Adulta ")
