import time
from functools import lru_cache

@lru_cache
def lru_cache_test():
    inicio= time.time()
    x=0
    while x < 10000000:
        x+=1
    fim= time.time()
    print("Lru_Cache: "+ str(fim-inicio))
    


def tarefa2():
    inicio = time.time()
    y=0
    while y < 10000000:
        y+=1
    fim= time.time()
    print("Tarefa2: "+ str(fim-inicio))

lru_cache_test()
tarefa2()