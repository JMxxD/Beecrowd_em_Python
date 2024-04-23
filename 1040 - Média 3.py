N1 ,N2 ,N3 ,N4 = list(map(float ,input().split()))

EXAME = 0.0
MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print('Media: %.1f' %MEDIA)

if MEDIA >= 7.0:
    print('Aluno aprovado.')

if MEDIA < 5.0:
    print('Aluno reprovado.')

if MEDIA >= 5.0 and MEDIA <= 6.9:
    print('Aluno em exame.')
    EXAME = float(input())
    print('Nota do exame: %.1f' %EXAME)
    MEDIA2 = (MEDIA + EXAME) / 2

    if MEDIA2 >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' %MEDIA2)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' %MEDIA2)
