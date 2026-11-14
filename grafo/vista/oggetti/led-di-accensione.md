# LED di accensione

`led-di-accensione` · oggetto · capitoli: 1, 3

Il LED dei televisori Meridian. Di norma lampeggia verde («sto pensando»); nei due televisori anomali è il canale dei messaggi in Morse.

## Caratteristiche

- Di norma lampeggia in un «innocuo verde sto pensando» *(cap. 1 r. 23)*
- Nel caso zero: fisso, spento, poi un pattern che non è nessuna sequenza diagnostica nota *(cap. 1 r. 23)*
- La presenza o assenza del «pattern anomalo sul LED» è un campo del quaderno *(cap. 3 r. 13)*

## Relazioni

- → trasmette in [Codice Morse](../concetti/codice-morse.md) *(cap. 1 r. 33)*
- ← [Televisore del primo contatto (caso zero)](../oggetti/tv-caso-zero.md) comunica tramite questa scheda *(cap. 1 r. 31)*
- ← [Televisore del secondo contatto](../oggetti/tv-secondo-contatto.md) comunica tramite questa scheda *(cap. 3 r. 23)*

## Catena degli eventi

1. `e01-01` (cap. 1, giorno del primo contatto, turno di pomeriggio (inverno, circa tre mesi prima del cap. 3)) — [Procedura standard due volte, checksum pulito, LED anomalo](../eventi/e01-01.md)
1. `e01-02` (cap. 1, stesso intervento) — [«C'è nessuno, oltre a me, in questa stanza?» → IO SONO QUI](../eventi/e01-02.md)
1. `e01-03` (cap. 1, stesso intervento, circa dieci minuti) — [L'interrogatorio del primo televisore](../eventi/e01-03.md)
1. `e03-04` (cap. 3, stesso intervento, nei minuti rimasti) — [«Ti senti solo?» → NO SONO QUI CON TE](../eventi/e03-04.md)

