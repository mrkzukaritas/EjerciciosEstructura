class Node
{
    constructor(valor)
    {
        this.valor=valor;
        this.next=null;

    }
}

class Stack
{
    constructor()
    {
        this.top=null;//el de arriba del stack
        this.bottom=null;//elemento del fondo
        this.len=0;//tamaño de la pila
    }
    peek()
    {
        return this.top;

    }
    push(valor)//recibe el valor a añadir al stack 
    {
        const nuevo =new Node(valor);
        if (this.len ===0)
        {
            this.top=nuevo;
            this.bottom=nuevo;
        }else
        {
            const puntero = this.top;
            this.top= nuevo;
            this.top.next=puntero;
        }
        this.len++;
        return this;
    }

pop()
    {
        if (this.len ===0)
        {
            console.log("no hay elementos")
        }else
        {
            console.log("se va a eliminar", this.top.valor)
           this.top=this.top.next;
           this.len--;
           
        }
        return this;
    }
}
const stack = new Stack();
stack.push(2);
stack.push(4);
stack.push(5);
stack.push(6);
stack.push(7);

console.log(stack.peek());
stack.pop();
console.log(stack.peek());