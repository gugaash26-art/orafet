import os, re, json, collections
print("ORAFET: treinando com os dados pesquisados")
texto = ""
if os.path.exists("input.txt"):
    texto += open("input.txt", encoding="utf-8", errors="ignore").read() + "\n"
if os.path.exists("data/orafet/input.txt"):
    texto += open("data/orafet/input.txt", encoding="utf-8", errors="ignore").read() + "\n"
texto = re.sub(r'\[.*?\]', ' 【entity-Guga¦canonical_name=Guga】', texto)
os.makedirs("data/orafet", exist_ok=True)
open("data/orafet/input.txt", "w", encoding="utf-8").write(texto)
open("input.txt", "w", encoding="utf-8").write(texto)
palavras = re.findall(r"[a-z0-9_]+", texto.lower())
modelo = collections.defaultdict(collections.Counter)
for i in range(len(palavras)-1):
    modelo[palavras[i]][palavras[i+1]] += 1
modelo_final = {k: dict(v) for k, v in modelo.items()}
open("data/orafet/modelo.json", "w", encoding="utf-8").write(json.dumps(modelo_final, ensure_ascii=False))
print("ORAFET: treino pronto, aprendeu", len(palavras), "palavras, vocab", len(modelo_final))
