import timeit
import gmpy2
import math

A = gmpy2.mpz(12421772708041)


# Input a positive integer to factor.
# Put it inside the parentheses as "A = gmpy2.mpz(....)"

def factor(A):
    B = gmpy2.mpz(math.sqrt(math.pow(2, 1) * A + 0.25) - 1)
    D = gmpy2.mpz(A - (B * B + B) / 2)
    while (D > 0):
        B += 1
        D = gmpy2.mpz(A - (B * B + B) / 2)
    print(f"interim B: {B}")
    n = gmpy2.mpz(29840)  # 8529840 = 29840 (mod 100000)
    D += (n * (n + 1)) / 2
    B += 95028  # 9879358-4984330 = 95028 (mod 100000)
    D -= 95028 * B - (95028 * 95027) / 2
    c = 0
    while (D != 0 and B <= A):
        if (D > 0):
            B += 100000
            D -= 100000 * B - 4999950000
            c += 1
        else:
            D += 100000 * n + 5000050000
            n += 100000
            c += 1
    print(f"c: {c}")
    if B > A:
        return output(0, 0, 0)
    else:
        print(f"[B={B}, n={n}]")
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
        running_time = round(timer_stop - timer_start, 8)
        print("running time: ", running_time, " seconds")
    else:
        print("undefined for A<2")
