class Node:
    #objetos de node tiene url, apuntador  a enxt y apuntador a previous
    def __init__(self,url):
        self.url= url
        self.next= None
        self.previous= None

class History:
    #constructor nodo inicial vacio
    def __init__(self):
        self.actual = None
    
    def visit(self,url):
        newNode= Node( url)
        #preguntar si hay algun valor 
        if self.actual :
            newNode.previous=self.actual
            self.actual.next = newNode
        #se ejecuta si no hay nada o despues de de cambiar el anterior y despues del actual 
        self.actual= newNode
        print(f"visito {self.actual.url}")
    
    def back(self):
        if self.actual.previous:
            self.actual=self.actual.previous
            print(f"Retrocediendo a: {self.actual.url}")
        else:
            print("No hay mas paginas hacia atras")
        
    def foward(self):
        #preguntar si hay algo mas adelante 
        if self.actual.next:
            self.actual=self.actual.next
            print(f"Avanzando a: {self.actual.url}")
        else:
            print("No hay mas paginas adelante")


    #Implement a function to display the entire browsing history.
    def mostrar(self):
        
        puntero= self.actual
        print("")
        while puntero:
            print(puntero.url)
            puntero=puntero.previous
        print("")

    #Add a function to delete a specific page from the history

    def eliminar(self,url):
        puntero=self.actual
        if self.actual.url==url:
            self.actual=self.actual.previous
            print(f"se elimino {self.actual.next.url}")
            self.actual.next=None
        else:
            while puntero :
                if puntero.previous.url==url:
                    print(f"se elimino puntero {puntero.previous.url}")
                    puntero.previous=puntero.previous.previous
                puntero=puntero.previous

    def actualizar(self,url,newUrl):
        if self.buscar(url):
            self.mostrar()
            if self.actual.url==url:
                self.actual.url=newUrl
                print("Se ha cambiado la url")
                self.mostrar()
            else:
                puntero = self.actual
                while puntero :
                    if puntero.previous.url == url:
                        puntero.previous.url = newUrl
                        print("Se ha cambiado la url")
                        self.mostrar()
                        return
                    puntero=puntero.previous
       
    def buscar(self,url):
        puntero=self.actual
        if not puntero:  # Si no hay nodos, retorna None inmediatamente
            print("La lista está vacía.")
            return None

        # Si la URL está en el nodo actual
        if puntero.url == url:
            print(f"La url buscada es: {puntero.url}")
            return puntero.url
        while puntero.previous:
            puntero = puntero.previous  # Mueve el puntero hacia el nodo anterior
            if puntero.url == url:
                print(f"La URL buscada es: {puntero.url}")
                return puntero.url

        print("La url no está en la lista.")
        return None

historial = History()
historial.visit('https://www.unibague.edu.co/')
historial.visit('https://plataforma.unibague.edu.co/mod/folder/view.php?id=434314')
historial.visit('file:///C:/Users/Unibague/Downloads/Sesio%CC%81n%208.pdf')
print("----------------------------------------------")
print("Buscar una URL")
historial.buscar('fa')
print("----------------------------------------------")
print("Actualizar la URL")
historial.actualizar('https://www.unibague.edu.co/','akjshgkjas.xd')