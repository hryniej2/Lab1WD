a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
c = input("Podaj operator: ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    print(a/b)
elif c == "*":
    print(a*b)
else:
    print("zly operator")
