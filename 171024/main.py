liczba = 5

for i in range(3):
	podanaliczba = int(input("Podaj liczbe: "))

	if(podanaliczba==liczba):
		print("Zgadles liczbe!")
		break
	elif(podanaliczba>liczba):
		print("Podana liczba jest wieksza.")
	elif(podanaliczba<liczba):
		print("Podana liczba jest mniejsza")
