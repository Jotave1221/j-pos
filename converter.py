import json
from pathlib import Path

raiz = Path("programas")
fs = json.loads(Path("filesystem.json").read_text())

for arq in raiz.rglob("*.py"):
    partes = arq.relative_to(raiz).parts
    pasta = fs
    for parte in partes[:-1]:
        pasta = pasta.setdefault(parte, {})
    codigo = arq.read_text()
    if partes[0] == "bin":
        primeira, _, resto = codigo.partition("\n")
        if primeira.startswith("#nivel="):
            pasta[arq.name] = [resto, int(primeira[7:])]
        else:
            pasta[arq.name] = [codigo, 1]
    else:
        pasta[arq.name] = codigo

Path("filesystem.json").write_text(json.dumps(fs, indent=2))