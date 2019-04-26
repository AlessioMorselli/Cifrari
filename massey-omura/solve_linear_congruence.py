from math import gcd

def euclidean_algorithm(a: int, b: int):
    '''
        Applica l'algoritmo euclideo

        Argomenti:
        - a: int -> primo numero
        - b: int -> secondo numero

        => Restituisce la serie di quozienti e resti dell'algoritmo euclideo, tranne quello nullo
    '''
    # Faccio in modo che a sia sempre il numero più grande
    if b > a:
        tmp = a
        a = b
        b = tmp
    q = a // b
    r = a % b
    if r == 0:
        return [(q, b)]
    else:
        return [(q, b)] + euclidean_algorithm(b, r)

def bezouts_identity(a: int, b: int):
    '''
        Restituisce l'identità di Bezout:
            (a, b) = bezout_lambda * a + bezout_mu * b

        Argomenti:
        - a: int -> primo numero
        - b: int -> secondo numero

        => Restituisce la lista contenente lambda e mu
    '''

    def recursive_bezout(eclidean, k, c_k2, c_k1):
        if k - 2 == 0:
            return c_k2, c_k1
        else:
            c_k3 = c_k1
            c_k2 = c_k2 - euclidean[k-2][0] * c_k1
            return recursive_bezout(euclidean, k - 1, c_k3, c_k2)

    # Faccio in modo che a sia sempre il numero più grande
    reverse = False
    if b > a:
        reverse = True
        tmp = a
        a = b
        b = tmp
    
    euclidean = euclidean_algorithm(a, b)

    euclidean = [(0, a)] + euclidean
    n = len(euclidean) - 1

    bezout_lambda, bezout_mu = recursive_bezout(euclidean, n, 1, -euclidean[n-1][0])

    if not reverse:
        return bezout_lambda, bezout_mu
    else:
        return bezout_mu, bezout_lambda


def solve_linear_congurence(a: int, b: int, m: int):
    '''
        Risolve una congruenza del tipo ax = b (mod m)
        Si suppone (a, m) = 1

        Argomenti:
        - a: int -> coefficiente dell'incognita
        - b: int -> termine noto
        - m: int -> modulo

        => Restituisce l'incognita x o None nel caso (a, m) != 1
    '''
    if gcd(a, m) != 1:
        return None
    else:
        lambda_x = bezouts_identity(a, m)
        return lambda_x[0] * b % m
