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
    n = gmpy2.mpz(9840)  # 8529840 = 9840 (mod 30000)
    D += (n * (n + 1)) / 2
    B += 5028  # 9879358-4984330 = 5028 (mod 30000)
    D -= 5028 * B - (5028 * 5027) / 2
    while (D != 0 and B <= A):
        if (D > 0):
            B += 30000
            D -= 30000 * B - 449985000
        else:
            D += 30000 * n + 450015000
            n += 30000
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
        running_time = round(timer_stop - timer_start, 6)
        print("running time: ", running_time, " seconds")
    else:
        print("undefined for A<2")
