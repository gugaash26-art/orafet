import os, subprocess, sys, json, random
print("ORAFET ONLINE - criado pelo Guga em Sao Paulo")
print("Comandos: aprender [tema] / python / bateria / termux / html / git / sair")
print("Exemplo: aprender python")
aulas_fixas = {
    "python": "Python: variavel e nome = 'Guga', depois print(nome). Funcao e def soma(a,b): return a + b.",
    "bateria": "Z Flip 6 bateria: desligar, aquecer traseira, abrir com ventosa, desconectar flat, trocar bateria, testar.",
    "termux": "Termux: cd ~/orafet entra, ls lista, python orafet.py roda.",
    "html": "HTML: <h1>Fala Guga</h1> cria titulo. <p>texto</p> cria paragrafo.",
    "git": "Git: git add . salva, git commit -m 'aula' registra, git push envia.",
    "loop": "Loop: for i in range(5): print(i) imprime 0 ate 4.",
    "funcao": "Funcao: def soma(a,b): return a + b. print(soma(2,3)) da 5.",
}
modelo = {}
if os.path.exists("data/orafet/modelo.json"):
    try:
        modelo = json.load(open("data/orafet/modelo.json", encoding="utf-8"))
    except:
        modelo = {}
while True:
    voce = input("\nVoce: ").strip()
    if not voce:
        continue
    baixo = voce.lower()
    if baixo == "sair":
        print("Orafet: Tamo junto, ate a proxima")
        break
    if baixo.startswith("aprender"):
        tema = voce[8:].strip() or "Python"
        print(f"Orafet: Vou pesquisar e aprender sobre {tema} agora...")
        subprocess.run([sys.executable, "pesquisar.py", tema])
        subprocess.run([sys.executable, "treinar_leve.py"])
        if os.path.exists("data/orafet/modelo.json"):
            modelo = json.load(open("data/orafet/modelo.json", encoding="utf-8"))
        print(f"Orafet: Aprendi sobre {tema}. Agora pergunta: o que e {tema}")
        continue
    achou = False
    for chave, resposta in aulas_fixas.items():
        if chave in baixo:
            print("Orafet:", resposta)
            achou = True
            break
    if achou:
        continue
    if os.path.exists("data/orafet/input.txt"):
        texto = open("data/orafet/input.txt", encoding="utf-8", errors="ignore").read()
        for linha in texto.split("\n"):
            if any(p in linha.lower() for p in baixo.split() if len(p) > 3) and "Pesquisa" in linha:
                print("Orafet: Achei na minha pesquisa -", linha[:400])
                achou = True
                break
    if achou:
        continue
    palavras = baixo.split()
    extra = ""
    for p in palavras:
        if p in modelo and modelo[p]:
            extra += " " + random.choice(list(modelo[p].keys()))
    if extra:
        print("Orafet: Pelo que aprendi -", extra)
    else:
        print("Orafet: Nao sei ainda. Digita: aprender " + voce)
