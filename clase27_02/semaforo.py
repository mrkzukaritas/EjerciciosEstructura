class Node:
    #objetos de node tiene url, apuntador  a enxt y apuntador a previous
    def __init__(self,color):
        self.color= color
        self.next= None

class semaforo:
    def __init__(self):

        #crear nodos con los colores del semaforo 
        verde=Node("verde")
        amarillo=Node("amarillo")
        rojo=Node("rojo")
        #concetar los nodos para formar la lista circular

        verde.next=amarillo
        amarillo.next=rojo
        rojo.next=verde

        self.actual= verde

    def next_ligth(self):
        #avanzar el semaforo 
        print(f"💡Semáforo en el color: {self.actual.color}")
        self.actual= self.actual.next

    def simular(self,veces):
        print("🚦Simulacion del semáforo")
        for i in range(veces):
            self.next_ligth()

#crear el semaforo 
semaforo=semaforo()
#simular 6 ciclos
semaforo.simular(6)
    

