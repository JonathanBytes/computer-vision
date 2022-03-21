while True:
    E=int(input('Intensidad: '))
    for E in range(4,16):
        print('Intensidad',E,': ')
        S=(3/2) * (E-4)
        print(S,'/',round(S,0))
