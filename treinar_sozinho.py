import os, re, json, urllib.request, collections

BASE = "data/orafet"
os.makedirs(BASE, exist_ok=True)

print("ORAFET: baixando conhecimento open source")

fontes = {
    "geral.txt": "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt",
    "python.txt": "https://raw.githubusercontent.com/python/cpython/main/README.rst",
    "git.txt": "https://raw.githubusercontent.com/git/git/master/README.md",
}

for nome, url in fontes.items():
    caminho = os.path.join(BASE, nome)
    if os.path.exists(caminho):
        print("ja existe", nome)
        continue
    try:
        urllib.request.urlretrieve(url, caminho)
        print("baixado", nome)
    except Exception as e:
        print("falhou", nome, e)

print("ORAFET: juntando base")
texto = ""

if os.path.exists("input.txt"):
    texto += open("input.txt", encoding="utf-8", errors="ignore").read() + "\n\n"

for nome in fontes:
    caminho = os.path.join(BASE, nome)
    if os.path.exists(caminho):
        texto += open(caminho, encoding="utf-8", errors="ignore").read()[:150000] + "\n\n"

texto += """
# ORAFET - ESCOLA DE PROGRAMACAO
# Aula Python 1: variavel
# nome = 'Guga'
# idade = 25
# print(nome)
# Aula Python 2: funcao
# def soma(a,b):
#     return a + b
# print(soma(2,3))
# Aula Python 3: if
# if idade >= 18:
#     print('maior de idade')
# Aula Python 4: loop
# for i in range(5):
#     print(i)
# Aula Python 5: lista
# celulares = ['Z Flip 6', 'S24', 'iPhone']
# for c in celulares:
#     print(c)
# Aula Python 6: input
# nome = input('Qual seu nome ')
# print('Fala', nome)
# Aula Termux 1: cd ~/orafet entra na pasta
# Aula Termux 2: ls lista arquivos
# Aula Termux 3: python chat2.py roda o chat
# Aula Conserto: Z Flip 6 bateria - desligar, aquecer traseira, abrir com ventosa, desconectar flat, trocar bateria, testar
# Aula Conserto: tela quebrada - desligar, aquecer borda, remover tela, limpar cola, colar tela nova
# Conhecimento geral: O Brasil fica na America do Sul, capital Brasilia, Sao Paulo e a maior cidade
# Conhecimento geral: Python foi criado por Guido van Rossum
# Conhecimento geral: O Orafet foi criado pelo Guga em Sao Paulo
"""

texto = re.sub(r'\[.*?\]', 'Guga', texto)
open(os.path.join(BASE, "input.txt"), "w", encoding="utf-8").write(texto)
open("input.txt", "w", encoding="utf-8").write(texto)

print("ORAFET: criando modelo")
palavras = re.findall(r"[a-z0-9_]+", texto.lower())
modelo = collections.defaultdict(collections.Counter)
for i in range(len(palavras)-1):
    modelo[palavras[i]][palavras[i+1]] += 1

modelo_final = {k: dict(v) for k, v in modelo.items()}
open(os.path.join(BASE, "modelo.json"), "w", encoding="utf-8").write(json.dumps(modelo_final, ensure_ascii=False))
print("ORAFET: treino pronto, palavras:", len(palavras))
