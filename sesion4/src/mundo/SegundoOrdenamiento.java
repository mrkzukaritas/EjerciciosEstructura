package mundo;

import java.util.Arrays;

public class SegundoOrdenamiento 
{

	public static void insercionArray(int[] array) 
	{
		int n = array.length;
		for (int i = 1; i < n; i++) { // O(n^2) ; O(n)
			int key = array[i]; // O(1)
			int j = i - 1; //O(1)

			// Mueve los elementos mayores a la derecha
			while (j >= 0 && array[j] > key) {
				array[j + 1] = array[j];
				j--;
			}
			array[j + 1] = key;
		}
	}

	public static void main(String[] args) { //O(1)
		/** 
		 * ORDENACION INSERCCION
		 */
		int[] vals = {376, 23, 184, 161, 103, 486, 325, 267, 474, 229, 343, 210, 154,
				310, 429, 122, 61, 167, 108, 77, 43, 490, 442, 75, 137, 6, 53, 340, 20,
				488, 5, 44, 388, 221, 267, 36, 239, 156, 450, 15, 9, 174, 135, 149, 368,
				444, 267, 126, 16, 380, 425, 300, 252, 24, 284, 369, 197, 33, 55, 157, 302,
				342, 39, 124, 333, 372, 41, 68, 180, 13, 400, 100, 47, 295, 59, 392, 101,
				303, 437, 162, 231, 92, 308, 197, 398, 347, 148, 414, 101, 140, 283, 374,
				115, 78, 95, 283, 56, 229, 268, 166, 221, 264, 282, 314, 161, 34, 68, 102,
				294, 41, 161, 379, 234, 249, 238, 38, 151, 46, 359, 337, 276, 31, 129, 165,
				194, 398, 110, 121, 266, 283, 272, 124, 258, 186, 191, 148, 117, 237, 170,
				179, 366, 44, 60, 450, 119, 98, 201, 366, 86, 281, 448, 175, 49, 150, 104,
				165, 374, 330, 332, 194, 335, 128, 273, 371, 79, 197, 337, 234, 324, 87,
				120, 220};

		// Iniciar medición de tiempo
		long inicio = System.nanoTime(); //O(1)

		// Llamamos al método de ordenación
		insercionArray(vals); //O(1)

		// Finalizar medición de tiempo
		long fin = System.nanoTime(); // O(1)
		// Calcular y mostrar el tiempo en nanosegundos
		long tiempoTotal = fin - inicio;
		// Imprimimos el arreglo ordenado
		System.out.println("Arreglo ordenado:");
		
		System.out.println(Arrays.toString(vals));

		System.out.println("\nTiempo de ejecución de inserccion es de: " + tiempoTotal + " nanosegundos");
	}
}



