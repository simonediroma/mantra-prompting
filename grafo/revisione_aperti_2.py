#!/usr/bin/env python3
"""Seconda revisione dei punti aperti (2026-11-15), dopo l'obiezione dell'autore sul cap. 1.

Criterio: resta «aperto» solo ciò che il testo afferma in due modi che non possono essere veri insieme.
Omissioni, tempi stretti, termini diversi e frasi che ammettono una lettura coerente passano in «note».
"""
from pathlib import Path

S = Path(__file__).resolve().parent / "schede"
# id: inizio del testo del punto da spostare
SPOSTA = {
    "log-tv-caso-zero": None,            # tolto del tutto: «una volta» sui log Meridian, «decine» sul giradischi
    "log-tv-secondo-contatto": "nota",   # omissione nel cap. 3, non contraddizione
    "quaderno-nero": "nota",             # Tom può aver riaperto il quaderno dopo averlo chiuso
    "transcript-del-video": "nota",      # tempi stretti, non impossibili
    "indirizzo-elab": "nota",            # Emma può intendere il contatto predefinito di Elab
    "hard-reset": "nota",                # «un reset qualunque» è generico, non contraddice la procedura
}
SPOSTA_UNO = {  # schede con più punti: sposto solo quello che inizia così
    "tv-secondo-contatto": "Lo stesso dato si chiama",   # due nomi per un dato: scelta di stile
    "pete": "Pete ha firmato la sanzione",               # «Pete» può essere il nome per esteso
}


def blocco(righe, chiave):
    i = next((k for k, r in enumerate(righe) if r.startswith(chiave + ":")), None)
    if i is None:
        return None, None
    j = i + 1
    while j < len(righe) and righe[j].startswith("  "):
        j += 1
    return i, j


def sposta(id_, filtro, togli=False):
    f = next(S.glob(f"*/{id_}.yaml"))
    righe = f.read_text(encoding="utf-8").splitlines()
    i, j = blocco(righe, "aperti")
    voci = righe[i + 1:j]
    via = [v for v in voci if filtro is None or v.split('"', 1)[1].startswith(filtro)]
    assert via, id_
    resto = [v for v in voci if v not in via]
    righe[i:j] = (["aperti:"] + resto) if resto else []
    if not togli:
        n, m = blocco(righe, "note")
        if n is None:
            righe += ["note:"] + via
        else:
            righe[m:m] = via
    f.write_text("\n".join(righe) + "\n", encoding="utf-8")


for id_, cosa in SPOSTA.items():
    sposta(id_, None, togli=cosa is None)
for id_, inizio in SPOSTA_UNO.items():
    sposta(id_, inizio)
