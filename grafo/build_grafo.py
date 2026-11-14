#!/usr/bin/env python3
"""Costruisce il grafo del libro dalle schede YAML.

  python3 grafo/build_grafo.py

Legge  grafo/schede/<tipo>/<id>.yaml  e  grafo/capitoli.yaml
Scrive grafo/vista/**.md (schede leggibili con link e backlink),
       grafo/INDICE.md, grafo/grafo.json
Si ferma con errore se una scheda cita un id inesistente o una riga fuori dal capitolo.
Avvisa se un capitolo è cambiato di versione dopo l'analisi.
"""
import json, re, shutil, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
BOOK = ROOT.parent
SCHEDE, VISTA = ROOT / "schede", ROOT / "vista"
TIPI = {"personaggi": "personaggio", "organizzazioni": "organizzazione", "oggetti": "oggetto",
        "luoghi": "luogo", "concetti": "concetto", "termini": "termine", "eventi": "evento"}
PLUR = {v: k for k, v in TIPI.items()}
errori, avvisi = [], []


def carica():
    nodi = {}
    for cartella, tipo in TIPI.items():
        for f in sorted((SCHEDE / cartella).glob("*.yaml")):
            d = yaml.safe_load(f.read_text(encoding="utf-8"))
            if d.get("id") != f.stem:
                errori.append(f"{f}: id '{d.get('id')}' diverso dal nome file")
            if d["id"] in nodi:
                errori.append(f"id duplicato: {d['id']}")
            d["tipo"] = tipo
            nodi[d["id"]] = d
    return nodi


def capitoli_info():
    info = yaml.safe_load((ROOT / "capitoli.yaml").read_text(encoding="utf-8"))
    for n, c in info.items():
        testo = (BOOK / c["file"]).read_text(encoding="utf-8")
        m = re.search(r"^version:\s*(\S+)", testo, re.M)
        c["righe"] = testo.count("\n") + 1
        c["versione_attuale"] = m.group(1) if m else "?"
        if c["versione_attuale"] != str(c["versione_analizzata"]):
            avvisi.append(f"cap. {n}: analizzata v{c['versione_analizzata']}, il file è alla "
                          f"v{c['versione_attuale']} → schede da riverificare")
    return info


def fonti(d):
    """Tutte le stringhe 'fonte' dentro una scheda."""
    if isinstance(d, dict):
        for k, v in d.items():
            if k == "fonte":
                yield str(v)
            else:
                yield from fonti(v)
    elif isinstance(d, list):
        for x in d:
            yield from fonti(x)


def controlla_fonte(f, caps, dove):
    for pezzo in re.split(r"[,;]\s*", f):
        m = re.fullmatch(r"c(\d+):(\d+)(?:-(\d+))?", pezzo.strip())
        if not m:
            errori.append(f"{dove}: fonte '{pezzo}' non nel formato cN:riga")
            continue
        cap = int(m.group(1))
        if cap not in caps:
            errori.append(f"{dove}: fonte {pezzo}, capitolo non in capitoli.yaml")
        elif int(m.group(3) or m.group(2)) > caps[cap]["righe"]:
            errori.append(f"{dove}: fonte {pezzo} oltre la fine del capitolo")


def link(nodi, i, da_tipo=None):
    if i not in nodi:
        return f"**{i}?**"
    n = nodi[i]
    return f"[{n['nome']}](../{PLUR[n['tipo']]}/{i}.md)"


def fmt_fonte(f):
    return "*(" + re.sub(r"c(\d+):", r"cap. \1 r. ", f) + ")*"


