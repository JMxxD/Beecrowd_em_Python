A ,B ,C = list(map(int ,input().split()))

MAIORAB = ((A + B + abs (A - B)) // 2)

if MAIORAB > C:
    print(MAIORAB ,'eh o maior')

elif C > MAIORAB:
    print(C ,'eh o maior')
