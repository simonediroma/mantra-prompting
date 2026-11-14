# Grafo del libro

Mappa di tutto ciò che esiste nel romanzo: personaggi, organizzazioni, oggetti, luoghi, concetti (regole, procedure, abitudini), termini (il glossario: parole a cui il libro dà un significato preciso) ed eventi, collegati tra loro.

**Regola unica: nelle schede entra solo ciò che è scritto nei capitoli**, con capitolo e riga (`c3:19` = cap. 3, riga 19 del file). Niente da outline, book-memory o memoria. Ciò che il testo *non* dice va nella sezione `non_detto`; dubbi e incongruenze in `aperti`.

## Come si usa

- Da leggere: [INDICE.md](INDICE.md) → `vista/` (schede con link, backlink e catena degli eventi di ogni scheda; `vista/capitoli/` ha il diagramma della catena per capitolo).
- Da modificare: solo `schede/<tipo>/<id>.yaml`, poi `python3 grafo/build_grafo.py`.
- Lo script si ferma se una scheda cita un id inesistente o una riga fuori dal capitolo, e avvisa se un capitolo ha cambiato versione dopo l'analisi (`capitoli.yaml`): quelle schede vanno riverificate.

## Campi di una scheda

`nome`, `alias`, `capitoli`, `sintesi`, `caratteristiche` (testo + fonte), `stato` (per capitolo), `non_detto`, `aperti`, `relazioni` (verso, tipo, nota, fonte).
Eventi: `capitolo`, `ordine`, `quando`, `dove`, `in_scena`, `coinvolti`, `dopo` (da quali eventi discende), `fatti`.

## Avanzamento

Si procede un capitolo alla volta: leggere il capitolo, aggiornare le schede esistenti, crearne di nuove, aggiungere gli eventi, rigenerare. Capitoli fatti: vedi `capitoli.yaml`.
