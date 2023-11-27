power = float(input("Enter power in watt:"))
time = float(input("Enter operating hours:"))

energy_Wh = power * time
energy_J = 3600 * energy_Wh

print("Energy = {:,.2f} Wh or {:,.2f} J".format(energy_Wh, energy_J))