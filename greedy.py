from time import *
from time import perf_counter
import matplotlib.pyplot as plt

def MaxActivities(arr, n):
	selected = []

	# Se ordena segun el tiempo de finalizacion
	arr.sort(key=lambda x: x[1])

	# Siempre se elije la primera actividad
	i = 0
	selected.append(arr[i])

	for j in range(1, n):

		'''If this activity has start time greater than or
		equal to the finish time of previously selected
		activity, then select it'''
		if arr[j][0] >= arr[i][1]:
			selected.append(arr[j])
			i = j
	return selected

actividades = [ [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]], 
	       		[[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [2, 4], [1, 3]],
				[[3, 7], [1, 5], [2, 4], [0, 6], [4, 8], [6, 9], [2, 3], [4, 6], [7, 9]],
				[[2, 6], [0, 3], [4, 7], [1, 5], [3, 8], [5, 9], [7, 9], [1, 4], [6, 8], [3, 5]],
				[[0, 4], [3, 6], [2, 5], [1, 3], [4, 7], [6, 8], [5, 9], [2, 6], [3, 4], [7, 9], [0, 2]],
				[[1, 6], [2, 4], [5, 8], [3, 5], [0, 7], [4, 9], [2, 3], [6, 9], [1, 3], [4, 6], [7, 8], [6, 8]]]

tamaños = []
tiempos = []

for actividad in actividades:

    n = len(actividad)
    tamaños.append(n)
    
    # start_time = time.time()
    # selected = MaxActivities(actividad, len(actividad))
    # end_time = time.time()
    # execution_time = end_time - start_time
    start_time = perf_counter()
    selected = MaxActivities(actividad, len(actividad))
    end_time = perf_counter()
    execution_time = end_time - start_time
    tiempos.append(execution_time)


    print("Se seleccionaron las siguientes actividades :")
    print(selected[0], end = "")
    for i in range (1, len(selected)):
        print(",", end = " ")
        print(selected[i], end = "")
    print("\n")
    

plt.plot(tamaños, tiempos)
plt.xlabel('Tamaño de entrada')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución en función del tamaño de entrada solucion greedy')
plt.show()