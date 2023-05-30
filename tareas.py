import random

class Tareas(object):
    def __init__(self):
        total_tasks = 500
        task_jump = 3
        task_lists = []

        for i in range(total_tasks):
            task_list = []
            for j in range(0, (i+1)*task_jump):
                start = random.randint(0, 8)
                end = random.randint(start, 10)
                task_list.append([start, end])
            task_lists.append(task_list)

        
        print("Se generaron las tareas")

        self.task_lists = task_lists

