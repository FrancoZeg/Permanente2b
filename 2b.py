import time

def crearlista(n):
    lista = []
    for i in range(n+1):
        lista.append(i)
    return(lista)


tiempo1 = time.time()

def crearlista(n):
    lista = []
    for i in range(n+1):
        lista.append(i)
    return(lista)

def INSERTION_SORT(A):
    for j in (1, len(A)-1):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
            A[i + 1] = key
    return A

n = crearlista(10000)
is_n = INSERTION_SORT(n)

print(is_n)

tiempo2 = time.time()

tiempo3 = tiempo2-tiempo1

print(tiempo3)

tiempo4 = time.time()

def BUBBLE_SORT(L):
    n = len(L)
    for i in range(0, n-1):
        for j in range(n - 1, i + 1):
            if L[j] < L[j - 1]:
                L[j], L[j-1] = L[j - 1], L[j]
    return L

n2 = crearlista(10000)

bs_n = BUBBLE_SORT(n2)

print(bs_n)

tiempo5 = time.time()

print(tiempo5 - tiempo4)