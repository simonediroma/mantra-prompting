#!/usr/bin/env python3
"""Revisione dei punti aperti (2026-11-15), su indicazione dell'autore.

Per ogni punto: V = incongruenza vera nel testo (resta in «aperti», a volte riformulata),
N = osservazione di lettura, non un errore (passa in «note»), X = sbagliato (tolto).
Eseguito una volta sola; resta come traccia delle decisioni.
"""
import json
from pathlib import Path

S = Path(__file__).resolve().parent / "schede"
D = {  # id: [azione per ogni punto, nell'ordine in cui compaiono], riformulazioni "V:testo"
 "anticipo-di-quindici-minuti": ["V:«Intoccabili come ogni mattina» (c9 r. 9), ma nelle due mattine dei cap. 4 e 5 Tom li ha spesi per telefonare alla signora Voss, arrivando una volta in ritardo (c5 r. 9). Il «come ogni mattina» va attenuato, o letto come proposito nato da quel ritardo."],
 "calendario": ["V:Il venerdì del cap. 16 (r. 15) fissa i cap. 12-14 di venerdì; a ritroso il cap. 9 è martedì e il ricondizionamento (cap. 6) lunedì. Dal martedì del secondo contatto (c3 r. 17) a un lunedì passano 20 o 27 giorni, non «poco più di tre settimane» (c6 r. 13, c16 r. 11).", "N"],
 "ciclo-diagnostico-14-minuti": ["X"],
 "digiuno-intermittente": ["X"],
 "indovinello-del-fondatore": ["N"],
 "ipotesi-canale-standby": ["N"],
 "ipotesi-ewatch": ["X", "N", "N"],
 "meccanismo-della-ripetizione": ["N", "N"],
 "porta-accostata": ["N", "N"],
 "procedura-standard": ["X"],
 "regole-sulla-posta": ["N", "N"],
 "sofisma-della-sarda-salata": ["N"],
 "casa-di-pete": ["N"],
 "la-mela-morsicata": ["N"],
 "laboratorio-di-tom": ["X"],
 "apparecchi-ordinari": ["N"],
 "archivio-artefatti": ["N", "N"],
 "archivio-di-emma": ["N", "N"],
 "avatar-di-emma": ["N"],
 "bilancia-marisa": ["N"],
 "canale-etv": ["N", "N"],
 "carrello-del-caffe": ["N"],
 "cartelli-di-tom": ["N", "N"],
 "cellulare-di-tom": ["N"],
 "disco-tango": ["N"],
 "edj": ["N"],
 "ewatch": ["N"],
 "foglio-io-sono-qui": ["V:Il foglio è «la sola prova al mondo, ormai» (c2 r. 41); nel cap. 3 lo diventa il quaderno («l'unica prova al mondo di ciò che aveva visto», c3 r. 13), mentre il foglio è ancora nel cassetto del laboratorio. Una delle due «uniche prove» va ridimensionata."],
 "frigorifero-anomalo": ["N"],
 "giradischi-di-tom": ["N"],
 "indirizzo-elab": ["V:«Quel contatto l'aveva scritto il sistema, anni prima» (c10 r. 23): ma il contatto è quello associato al video, generato 6 mesi prima (c9 r. 32), e l'archivio etichetta i contenuti da «un paio d'anni» (c9 r. 25). Se Emma intende che l'indirizzo di Elab è stato impostato anni fa come contatto predefinito, conviene dirlo."],
 "led-del-faretto": ["N"],
 "log-tv-caso-zero": ["V:La riga «compacting context» gli pare vista «una volta, mesi prima, su un altro apparecchio, in un altro contesto» (c1 r. 87); due righe dopo l'ha vista «decine di volte» sul giradischi (c1 r. 91). Le due frasi si contraddicono: una volta o decine, un altro apparecchio o il suo giradischi."],
 "log-tv-secondo-contatto": ["V:Nel cap. 19 (r. 39) Tom dice che l'ultima riga del log del televisore Voss era «compacting context»; nel cap. 3 (r. 19), quando lo apre, il testo dice solo che si interrompe «come il primo». Il lettore del cap. 3 non sa che la riga c'è: se serve come preparazione, va resa esplicita.", "X"],
 "mail-bluff-di-tom": ["N"],
 "organigramma": ["X"],
 "pannello-di-etv": ["X"],
 "post-del-fratello": ["N"],
 "quaderno-nero": ["X", "V:A fine cap. 3 Tom chiude il quaderno e spegne la lampada (c3 r. 39); il cap. 4 dice che «poco dopo» aver trascritto il numero era alla scrivania con il quaderno aperto a provare la scusa (c4 r. 9). L'ordine della serata va sistemato in uno dei due capitoli.", "X", "X"],
 "riepilogo-di-mezzanotte": ["N", "X"],
 "risposta-di-emma": ["X", "X"],
 "scatti-di-pete": ["N", "N"],
 "telecamera-di-sorveglianza": ["N", "N", "N"],
 "transcript-del-video": ["V:In un'ora prima di uscire (c9 r. 9-21) Tom carica il video, attende il verdetto, trascrive a mano tutto il parlato di quindici minuti e interroga tre servizi. La sola trascrizione parola per parola di quindici minuti richiede di norma più di un'ora: i tempi sono stretti."],
 "trascrizione-del-meeting": ["N", "N", "N"],
 "tritatutto": ["N"],
 "tv-secondo-contatto": ["V:Nella telefonata Tom pensa al reset come a «un evento di poche ore prima» (c4 r. 23), ma è avvenuto a fine turno del giorno prima (c3 r. 17) e la chiamata è del mattino dopo: quasi un giorno intero.", "X", "X", "X", "V:Lo stesso dato si chiama «numero di serie» nel cap. 6 (r. 9) e «numero di matricola» nel cap. 12 (r. 21) e nel cap. 13 (r. 43). Conviene un nome solo.", "N", "N", "V:«Pochi giorni dopo … la causale era diventata decesso cliente … Tre settimane più tardi l'apparecchio era tornato sul suo banco» (c14 r. 31): contate dal decesso, le tre settimane non tornano, perché dal reset al ricondizionamento passano in tutto «poco più di tre settimane» (c6 r. 13)."],
 "video-della-voss": ["N"],
 "video-yoga": ["N", "N", "N", "N"],
 "emma": ["N", "N", "N"],
 "pete": ["V:Pete ha firmato la sanzione «con il nome per esteso» (c17 r. 52), ma la firma riportata nel cap. 2 è «Pete, Supervisore» (c2 r. 23). O Pete è già il nome per esteso, o la firma del cap. 2 va allungata.", "X", "V:Per Pete la morte «stava nel registro dal giorno del ricondizionamento» (c18 r. 47); nel registro il decesso è annotato prima, pochi giorni dopo il rifiuto del ritiro (c6 r. 21). Pete, che «le date le guardava sempre prima delle parole», vedrebbe la data giusta."],
 "signora-voss": ["N", "N", "N", "X", "N", "N", "X"],
 "tecnico-turno-b": ["X"],
 "tom": ["X", "N", "X", "X", "X", "X", "X", "X", "X", "N"],
 "tommy": ["N"],
 "fattore-turno": ["X"],
 "hard-reset": ["V:Sul caso zero Tom esegue due volte la procedura standard, che comprende un reset software, e il televisore parla lo stesso (c1 r. 23); poi teme che «un reset qualunque» cancelli tutto (c1 r. 97). Conviene precisare che teme l'hard reset, l'unico che cancella (c6 r. 25)."],
 "modalita-presenza": ["N"],
}


def blocco(righe, chiave):
    i = next((k for k, r in enumerate(righe) if r.startswith(chiave + ":")), None)
    if i is None:
        return None, None
    j = i + 1
    while j < len(righe) and righe[j].startswith("  "):
        j += 1
    return i, j


conti = {"V": 0, "N": 0, "X": 0}
for id_, azioni in D.items():
    f = next(S.glob(f"*/{id_}.yaml"))
    righe = f.read_text(encoding="utf-8").splitlines()
    i, j = blocco(righe, "aperti")
    voci = righe[i + 1:j]
    assert len(voci) == len(azioni), (id_, len(voci), len(azioni))
    tieni, note = [], []
    for v, a in zip(voci, azioni):
        conti[a[0]] += 1
        if a.startswith("V:"):
            tieni.append("  - {testo: " + json.dumps(a[2:], ensure_ascii=False) + "}")
        elif a == "V":
            tieni.append(v)
        elif a == "N":
            note.append(v)
    nuovo = (["aperti:"] + tieni if tieni else []) + (["note:"] + note if note else [])
    righe[i:j] = nuovo
    f.write_text("\n".join(righe) + "\n", encoding="utf-8")
print(conti)
