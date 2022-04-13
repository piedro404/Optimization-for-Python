import time
import threading
from functools import lru_cache

def threading_test():
    inicio= time.time()
    x=0
    while x < 10000000:
        x+=1
    fim= time.time()
    print("Threading: "+ str(fim-inicio))
    

@lru_cache
def lru_cache_test():
    inicio= time.time()
    x=0
    while x < 10000000:
        x+=1
    fim= time.time()
    print("Lru_Cache: "+ str(fim-inicio))



lru_cache_test()
threading.Thread(target=threading_test).start()
print("----------------------------------------------------------------")
threading.Thread(target=threading_test).start()
lru_cache_test()

#Lru_cache não pede passagem ou espera, só vai
#Threading da passagem e depois vai 
#Lru_cache win