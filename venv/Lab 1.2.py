a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
op = input("Podaj operator matematyczny: ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "/":
    print(a/b)
elif op == "*":
    print(a*b)
else:
    print("zly operator matematyczny")
