#Crear la clase node 
class Node:
    #Definir su metodo constructor y sus atributos 

    #Constructor
    def __init__(self,data,next =None):

        #Atributos
        #data es la informacion
        self.data=data
        #next es lo que apunta a el siguiente nodo ; al principio no hay nada porq apenas la creamos
        self.next=next
    

    