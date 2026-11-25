import re, glob
for f in glob.glob('*.py'):
    txt = open(f, encoding='utf-8').read()
    txt = re.sub(r'Guga]*】', 'Guga', txt)
    txt = txt.replace('Guga', 'Guga')
    txt = txt.replace('', '')
    open(f, 'w', encoding='utf-8').write(txt)
    print('limpo', f)
