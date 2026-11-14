#!/usr/bin/env python3
"""Aggiunge voci a schede esistenti senza riformattarle.

Legge da un file blocchi del tipo:
    @ oggetti/quaderno-nero  cap=4
    caratteristiche: {testo: "...", fonte: "c4:9"}
    stato: {cap: 4, testo: "..."}
    alias+: "nuovo alias"
"""
import re, sys
from pathlib import Path
SCHEDE = Path(__file__).resolve().parent / "schede"


def aggiungi(righe, chiave, voce):
    i = next((k for k, r in enumerate(righe) if r.startswith(chiave + ":")), None)
    if i is None:
        j = next((k for k, r in enumerate(righe) if r.startswith("relazioni:")), len(righe))
        righe[j:j] = [chiave + ":", "  - " + voce]
        return
    j = i + 1
    while j < len(righe) and (righe[j].startswith(" ") or not righe[j].strip()):
        j += 1
    righe.insert(j, "  - " + voce)


f = righe = None
def salva():
    if f:
        f.write_text("\n".join(righe) + "\n", encoding="utf-8")

for r in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    if r.startswith("@ "):
        salva()
        nome, *resto = r[2:].split()
        f = SCHEDE / (nome + ".yaml")
        righe = f.read_text(encoding="utf-8").splitlines()
        for x in resto:
            cap = x.split("=")[1]
            k = next(k for k, t in enumerate(righe) if t.startswith("capitoli:"))
            caps = re.findall(r"\d+", righe[k])
            if cap not in caps:
                righe[k] = "capitoli: [" + ", ".join(sorted(caps + [cap], key=int)) + "]"
    elif r.strip():
        chiave, voce = r.split(": ", 1)
        if chiave == "alias+":
            k = next((k for k, t in enumerate(righe) if t.startswith("alias:")), None)
            if k is None:
                righe.insert(2, f"alias: [{voce}]")
            else:
                righe[k] = righe[k].rstrip("]") + ", " + voce + "]"
        elif chiave in ("nome", "sintesi"):
            k = next(k for k, t in enumerate(righe) if t.startswith(chiave + ":"))
            righe[k] = f"{chiave}: {voce}"
        else:
            aggiungi(righe, chiave, voce)
salva()
