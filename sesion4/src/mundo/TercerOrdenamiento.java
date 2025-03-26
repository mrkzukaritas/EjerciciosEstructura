package mundo;

import java.util.Arrays;

public class TercerOrdenamiento 
{
	/** 
	 * ORDENACION SELECCION
	 */
	public static void selectionSort(int[] arr) 
	{
		int n = arr.length;
		for (int i = 0; i < n - 1; i++) {
			int minIndex = i;
			for (int j = i + 1; j < n; j++) {//O(N^2)
				if (arr[j] < arr[minIndex]) {
					minIndex = j;
				}
			}
			int temp = arr[minIndex];
			arr[minIndex] = arr[i];
			arr[i] = temp;
		}
	}
	public static void main(String[] args) 
	{
		int[] arr = {376, 23, 184, 161, 103, 486, 325, 267, 474, 229, 343, 210, 154,
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
				120, 220};//o(1);o(n)

		long inicioEjecucion = System.nanoTime();
		
		selectionSort(arr);
		
		long finalEjecucion = System.nanoTime();

		long tiempoEjecucion = finalEjecucion - inicioEjecucion;

		System.out.println("Arreglo ordenado: ");
		
		System.out.println(Arrays.toString(arr));
		
		System.out.println("\nTiempo de ejecución de seleccion es de: " + tiempoEjecucion + " nanosegundos");
	}




}
