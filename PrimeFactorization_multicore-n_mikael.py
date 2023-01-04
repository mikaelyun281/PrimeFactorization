import timeit
import gmpy2
import math
import multiprocessing

A = gmpy2.mpz(math.pow(2,29)-1)
# Input a positive integer to factor.
# Put it inside the parentheses as "A = gmpy2.mpz(....)"

k = 6
# Input the number of cores to be used as "k=..."
# [!!Caveat!!] Don't use too much number of cores which exceeds the
# availability of CPU resources of your personal computer environment.
# It can damage the CPU !!!

def factor(n):
    if A < 2:
        print("undefined for A<2")
    else:
        B = gmpy2.mpz(math.sqrt(2 * A + 0.25) - 1)
        D = gmpy2.mpz(A - (B * B + B) / 2)
        while (D > 0):
            B += 1
            D = gmpy2.mpz(A - (B * B + B) / 2)
        D += gmpy2.mpz(n * (n + 1) / 2)
        while (D != 0 and B <= A):
            if (D > 0):
                B += 1
                D -= B
            else:
                D += k * n + (k * (k + 1)) / 2
                n += k
        if B > A:
            return output(0, 0, 0)
        else:
            if (B - n) % 2 == 0:
                E = gmpy2.mpz((B - n) / 2)
                F = gmpy2.mpz(B + n + 1)
            else:
                E = gmpy2.mpz(B - n)
                F = gmpy2.mpz((B + n + 1) / 2)
            return output(A, E, F)


def output(A, E, F):
    timer_stop = timeit.default_timer()
    running_time = round(timer_stop - timer_start, 6)
    if A == 0:
        print(f"Initial Value Error: Reset the B or k value \n")
    else:
        if A % E != 0 or A % F != 0 or A != E * F:
            print(f"[Error Occurred]  {A}  !=  {E}  *  {F} \n")
        else:
            print(f"[running time: {running_time} seconds]  {A}  =  {E}  *  {F} \n")
    return 0


if __name__ == '__main__':
    n = []
    timer_start = timeit.default_timer()
    with multiprocessing.Pool(processes=k) as pool:
        for x in range(0, k):
            y = gmpy2.mpz(x)
            n.append(y)
        results = pool.map(factor, n)
