def kinetic_energy(mass=int(input('Enter the mass in kg: >>> ')), velocity=int(input('Enter the velocity in m/s2: >> '))):
    return 12 * mass * velocity ** 2
print(kinetic_energy())