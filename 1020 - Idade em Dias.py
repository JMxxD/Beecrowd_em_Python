IDADE = int(input())
ANO = IDADE // 365
IDADE = IDADE - ANO*365
MES = IDADE // 30
IDADE = IDADE - MES*30
DIA = IDADE

print('{} ano(s)'.format(ANO))
print('{} mes(es)'.format(MES))
print('{} dia(s)'.format(DIA))