def main():
    nodi = carica()
    caps = capitoli_info()
    archi = []
    for i, n in nodi.items():
        for f in fonti(n):
            controlla_fonte(f, caps, i)
        for r in n.get("relazioni", []):
            archi.append({"da": i, "a": r["verso"], "tipo": r["tipo"], "nota": r.get("nota", ""),
                          "fonte": r.get("fonte", "")})
        if n["tipo"] == "evento":
            for x in n.get("coinvolti", []):
                archi.append({"da": i, "a": x, "tipo": "coinvolge", "nota": "", "fonte": ""})
            if n.get("dove"):
                archi.append({"da": i, "a": n["dove"], "tipo": "avviene in", "nota": "", "fonte": ""})
            for x in n.get("dopo", []):
                archi.append({"da": x, "a": i, "tipo": "porta a", "nota": "", "fonte": ""})
    for a in archi:
        for k in ("da", "a"):
            if a[k] not in nodi:
                errori.append(f"arco {a['da']} → {a['a']} ({a['tipo']}): '{a[k]}' non esiste")
    if errori:
        print("ERRORI:\n  " + "\n  ".join(errori))
        sys.exit(1)

    eventi = sorted((n for n in nodi.values() if n["tipo"] == "evento"), key=lambda e: e["ordine"])
    if VISTA.exists():
        shutil.rmtree(VISTA)
    for cartella in list(TIPI) + ["capitoli"]:
        (VISTA / cartella).mkdir(parents=True)

    for i, n in nodi.items():
        o = [f"# {n['nome']}", "", f"`{i}` · {n['tipo']}" +
             (f" · capitoli: {', '.join(map(str, n['capitoli']))}" if n.get("capitoli") else "")]
        if n.get("alias"):
            o.append(f"\nAlias: {', '.join(n['alias'])}")
        o += ["", n.get("sintesi", "").strip(), ""]
        if n["tipo"] == "evento":
            o += [f"- **Capitolo**: [{n['capitolo']}](../capitoli/{n['capitolo']:02d}.md)",
                  f"- **Quando**: {n['quando']}",
                  f"- **In scena**: {'sì' if n.get('in_scena', True) else 'no (riferito / fuori scena)'}"]
            if n.get("dove"):
                o.append(f"- **Dove**: {link(nodi, n['dove'])}")
            o.append("- **Coinvolti**: " + ", ".join(link(nodi, x) for x in n.get("coinvolti", [])))
            prima = [link(nodi, x) for x in n.get("dopo", [])]
            poi = [link(nodi, e["id"]) for e in eventi if i in e.get("dopo", [])]
            o.append("- **Viene da**: " + (", ".join(prima) or "—"))
            o.append("- **Porta a**: " + (", ".join(poi) or "—"))
            o.append("")
        for titolo, chiave in (("Caratteristiche", "caratteristiche"), ("Fatti", "fatti"),
                               ("Cosa NON dice il testo", "non_detto"),
                               ("Punti aperti / da verificare", "aperti")):
            if n.get(chiave):
                o += [f"## {titolo}", ""]
                for x in n[chiave]:
                    o.append(f"- {x['testo']} {fmt_fonte(x['fonte']) if x.get('fonte') else ''}".rstrip())
                o.append("")
        if n.get("stato"):
            o += ["## Stato capitolo per capitolo", ""]
            for x in n["stato"]:
                o.append(f"- **Cap. {x['cap']}** — {x['testo']} {fmt_fonte(x['fonte']) if x.get('fonte') else ''}".rstrip())
            o.append("")
        usc = [a for a in archi if a["da"] == i and a["tipo"] not in ("coinvolge", "avviene in", "porta a")]
        ent = [a for a in archi if a["a"] == i and a["tipo"] not in ("coinvolge", "avviene in", "porta a")]
        if usc or ent:
            o += ["## Relazioni", ""]
            for a in usc:
                o.append(f"- → {a['tipo']} {link(nodi, a['a'])}" + (f" — {a['nota']}" if a["nota"] else "") +
                         (f" {fmt_fonte(a['fonte'])}" if a["fonte"] else ""))
            for a in ent:
                o.append(f"- ← {link(nodi, a['da'])} {a['tipo']} questa scheda" +
                         (f" — {a['nota']}" if a["nota"] else "") +
                         (f" {fmt_fonte(a['fonte'])}" if a["fonte"] else ""))
            o.append("")
        if n["tipo"] != "evento":
            miei = [e for e in eventi if i in e.get("coinvolti", []) or e.get("dove") == i]
            if miei:
                o += ["## Catena degli eventi", ""]
                for e in miei:
                    o.append(f"1. `{e['id']}` (cap. {e['capitolo']}, {e['quando']}) — {link(nodi, e['id'])}")
                o.append("")
        (VISTA / PLUR[n["tipo"]] / f"{i}.md").write_text("\n".join(o) + "\n", encoding="utf-8")

    for num, c in caps.items():
        ev = [e for e in eventi if e["capitolo"] == num]
        ids = {e["id"] for e in ev}
        o = [f"# Capitolo {num} — {c['titolo']}", "",
             f"File: `{c['file']}` · versione analizzata: {c['versione_analizzata']}", "",
             "## Catena degli eventi", "", "```mermaid", "flowchart TD"]
        for e in ev:
            o.append(f'  {e["id"]}["{e["id"]}<br/>{e["nome"]}"]')
        for e in ev:
            for p in e.get("dopo", []):
                if p not in ids:
                    o.append(f'  {p}(["{p} (cap. {nodi[p]["capitolo"]})"])')
                o.append(f"  {p} --> {e['id']}")
        o += ["```", ""]
        for e in ev:
            o.append(f"1. `{e['id']}` — {link(nodi, e['id'])} · {e['quando']}")
        o += ["", "## Schede toccate dal capitolo", ""]
        for tipo in ("personaggio", "organizzazione", "oggetto", "luogo", "concetto", "termine"):
            xs = [n for n in nodi.values() if n["tipo"] == tipo and num in n.get("capitoli", [])]
            if xs:
                o.append(f"- **{PLUR[tipo].capitalize()}**: " + ", ".join(link(nodi, n["id"]) for n in xs))
        (VISTA / "capitoli" / f"{num:02d}.md").write_text("\n".join(o) + "\n", encoding="utf-8")

    o = ["# Grafo del libro — indice", "",
         "Generato da `build_grafo.py`. Non modificare: le sorgenti sono in `schede/`.", "",
         "## Capitoli analizzati", ""]
    for num, c in caps.items():
        o.append(f"- [Cap. {num} — {c['titolo']}](vista/capitoli/{num:02d}.md) (v{c['versione_analizzata']})" +
                 (" — **analisi parziale**: solo i termini anticipati" if c.get("parziale") else ""))
    for tipo in ("personaggio", "organizzazione", "oggetto", "luogo", "concetto", "termine", "evento"):
        xs = [n for n in nodi.values() if n["tipo"] == tipo]
        xs.sort(key=lambda n: n.get("ordine", n["nome"].lower()) if tipo == "evento" else n["nome"].lower())
        o += ["", f"## {PLUR[tipo].capitalize()} ({len(xs)})", ""]
        for n in xs:
            o.append(f"- [{n['nome']}](vista/{PLUR[tipo]}/{n['id']}.md) — {n.get('sintesi', '').strip().splitlines()[0]}")
    aperti = [(n, x) for n in nodi.values() for x in n.get("aperti", [])]
    if aperti:
        o += ["", f"## Punti aperti ({len(aperti)})", ""]
        for n, x in aperti:
            o.append(f"- [{n['nome']}](vista/{PLUR[n['tipo']]}/{n['id']}.md): {x['testo']}")
    (ROOT / "INDICE.md").write_text("\n".join(o) + "\n", encoding="utf-8")

    (ROOT / "grafo.json").write_text(json.dumps({
        "nodi": [{"id": i, "tipo": n["tipo"], "nome": n["nome"], "capitoli": n.get("capitoli", [n.get("capitolo")])}
                 for i, n in nodi.items()],
        "archi": archi}, ensure_ascii=False, indent=1), encoding="utf-8")
    for a in avvisi:
        print("AVVISO:", a)
    print(f"OK: {len(nodi)} schede, {len(archi)} archi, {len(eventi)} eventi")


if __name__ == "__main__":
    main()
