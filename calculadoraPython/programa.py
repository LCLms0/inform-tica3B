from operacoes import *
from color50 import rgb, constants
import emoji
roxo = rgb(128, 0, 128)
print(emoji.emojize("-----------:alien_monster: BEM VINDO A CALCULADORA PYTHON:alien_monster: -----------"))
print("Você tem as seguintes operações disponiveis:  ")
print("Adição, Subtração, Multiplicação e Divisão.")
print("Comandos: ")
print("-----------------------")
print("[a] -> Adição")
print("-----------------------")
print("[b] -> Subtração")
print("-----------------------")
print("[c] -> Multiplicação")
print("-----------------------")
print("[d] -> Divisão")
print("-----------------------")
print("[e] -> Sair")
print("-----------------------")
print(roxo + "ATENÇÃO: os comandos devem estar em letra minuscula" + constants.RESET)

while True:
    operação = input("Escolha sua operação usando os comandos:  ")
    if operação == "a":
        soma()
    if operação == "b":
        subtracao()
    if operação == "c":
        multiplicacao()
    if operação == "d":
        divisao()
    if operação == "e":
        break
