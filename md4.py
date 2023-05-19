import struct


def md4(message):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    length = len(message)
    message += b"\x80"
    while len(message) % 64 != 56:
        message += b"\x00"
    message += struct.pack("<Q", length * 8)

    def F(X, Y, Z):
        return (X & Y) | (~X & Z)

    def G(X, Y, Z):
        return (X & Y) | (X & Z) | (Y & Z)

    def H(X, Y, Z):
        return X ^ Y ^ Z

    def rotate_left(x, n):
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

    def FF(a, b, c, d, x, s):
        return rotate_left((a + F(b, c, d) + x) & 0xFFFFFFFF, s)

    def GG(a, b, c, d, x, s):
        return rotate_left((a + G(b, c, d) + x + 0x5A827999) & 0xFFFFFFFF, s)

    def HH(a, b, c, d, x, s):
        return rotate_left((a + H(b, c, d) + x + 0x6ED9EBA1) & 0xFFFFFFFF, s)

    for i in range(0, len(message), 64):
        X = struct.unpack("<16I", message[i : i + 64])

        AA, BB, CC, DD = A, B, C, D

        A = FF(A, B, C, D, X[0], 3)
        D = FF(D, A, B, C, X[1], 7)
        C = FF(C, D, A, B, X[2], 11)
        B = FF(B, C, D, A, X[3], 19)

        A = FF(A, B, C, D, X[4], 3)
        D = FF(D, A, B, C, X[5], 7)
        C = FF(C, D, A, B, X[6], 11)
        B = FF(B, C, D, A, X[7], 19)

        A = FF(A, B, C, D, X[8], 3)
        D = FF(D, A, B, C, X[9], 7)
        C = FF(C, D, A, B, X[10], 11)
        B = FF(B, C, D, A, X[11], 19)

        A = FF(A, B, C, D, X[12], 3)
        D = FF(D, A, B, C, X[13], 7)
        C = FF(C, D, A, B, X[14], 11)
        B = FF(B, C, D, A, X[15], 19)

        A = GG(A, B, C, D, X[0], 3)
        D = GG(D, A, B, C, X[4], 5)
        C = GG(C, D, A, B, X[8], 9)
        B = GG(B, C, D, A, X[12], 13)

        A = GG(A, B, C, D, X[1], 3)
        D = GG(D, A, B, C, X[5], 5)
        C = GG(C, D, A, B, X[9], 9)
        B = GG(B, C, D, A, X[13], 13)

        A = GG(A, B, C, D, X[2], 3)
        D = GG(D, A, B, C, X[6], 5)
        C = GG(C, D, A, B, X[10], 9)
        B = GG(B, C, D, A, X[14], 13)

        A = GG(A, B, C, D, X[3], 3)
        D = GG(D, A, B, C, X[7], 5)
        C = GG(C, D, A, B, X[11], 9)
        B = GG(B, C, D, A, X[15], 13)

        A = HH(A, B, C, D, X[0], 3)
        D = HH(D, A, B, C, X[8], 9)
        C = HH(C, D, A, B, X[4], 11)
        B = HH(B, C, D, A, X[12], 15)

        A = HH(A, B, C, D, X[2], 3)
        D = HH(D, A, B, C, X[10], 9)
        C = HH(C, D, A, B, X[6], 11)
        B = HH(B, C, D, A, X[14], 15)

        A = HH(A, B, C, D, X[1], 3)
        D = HH(D, A, B, C, X[9], 9)
        C = HH(C, D, A, B, X[5], 11)
        B = HH(B, C, D, A, X[13], 15)

        A = HH(A, B, C, D, X[3], 3)
        D = HH(D, A, B, C, X[11], 9)
        C = HH(C, D, A, B, X[7], 11)
        B = HH(B, C, D, A, X[15], 15)

        A = A + AA & 0xFFFFFFFF
        B = B + BB & 0xFFFFFFFF
        C = C + CC & 0xFFFFFFFF
        D = D + DD & 0xFFFFFFFF

    hash = struct.pack("<4I", A, B, C, D)
    return hash.hex()


message = b"The quick"
result = md4(message)
print(result)
