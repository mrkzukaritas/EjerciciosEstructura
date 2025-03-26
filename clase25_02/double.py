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
    
#crear la clase bidireccional
class bidirectional(Node):
    #definir metodo constructor con data, next, previous
    def __init__(self, data, next=None,previous=None):
        super().__init__(data, next)
        self.previous= previous

head= bidirectional(1)
tail=head
for data in range(2,6):
    tail.next= bidirectional(data,previous=tail)
    tail=tail.next

puntero=tail
while puntero !=None:
    print(puntero.data)
    puntero=puntero.previous
print("otro orden")
puntero=head
while puntero !=None:
    print(puntero.data)
    puntero=puntero.next
print("-------------------")

head.previous=tail
tail.next= head
f=0
puntero=head

while puntero !=None and f<20:
    print(puntero.data)
    puntero=puntero.next
    f+=1
print("asga")