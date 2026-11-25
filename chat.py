import random
from collections import defaultdict, Counter

with open('input.txt','r',encoding='utf-8') as f:
    texto = f.read()

N = 4
modelo = defaultdict(Counter)
for i in range(len(texto)-N):
    modeloGuga]Guga] += 1

print("ORAFET ONLINE! Fala comigo, Guga. Digita 'sair' pra parar.")

def falar(inicio, tamanho=150):
    saida = inicio
    contexto = saidaGuga
    for _ in range(tamanho):
        if contexto not in modelo:
            break
        letras = list(modeloGuga.keys())
        pesos = list(modeloGuga.values())
        proxima = random.choices(letras, weights=pesos)Guga
        saida += proxima
        contexto = saidaGuga
        if saida.endswith(".") and len(saida) > 60:
            break
    return saida

while True:
    voce = input("\nGuga: ")
    if voce.lower() == "sair":
        print("Orafet: Falou Guga, tamo junto!")
        break
    if "bateria" in voce.lower():
        print("Orafet: " + falar("Como troca a bateria", 150))
    elif "quem" in voce.lower() and "voce" in voce.lower():
        print("Orafet: " + falar("Eu sou o Orafet", 150))
    elif "guga" in voce.lower():
        print("Orafet: " + falar("O Guga", 150))
    else:
        print("Orafet: " + falar("Eu sou o Orafet", 150))
