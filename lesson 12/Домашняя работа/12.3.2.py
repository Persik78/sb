import math

def sphereArea(R):
    S = 4 * math.pi * R**2
    print(S)

def sphereVolume(R):
    V = (4/3) * math.pi * R**3
    print(V)

while True:
    R = float(input('Введите радиус: '))
    sphereArea(R)
    sphereVolume(R)

