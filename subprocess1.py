import time
import threading


def threading_test():
    inicio= time.time()
    x=0
    while x < 10000000:
        x+=1
    fim= time.time()
    print("Threading: "+ str(fim-inicio))
    


def tarefa2():
    inicio = time.time()
    y=0
    while y < 10000000:
        y+=1
    fim= time.time()
    print("Tarefa2: "+ str(fim-inicio))


threading.Thread(target=threading_test).start()
tarefa2()
