class Nodo:
    #init es el contructor 
    def __init__(self,dato):
        #atributos
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 
    
    def agregarInicio(self,dato):
        #se crea el nuevo nodo 
        nuevoNodo= Nodo(dato)
        #se verifica si la lista no esta vacia 
        if not self.cabeza:
            self.cabeza= nuevoNodo
        else:
            #primero guardamos el primer nodo en el siguiente
            nuevoNodo.siguiente= self.cabeza
            #y cambiamos la cabeza
            self.cabeza = nuevoNodo

    def agregarFinal(self,dato):
        #se crea el nuevo nodo 
        nuevoNodo= Nodo(dato)
        if not self.cabeza:
            self.cabeza= nuevoNodo
        else:
            puntero= self.cabeza
            while (puntero.siguiente != None):
                puntero= puntero.siguiente
            puntero.siguiente= nuevoNodo

    def ingresarDespues(self,dato,numero):

        nuevoNodo= Nodo(dato)
        puntero= self.cabeza
        if not self.cabeza:
            self.cabeza= nuevoNodo
        else:
            
            cont=0
            #va contando hasta donde quiere estar 
            while (cont < n and puntero.siguiente != None):
                puntero= puntero.siguiente
                n+=1
            #el nuevo nodo se pone en medio del puntero y el siguiente del puntero 
            nuevoNodo.siguiente= puntero.siguiente
            #primero guardamos la parte de atras de la lista 
            puntero.siguiente= nuevoNodo
            #y luego la unimos al principio 

    def eliminarInicio(self):
         
        if not self.cabeza:
             
             print("La lista esta vacia")
        else:
            #copiamos la cabeza
            puntero = self.cabeza
            #la cabeza se vuelve el segundo elementi
            self.cabeza = self.cabeza.siguiente
            #eliminamos la referencia 
            puntero.siguiente = None

    def eliminarUltimo(self):
        if not self.cabeza:
            print("a")
