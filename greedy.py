from time import perf_counter
import matplotlib.pyplot as plt
from tareas import *

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

tareas = Tareas()
actividades = tareas.task_lists
tamaños = []
tiempos = []

for actividad in actividades:

    n = len(actividad)
    tamaños.append(n)
    
    start_time = perf_counter()
    selected = MaxActivities(actividad, len(actividad))
    end_time = perf_counter()
    execution_time = end_time - start_time
    tiempos.append(execution_time)


    # print("Se seleccionaron las siguientes actividades :")
    # print(selected[0], end = "")
    # for i in range (1, len(selected)):
    #     print(",", end = " ")
    #     print(selected[i], end = "")
    # print("\n")
    

plt.plot(tamaños, tiempos)
plt.xlabel('Tamaño de entrada')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución en función del tamaño de entrada solucion greedy')
plt.show()