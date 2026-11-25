import random

# Respostas prontas do ORAFET
respostas = {
    "ola": "Fala Guga, beleza? Sou o Orafet, criado por voce em Sao Paulo.",
    "quem e voce": "Eu sou o Orafet, criado pelo Guga. Aprendo com o Guga.",
    "quem e o Guga": "O Guga e meu criador. Ele e de Sao Paulo e conserta celular.",
    "bateria": "Bora trocar essa bateria do Z Flip 6? Calma que eu te explico passo a passo.",
    "flip": "O Z Flip 6 e o favorito do Guga. Bora abrir ele com cuidado.",
    "celular": "Eu sou o Orafet, especialista em celular. O Guga me criou pra ajudar.",
    "tudo bem": "Tudo certo, Guga! E voce, bora consertar o que hoje?",
    "obrigado": "Tamo junto, Guga! Voce que me criou.",
}

print("ORAFET ONLINE! Fala comigo, Guga. Digita 'sair' pra parar.")

while True:
    voce = input("\nGuga: ").lower().strip()
    if voce == "sair":
        print("Orafet: Falou Guga, tamo junto!")
        break
    
    achou = False
    for palavra, resposta in respostas.items():
        if palavra in voce:
            print("Orafet:", resposta)
            achou = True
            break
    
    if not achou:
        print("Orafet: Fala Guga, nao entendi ainda, mas to aprendendo com voce. Me ensina mais?")
