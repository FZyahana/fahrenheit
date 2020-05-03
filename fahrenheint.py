#sei la mano salve jean
print("Transformador de medidas. Se inserir Celsius, devolverei em Farenheit e se inserir Farenheit devolverei em Celsius")
input("Aperte enter para continuar.")
op = str(input("Defina a unidade que você irá inserir. C = Celsius | F = Farenheit: "))

if (op != "C") and (op != "c") and (op != "F") and (op != "f"):
	print("Insira uma unidade válida.")
	input("Aperte enter para finalizar.")
else:
	med = float(input("Qual é quantidade de graus? "))
	if (op == "C") or (op == "c"):
		medc = (9*med/5)+32
		print("A conversão resultou em:", medc, "ºF")
		input("Aperte enter para finalizar.")
	else:
		medc = (med-32)*5/9
		print("A conversão resultou em:", medc, "ºC")
		input("Aperte enter para finalizar.")
