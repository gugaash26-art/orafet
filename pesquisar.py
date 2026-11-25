import urllib.request, urllib.parse, json, os, sys, re
os.makedirs("data/orafet", exist_ok=True)
def limpar(texto):
    texto = re.sub(r'<[^>]+>', ' ', texto)
    texto = re.sub(r'\[.*?\]', ' Guga', texto)
    return texto[:8000]
def pesquisar_wikipedia(tema):
    print("ORAFET: pesquisando Wikipedia sobre", tema)
    try:
        url = "https://pt.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(tema)
        req = urllib.request.Request(url, headers={"User-Agent": "Orafet/1.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=15).read())
        texto = data.get("extract", "")
        if texto:
            print("ORAFET: achou na Wikipedia")
            return texto
    except Exception as e:
        print("ORAFET: nao achou na Wikipedia", e)
    return ""
if __name__ == "__main__":
    tema = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("O que pesquisar? ")
    if not tema:
        tema = "Python"
    texto = pesquisar_wikipedia(tema)
    if not texto:
        texto = f"Tema {tema} - O Orafet foi criado pelo Guga em Sao Paulo e ensina {tema} passo a passo."
    texto = limpar(texto)
    with open("data/orafet/input.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nPesquisa {tema}: {texto}\n")
    with open("input.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nPesquisa {tema}: {texto}\n")
    print("ORAFET: aprendi sobre", tema)
    print(texto[:500])
