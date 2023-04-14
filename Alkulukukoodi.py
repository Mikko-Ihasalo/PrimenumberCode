import matplotlib.pyplot as plt
# Original code taken from https://www.programiz.com/python-programming/examples/prime-number.
# Code is then altered to fit the wanted purpose.

def A_count_Primes_nums(n):

    ctr = 0
    
    for num in range(7,n,6):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

def B_count_Primes_nums(n):

    ctr = 0
    
    for num in range(11,n,6):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

def count_Primes_nums(n):
    ctr = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr

def koordinaatitA(luvut:int,vali:int):
    x=[]
    y=[]
    for i in range(1,luvut+1,vali):
        x.append(i)
        y.append(A_count_Primes_nums(i))
    plt.plot(x,y,label = "Alkuluvut A:ssa")

def koordinaatitB(luvut:int, vali:int):
    x=[]
    y=[]
    for i in range(1,luvut+1,vali):
        x.append(i)
        y.append(B_count_Primes_nums(i))
    plt.plot(x,y,label = "Alkuluvut B:ssa")

plt.xlabel("x")
plt.ylabel("Alkulukujen määrä")
plt.legend()