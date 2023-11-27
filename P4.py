v = float(input("Enter voltage (V): "))
i = float(input("Enter current (A): "))
h = float(input("Enter operating time (h): "))
Power = v * i
E = Power * h
C = 4 * E / 1000
print("The cost is",C)