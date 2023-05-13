import sys
import numpy as np
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import ayuda
import time
import random

cartas2=[]
bandera=0


puntaje_maquina=[0,0]
cartas=[["C","A"],["E","A"],["D","A"],["T","A"],["C","10"],["E","10"],["D","10"],["T","10"],
        ["C","2"],["E","2"],["D","2"],["T","2"],
        ["C","3"],["E","3"],["D","3"],["T","3"],["C","4"],["E","4"],["D","4"],["T","4"],
        ["C","5"],["E","5"],["D","5"],["T","5"],["C","6"],["E","6"],["D","6"],["T","6"],
        ["C","7"],["E","7"],["D","7"],["T","7"],["C","8"],["E","8"],["D","8"],["T","8"],
        ["C","9"],["E","9"],["D","9"],["T","9"],["C","J"],["E","J"],["D","J"],["T","J"],
        ["C","Q"],["E","Q"],["D","Q"],["T","Q"],["C","K"],["E","K"],["D","K"],["T","K"]]

lista=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
puntaje = [0,0]
carta1=[]
m,j=2,2
carta_m=[]
class venti_Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("21.ui",self)
        self.ini.clicked.connect(self.inicio)
        self.b5.clicked.connect(self.voltea)
        self.carta.clicked.connect(self.cartas)
        self.parar.clicked.connect(self.paraste)
        self.b1.clicked.connect(self.voltea2)

    def voltea(self):
        print(carta1)
        self.imagen(carta1,"j1")
    def voltea2(self):
        print(carta_m)
        self.imagen(carta_m,"m1")
    def inicio(self):
        globals()['m']=2
        globals()['j']=2
        globals()['puntaje']=[0,0]
        globals()['puntaje_maquina']=[0,0]
        self.carta.setEnabled(True)
        self.parar.setEnabled(True)
        self.b1.setIcon(QtGui.QIcon("N.jpg"))
        self.b1.setEnabled(False)
        self.b2.setIcon(QtGui.QIcon("N.jpg"))
        self.b3.setIcon(QtGui.QIcon("N.jpg"))
        self.b4.setIcon(QtGui.QIcon("N.jpg"))
        self.b5.setIcon(QtGui.QIcon("N.jpg"))
        self.b6.setIcon(QtGui.QIcon("N.jpg"))
        self.b7.setIcon(QtGui.QIcon("N.jpg"))
        self.b8.setIcon(QtGui.QIcon("N.jpg"))
        globals()['cartas2']=self.revolver()
        globals()['carta1']=cartas2.pop(0)
        print(carta1)
        puntaje2=self.npuntaje(carta1,1)
        globals()['puntaje']=puntaje2
        print(puntaje)
        self.b5.setIcon(QtGui.QIcon("atras.jpg"))
        globals()['carta_m']=cartas2.pop()
        print(carta_m)
        puntaje_maquina2=self.npuntaje(carta_m,2)
        globals()['puntaje_maquina']=puntaje_maquina2
        print(puntaje_maquina)
        self.listas(carta_m)
        self.b1.setIcon(QtGui.QIcon("atras.jpg"))
        carta2 = cartas2.pop(0)
        print(carta2)
        puntaje2 = self.npuntaje(carta2, 1)
        globals()['puntaje'] = puntaje2
        print(puntaje)
        self.listas(carta2)
        self.imagen(carta2,"j2")
        carta_m2 = cartas2.pop()
        print(carta_m2)
        self.listas(carta_m2)
        puntaje_maquina2 = self.npuntaje(carta_m2, 2)
        globals()['puntaje_maquina']=puntaje_maquina2
        print(puntaje_maquina)
        self.imagen(carta_m2,"m2")
        if puntaje[0] == 21:
            print("Ganaste")
            self.imagen(carta_m,"m1")
            self.carta.setEnabled(False)
            self.parar.setEnabled(False)
            print(puntaje, puntaje_maquina)
        elif puntaje_maquina[0]==21:
            print("Perdiste")
            self.imagen(carta_m, "m1")
            self.carta.setEnabled(False)
            self.parar.setEnabled(False)
            print(puntaje,puntaje_maquina)

    def revolver(self):
        for i in range(len(cartas)):
            indice = random.randint(0, len(cartas) - 1)
            lista = cartas[i]
            cartas[i] = cartas[indice]
            cartas[indice] = lista
        return cartas

    def npuntaje(self,carta,a):
        if(a==1):
            puntaje2 = puntaje
        else:
            puntaje2=puntaje_maquina
        numero = carta[1]
        if numero == "K" or numero == "J" or numero == "Q":
            puntaje2[0] += 10
        elif numero == "A":
            puntaje2[0] += 11
            puntaje2[1] = +1
        else:
            puntaje2[0] += int(numero)
        if puntaje2[0] > 21 and puntaje2[1] > 0:
            puntaje2[0] -= 10
            puntaje2[1] = -1
        return puntaje2

    def imagen(self, carta, n):
        if n =="j1":
            if carta == ["C", "A"]:
                self.b5.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b5.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b5.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b5.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b5.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b5.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b5.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b5.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b5.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b5.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b5.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b5.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b5.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b5.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b5.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b5.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b5.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b5.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b5.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b5.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b5.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b5.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b5.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b5.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b5.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b5.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b5.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b5.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b5.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b5.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b5.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b5.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b5.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b5.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b5.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b5.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b5.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b5.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b5.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b5.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b5.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b5.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b5.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b5.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b5.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b5.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b5.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b5.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b5.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b5.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b5.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b5.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="j2":
            if carta == ["C", "A"]:
                self.b7.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b7.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b7.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b7.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b7.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b7.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b7.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b7.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b7.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b7.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b7.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b7.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b7.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b7.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b7.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b7.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b7.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b7.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b7.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b7.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b7.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b7.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b7.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b7.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b7.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b7.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b7.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b7.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b7.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b7.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b7.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b7.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b7.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta== ["E", "8"]:
                self.b7.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b7.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b7.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b7.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b7.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b7.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b7.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b7.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b7.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b7.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b7.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b7.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b7.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b7.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b7.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b7.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b7.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b7.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b7.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="j3":
            if carta == ["C", "A"]:
                self.b6.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b6.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b6.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b6.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b6.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b6.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b6.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b6.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b6.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b6.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b6.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b6.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b6.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b6.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b6.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b6.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b6.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b6.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b6.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b6.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b6.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b6.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b6.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b6.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b6.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b6.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b6.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b6.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b6.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b6.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b6.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b6.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b6.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b6.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b6.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b6.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b6.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b6.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b6.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b6.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b6.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b6.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta== ["D", "4"]:
                self.b6.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b6.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b6.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b6.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b6.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b6.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b6.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b6.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b6.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b6.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="j4":
            if carta == ["C", "A"]:
                self.b8.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b8.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b8.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta== ["C", "4"]:
                self.b8.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b8.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b8.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b8.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b8.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b8.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b8.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b8.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b8.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b8.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b8.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b8.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b8.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b8.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b8.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b8.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b8.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b8.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b8.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b8.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b8.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b8.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b8.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b8.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b8.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b8.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b8.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b8.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b8.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b8.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b8.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b8.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b8.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b8.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b8.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b8.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b8.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b8.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b8.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b8.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta== ["D", "5"]:
                self.b8.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b8.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b8.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b8.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b8.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b8.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b8.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b8.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b8.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="m1":
            if carta == ["C", "A"]:
                self.b1.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b1.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b1.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b1.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b1.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b1.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b1.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b1.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b1.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b1.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b1.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b1.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b1.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b1.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b1.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b1.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b1.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b1.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b1.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b1.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b1.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b1.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b1.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b1.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b1.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b1.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b1.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b1.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b1.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b1.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b1.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b1.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b1.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b1.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b1.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b1.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b1.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b1.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b1.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b1.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b1.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b1.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b1.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b1.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b1.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b1.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b1.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b1.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b1.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b1.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b1.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b1.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="m2":
            if carta == ["C", "A"]:
                self.b2.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b2.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b2.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b2.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b2.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b2.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b2.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b2.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b2.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b2.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b2.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b2.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b2.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b2.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b2.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b2.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b2.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b2.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b2.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b2.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b2.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b2.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b2.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b2.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b2.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b2.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b2.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b2.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b2.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b2.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b2.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b2.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b2.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b2.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b2.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b2.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b2.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b2.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b2.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b2.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b2.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b2.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b2.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b2.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b2.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b2.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b2.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b2.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta== ["D", "10"]:
                self.b2.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b2.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b2.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b2.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="m3":
            if carta == ["C", "A"]:
                self.b3.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b3.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b3.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b3.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b3.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b3.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b3.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b3.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b3.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b3.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b3.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b3.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b3.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b3.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b3.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b3.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b3.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b3.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b3.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b3.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta == ["T", "8"]:
                self.b3.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b3.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b3.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b3.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b3.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b3.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b3.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b3.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b3.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b3.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b3.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b3.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b3.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b3.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b3.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b3.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b3.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b3.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b3.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b3.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b3.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b3.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b3.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b3.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b3.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b3.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b3.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b3.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b3.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b3.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b3.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b3.setIcon(QtGui.QIcon("kd.jpg"))
        elif n=="m4":
            if carta == ["C", "A"]:
                self.b4.setIcon(QtGui.QIcon("ac.jpg"))
            elif carta == ["C", "2"]:
                self.b4.setIcon(QtGui.QIcon("2c.jpg"))
            elif carta == ["C", "3"]:
                self.b4.setIcon(QtGui.QIcon("3c.jpg"))
            elif carta == ["C", "4"]:
                self.b4.setIcon(QtGui.QIcon("4c.jpg"))
            elif carta == ["C", "5"]:
                self.b4.setIcon(QtGui.QIcon("5c.jpg"))
            elif carta == ["C", "6"]:
                self.b4.setIcon(QtGui.QIcon("6c.jpg"))
            elif carta == ["C", "7"]:
                self.b4.setIcon(QtGui.QIcon("7c.jpg"))
            elif carta == ["C", "8"]:
                self.b4.setIcon(QtGui.QIcon("8c.jpg"))
            elif carta == ["C", "9"]:
                self.b4.setIcon(QtGui.QIcon("9c.jpg"))
            elif carta == ["C", "10"]:
                self.b4.setIcon(QtGui.QIcon("10c.jpg"))
            elif carta == ["C", "J"]:
                self.b4.setIcon(QtGui.QIcon("jc.jpg"))
            elif carta == ["C", "Q"]:
                self.b4.setIcon(QtGui.QIcon("qc.jpg"))
            elif carta == ["C", "K"]:
                self.b4.setIcon(QtGui.QIcon("kc.jpg"))
            elif carta == ["T", "A"]:
                self.b4.setIcon(QtGui.QIcon("at.jpg"))
            elif carta == ["T", "2"]:
                self.b4.setIcon(QtGui.QIcon("2t.jpg"))
            elif carta == ["T", "3"]:
                self.b4.setIcon(QtGui.QIcon("3t.jpg"))
            elif carta == ["T", "4"]:
                self.b4.setIcon(QtGui.QIcon("4t.jpg"))
            elif carta == ["T", "5"]:
                self.b4.setIcon(QtGui.QIcon("5t.jpg"))
            elif carta == ["T", "6"]:
                self.b4.setIcon(QtGui.QIcon("6t.jpg"))
            elif carta == ["T", "7"]:
                self.b4.setIcon(QtGui.QIcon("7t.jpg"))
            elif carta== ["T", "8"]:
                self.b4.setIcon(QtGui.QIcon("8t.jpg"))
            elif carta == ["T", "9"]:
                self.b4.setIcon(QtGui.QIcon("9t.jpg"))
            elif carta == ["T", "10"]:
                self.b4.setIcon(QtGui.QIcon("10t.jpg"))
            elif carta == ["T", "J"]:
                self.b4.setIcon(QtGui.QIcon("jt.jpg"))
            elif carta == ["T", "Q"]:
                self.b4.setIcon(QtGui.QIcon("qt.jpg"))
            elif carta == ["T", "K"]:
                self.b4.setIcon(QtGui.QIcon("kt.jpg"))
            elif carta == ["E", "A"]:
                self.b4.setIcon(QtGui.QIcon("ae.jpg"))
            elif carta == ["E", "2"]:
                self.b4.setIcon(QtGui.QIcon("2e.jpg"))
            elif carta == ["E", "3"]:
                self.b4.setIcon(QtGui.QIcon("3e.jpg"))
            elif carta == ["E", "4"]:
                self.b4.setIcon(QtGui.QIcon("4e.jpg"))
            elif carta == ["E", "5"]:
                self.b4.setIcon(QtGui.QIcon("5e.jpg"))
            elif carta == ["E", "6"]:
                self.b4.setIcon(QtGui.QIcon("6e.jpg"))
            elif carta == ["E", "7"]:
                self.b4.setIcon(QtGui.QIcon("7e.jpg"))
            elif carta == ["E", "8"]:
                self.b4.setIcon(QtGui.QIcon("8e.jpg"))
            elif carta == ["E", "9"]:
                self.b4.setIcon(QtGui.QIcon("9e.jpg"))
            elif carta == ["E", "10"]:
                self.b4.setIcon(QtGui.QIcon("10e.jpg"))
            elif carta == ["E", "J"]:
                self.b4.setIcon(QtGui.QIcon("je.jpg"))
            elif carta == ["E", "Q"]:
                self.b4.setIcon(QtGui.QIcon("qe.jpg"))
            elif carta == ["E", "K"]:
                self.b4.setIcon(QtGui.QIcon("ke.jpg"))
            elif carta == ["D", "A"]:
                self.b4.setIcon(QtGui.QIcon("ad.jpg"))
            elif carta == ["D", "2"]:
                self.b4.setIcon(QtGui.QIcon("2d.jpg"))
            elif carta == ["D", "3"]:
                self.b4.setIcon(QtGui.QIcon("3d.jpg"))
            elif carta == ["D", "4"]:
                self.b4.setIcon(QtGui.QIcon("4d.jpg"))
            elif carta == ["D", "5"]:
                self.b4.setIcon(QtGui.QIcon("5d.jpg"))
            elif carta == ["D", "6"]:
                self.b4.setIcon(QtGui.QIcon("6d.jpg"))
            elif carta == ["D", "7"]:
                self.b4.setIcon(QtGui.QIcon("7d.jpg"))
            elif carta == ["D", "8"]:
                self.b4.setIcon(QtGui.QIcon("8d.jpg"))
            elif carta == ["D", "9"]:
                self.b4.setIcon(QtGui.QIcon("9d.jpg"))
            elif carta == ["D", "10"]:
                self.b4.setIcon(QtGui.QIcon("10d.jpg"))
            elif carta == ["D", "J"]:
                self.b4.setIcon(QtGui.QIcon("jd.jpg"))
            elif carta == ["D", "Q"]:
                self.b4.setIcon(QtGui.QIcon("qd.jpg"))
            elif carta == ["D", "K"]:
                self.b4.setIcon(QtGui.QIcon("kd.jpg"))

    def listas(self,carta):
        numero = carta[1]
        if numero == "K" or numero == "J" or numero == "Q":
            lista.remove(10)
        elif numero == "A":
            lista.remove(1)
        else:
            lista.remove(int(numero))

    def cartas(self):
        globals()['j']+=1
        print(j)
        n="j{}".format(j)
        carta_n=cartas2.pop(0)
        print(carta_n)
        puntaje2 = self.npuntaje(carta_n, 1)
        print(puntaje2)
        self.listas(carta_n)
        globals()['puntaje'] = puntaje2
        self.imagen(carta_n, n)
        print(lista)
        if puntaje[0] > 21:
            print("Perdiste")
            self.imagen(carta_m, "m1")
            self.carta.setEnabled(False)
            self.parar.setEnabled(False)
            print(puntaje, puntaje_maquina)
            bandera =1
        if puntaje[0] == 21:
            print("Ganaste")
            self.imagen(carta_m, "m1")
            self.carta.setEnabled(False)
            self.parar.setEnabled(False)
            print(puntaje, puntaje_maquina)
            bandera = 1

    def paraste(self):
        self.carta.setEnabled(False)
        self.ini.setEnabled(False)
        meta = 21 - puntaje_maquina[0]
        lista_utilseñor = self.lista_util(meta)
        print(lista_utilseñor)
        proba = self.probabilidad(lista_utilseñor)
        print(proba)
        bandera=0
        print(bandera)
        while proba >= .30:
           # time.sleep(3)
            globals()['m'] += 1
            n = "m{}".format(m)
            carta_n_maquina = cartas2.pop(0)
            self.imagen(carta_n_maquina, n)
            print("Carta de maquina")
            print(carta_n_maquina, n)
            self.listas(carta_n_maquina)
            puntaje_maquina2=self.npuntaje(carta_n_maquina,2)
            print(puntaje_maquina2)
            globals()['puntaje_maquina']=puntaje_maquina2
            print(puntaje_maquina)
            time.sleep(1)
            if puntaje_maquina[0] > 21:
                print("Ganaste")
                #self.imagen(carta_m, "m1")
                self.ini.setEnabled(True)
                bandera=1
                print(puntaje, puntaje_maquina)
                break
            elif puntaje_maquina[0] == 21:
                print("perdiste")
                #self.imagen(carta_m, "m1")
                self.ini.setEnabled(True)
                bandera=1
                print(puntaje, puntaje_maquina)
                break
            meta = 21 - puntaje_maquina[0]
            lista_utilseñor = self.lista_util(meta)
            proba = self.probabilidad(lista_utilseñor)
            print(proba)
            #time.sleep(3)
        time.sleep(1)
        self.parar.setEnabled(False)
        if bandera==0:
            resta = 21 - puntaje[0]
            resta2 = 21 - puntaje_maquina[0]
            if resta < resta2:
                print("ganaste")
            else:
                print("Perdiste")
            print(puntaje, puntaje_maquina)
            self.ini.setEnabled(True)
        self.b1.setEnabled(True)


    def probabilidad(self,lista_utilseñor):
        tam = len(lista_utilseñor)
        tam2 = len(lista)
        proba1 = (tam / tam2) * ((tam - 1) / (tam2 - 1))
        proba2 = (1 - (tam / tam2)) * (tam / (tam2 - 1))
        return proba1 + proba2

    def lista_util(self,meta):
        lista2 = []
        if meta >= 10:
            return lista
        else:
            for i in range(len(lista)):
                if lista[i] <= meta:
                    lista2.append(lista[i])
                else:
                    break
            return lista2
if __name__=="__main__":
    app = QApplication(sys.argv)
    GUI = venti_Gui()
    GUI.show()
    sys.exit(app.exec_())