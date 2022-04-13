import time

def tarefa1():
    inicio= time.time()
    x=0
    while x < 10000000:
        x+=1
    fim= time.time()
    print("Tarefa1: "+ str(fim-inicio))
    


def tarefa2():
    inicio = time.time()
    y=0
    while y < 10000000:
        y+=1
    fim= time.time()
    print("Tarefa2: "+ str(fim-inicio))

tarefa1()
tarefa2()