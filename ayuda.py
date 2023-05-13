import random

cartas=[["C","A"],["E","A"],["D","A"],["T","A"],["C","10"],["E","10"],["D","10"],["T","10"],
        ["C","1"],["E","1"],["D","1"],["T","1"],["C","2"],["E","2"],["D","2"],["T","2"],
        ["C","3"],["E","3"],["D","3"],["T","3"],["C","4"],["E","4"],["D","4"],["T","4"],
        ["C","5"],["E","5"],["D","5"],["T","5"],["C","6"],["E","6"],["D","6"],["T","6"],
        ["C","7"],["E","7"],["D","7"],["T","7"],["C","8"],["E","8"],["D","8"],["T","8"],
        ["C","9"],["E","9"],["D","9"],["T","9"],["C","J"],["E","J"],["D","J"],["T","J"],
        ["C","Q"],["E","Q"],["D","Q"],["T","Q"],["C","K"],["E","K"],["D","K"],["T","K"]]

lista=[1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

def revolver():
    for i in range(len(cartas)):
        indice=random.randint(0,len(cartas)-1)
        lista=cartas[i]
        cartas[i]=cartas[indice]
        cartas[indice]=lista
    return cartas;

def npuntaje(carta, puntaje2):
    print("hola")
    numero=carta[1]
    if numero=="K" or numero=="J" or numero=="Q":
        puntaje2[0]+=10
    elif numero=="A":
        puntaje2[0]+=11
        puntaje2[1]=+1
    else:
        puntaje2[0]+=int(numero)
    if puntaje2[0]>21 and puntaje2[1]>0:
        puntaje2[0]-=10
        puntaje2[1]=-1
    return puntaje2

def listas(carta):
    numero = carta[1]
    if numero == "K" or numero == "J" or numero == "Q":
        lista.remove(10)
    elif numero == "A":
        lista.remove(1)
    else:
        lista.remove(int(numero))

def lista_util(meta):
    lista2=[]
    if meta >=10:
        return lista
    else:
        for i in range(len(lista)):
            if lista[i]<=meta:
                lista2.append(lista[i])
            else:
                break
        return lista2

def probabilidad():
    tam=len(lista_utilseñor)
    tam2=len(lista)
    proba1=(tam/tam2)*((tam-1)/(tam2-1))
    proba2=(1-(tam/tam2))*(tam/(tam2-1))
    return proba1+proba2
if __name__ == "__main__":
    juego="S"
    dinero=20

    while juego=="S" and dinero>0:
        print("Tienes {} pesos para apostar".format(dinero))
        apuesta=int(input("Ingrese la cantidad a apostar: "))
        bandera=0
        puntaje = [0,0]
        puntaje_maquina=[0,0]
        cartas2 = revolver()
        carta1 = cartas2.pop(0)
        print("Primer carta")
        print(carta1)
        puntaje = npuntaje(carta1,puntaje)
        carta1_m=cartas2.pop(0)
        listas(carta1_m)
        puntaje_maquina = npuntaje(carta1_m,puntaje_maquina)
        carta2=cartas2.pop(0)
        print("Segunda carta")
        print(carta2)
        puntaje = npuntaje(carta2, puntaje)
        listas(carta2)
        carta2_m = cartas2.pop(0)
        print("Carta de maquina")
        print(carta2_m)
        listas(carta2_m)
        puntaje_maquina=npuntaje(carta2_m,puntaje_maquina)
        if puntaje[0] == 21:
            print("Ganaste")
            dinero+=apuesta
            print(puntaje, puntaje_maquina)
        elif puntaje_maquina[0]==21:
            print("Perdiste")
            dinero -= apuesta
            print(puntaje,puntaje_maquina)
        else:
            sigue=input("Nueva carta? S/N"+ "\n")
            while sigue=="S":
                carta_n=cartas2.pop(0)
                print(carta_n)
                puntaje = npuntaje(carta_n, puntaje)
                listas(carta_n)
                if puntaje[0]>21:
                    print("Perdiste")
                    dinero -= apuesta
                    print(puntaje, puntaje_maquina)
                    bandera=1
                    break
                if puntaje[0] == 21:
                    print("Ganaste")
                    dinero += apuesta
                    print(puntaje, puntaje_maquina)
                    bandera = 1
                    break
                elif puntaje_maquina[0] == 21:
                    print("Perdiste")
                    dinero -= apuesta
                    print(puntaje, puntaje_maquina)
                    bandera = 1
                    break
                sigue = input("Nueva carta? S/N"+ "\n")
            if puntaje[0]<21:
                meta=21-puntaje_maquina[0]
                lista_utilseñor=lista_util(meta)
                proba=probabilidad()
                print(proba)
                while proba >= .5:
                    carta_n_maquina = cartas2.pop(0)
                    print("Carta de maquina")
                    print(carta_n_maquina)
                    listas(carta_n_maquina)
                    puntaje_maquina = npuntaje(carta_n_maquina, puntaje_maquina)
                    if puntaje_maquina[0] > 21:
                        print("Ganaste")
                        dinero += apuesta
                        print(puntaje, puntaje_maquina)
                        bandera = 1
                        break
                    elif puntaje_maquina[0] ==21:
                        print("perdiste")
                        dinero -= apuesta
                        print(puntaje, puntaje_maquina)
                        bandera = 1
                        break
                    meta = 21 - puntaje_maquina[0]
                    lista_utilseñor = lista_util(meta)
                    proba=probabilidad()
                    print(proba)
            if bandera==0:
                resta=21-puntaje[0]
                resta2=21-puntaje_maquina[0]
                if resta<resta2:
                    print("ganaste")
                    dinero += apuesta
                else:
                    print("Perdiste")
                    dinero -= apuesta
                print(puntaje,puntaje_maquina)
        if dinero>0:
            juego=input("Nuevo juego? S/N"+ "\n")
        else:
            print("Se te acabo el dinero")

