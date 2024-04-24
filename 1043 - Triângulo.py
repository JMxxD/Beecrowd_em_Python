A ,B ,C = list(map(float ,input().split()))

if ((A + B) > C) and ((B + C) > A) and ((A + C) > B):
    PERIMETRO = A + B + C
    print('Perimetro = %.1f' %PERIMETRO)

else:
    AREA = (A + B) * C / 2
    print('Area = %.1f' %AREA)
