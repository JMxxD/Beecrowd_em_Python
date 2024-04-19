A = input().split()
CA, QA, VA = A
B = input().split()
CB, QB, VB = B

T = float(int(QA) * float(VA) + int(QB) * float(VB))
print('VALOR A PAGAR: R$ {:.2f}'.format(T)) 
