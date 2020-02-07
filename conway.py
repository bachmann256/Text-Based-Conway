import os
import time
import random
cells = [random.choice([0,0,1]) for i in range(1000)]
neigh = [0] * 1000
def sorrounding(n):
    try: ch1 = cells[n+1]
    except: ch1 = 0
    try: ch2 = cells[n-1]
    except: ch2 = 0
    try: chv1 = cells[n+99]
    except: chv1 = 0
    try: chv2 = cells[n-99]
    except: chv2 = 0
    try: chvv1 = cells[n+101]
    except: chvv1 = 0
    try: chvv2 = cells[n-101]
    except: chvv2 = 0
    try: cv1 = cells[n-100]
    except: cv1 = 0
    try: cv2 = cells[n+100]
    except: cv2 = 0
    neigh[n] = ch1+ch2+cv1+cv2+chv1+chv2+chvv1+chvv2
def graph():
    os.system('cls')
    for i in range(len(cells)):
        if i % 100 == 0: print()
        if cells[i] == 0 : print(".", end="")
        elif cells[i] == 1: print("█", end="")
while True:
    graph()
    for i in range(len(cells)):
        sorrounding(i)
    for i in range(len(cells)):
        n8 = neigh[i]
        if n8 < 2 and cells[i]: cells[i] = 0
        elif n8 > 3 and cells[i]: cells[i] = 0
        elif n8 == 3 and not cells[i]: cells[i] = 1
    time.sleep(0.5)
    graph()
