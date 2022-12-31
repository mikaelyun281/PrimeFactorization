import timeit
import gmpy2
import math

A = gmpy2.mpz(11111111111)
# Input a positive integer to factor.
# Put it inside the parentheses as "A = gmpy2.mpz(....)"

def factor(A):
    B = gmpy2.mpz(math.sqrt(2 * A + 0.25) - 1)
    D = gmpy2.mpz(A - (B * B + B) / 2)
    while (D > 0):
        B += 1
        D = gmpy2.mpz(A - (B * B + B) / 2)
    n = gmpy2.mpz(0)
    while (D != 0 and B <= A):
        if (D > 0):
            B += 1
            D -= B
        else:
            n += 1
            D += n
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
    if A == 0:
        print(f"Initial Value Error: Reset the B value")
    else:
        if A % E != 0 or A % F != 0 or A != E * F:
            print(f"[Error Occurred]  {A}  !=  {E}  *  {F}")
        else:
            print(f"{A}  =  {E}  *  {F}")
    return 0


if __name__ == '__main__':
    if A >= 2:
        timer_start = timeit.default_timer()
        factor(A)
        timer_stop = timeit.default_timer()
        running_time = round(timer_stop - timer_start, 6)
        print("running time: ", running_time, " seconds")
    else:
        print("undefined for A<2")
