import json, os, random, re

aulas = {
    "python": "Aula Python: variavel e assim - nome = '【entity-Guga¦canonical_name=Guga】' - depois print(nome). Quer aprender funcao? digita: funcao",
    "funcao": "Aula funcao: def soma(a,b): return a+b - depois print(soma(2,3)) vai dar 5",
    "loop": "Aula loop: for i in range(5): print(i) - isso imprime 0 ate 4",
    "lista": "Aula lista: celulares = ['Z Flip 6','S24'] - for c in celulares: print(c)",
    "if": "Aula if: if idade >= 18: print('maior de idade')",
    "termux": "Aula Termux: cd ~/orafet entra, ls lista, python orafet_ensina.py roda o chat",
    "bateria": "Aula conserto Z Flip 6: desligar, aquecer traseira, abrir com ventosa, desconectar flat, trocar bateria, testar",
    "tela": "Aula tela: desligar, aquecer borda, remover tela, limpar cola, colar tela nova",
    "html": "Aula HTML: <h1>Fala Guga</h1> cria um titulo na pagina",
    "git": "Aula git: git add . salva, git commit -m 'aula' registra, git push envia",
}

print("ORAFET ESCOLA ONLINE - digita: python, funcao, loop, lista, if, termux, bateria, tela, html, git")
print("Digita sair para parar")

modelo = {}
if os.path.exists("data/orafet/modelo.json"):
    modelo = json.load(open("data/orafet/modelo.json", encoding="utf-8"))

while True:
    voce = input("\nVoce: ").lower().strip()
    if voce == "sair":
        print("Orafet: Tamo junto, ate a proxima aula")
        break
    achou = False
    for chave, resposta in aulas.items():
        if chave in voce:
            print("Orafet:", resposta)
            achou = True
            break
    if not achou:
        if voce in modelo and modelo[voce]:
            proxima = random.choice(list(modelo[voce].keys()))
            print("Orafet: aprendi isso -", voce, proxima)
        else:
            print("Orafet: Nao sei ainda, mas vou aprender. Digita: python ou bateria ou termux")
