A ,B ,C = list(map(float, input().split()))

DELTA = ((B**2)-4*A*C)

if ((DELTA < 0) or A == 0):
	print( "Impossivel calcular")
	
elif ( DELTA == 0 ):
	RAIZ_1 = (-B + DELTA **(1/2))/(2*A)
	RAIZ_2 = RAIZ_1
	print("R1 = %.5f" %(RAIZ_1))
	print("R2 = %.5f" %(RAIZ_2))

else:
	RAIZ_1 = (-B + DELTA **(1/2))/(2*A)
	RAIZ_2 = (-B - DELTA **(1/2))/(2*A)
	print("R1 = %.5f" %(RAIZ_1))
	print("R2 = %.5f" %(RAIZ_2))
