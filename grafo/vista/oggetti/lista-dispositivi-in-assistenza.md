# Lista dei dispositivi in assistenza

`lista-dispositivi-in-assistenza` · oggetto · capitoli: 11, 12, 13

L'elenco aggiornato ogni giorno dall'assistenza tecnica, con le schede e le frasi dei clienti.

## Caratteristiche

- Aggiornata ogni giorno dai colleghi del dipartimento di assistenza tecnica *(cap. 11 r. 29)*
- Le schede riportano la frase esatta del cliente e le anomalie registrate (es. assenza dei log) *(cap. 11 r. 31)*
- Tiene traccia di tutto: numero di matricola, nome del tecnico, anni di note d'esito firmate *(cap. 12 r. 21, cap. 12 r. 29)*
- Si può cercare per matricola: restituisce tutte le righe dell'apparecchio, con stato finale («in attesa di ritiro», «ricondizionato, in magazzino, in attesa di vendita») *(cap. 13 r. 43)*
- È distinta dal registro interventi: dalla matricola Emma «risalì alla pratica nel registro interventi» *(cap. 13 r. 43)*

## Relazioni

- → aggiornata da [Divisione Assistenza Tecnica](../organizzazioni/divisione-assistenza-tecnica.md) *(cap. 11 r. 29)*
- ← [L'archivio delle anomalie di Emma](../oggetti/archivio-di-emma.md) costruito sulla questa scheda *(cap. 11 r. 29)*

## Catena degli eventi

1. `e11-0a` (cap. 11, giorni prima del cap. 11 (non quantificati)) — [Antefatto - il frigorifero che si rifiuta](../eventi/e11-0a.md)
1. `e11-05` (cap. 11, il pomeriggio) — [Emma aggiorna l'archivio delle anomalie - il frigorifero, gli smoothie](../eventi/e11-05.md)
1. `e12-02` (cap. 12, la stessa mattina) — [Emma scopre che il tecnico del televisore Voss era Tom](../eventi/e12-02.md)
1. `e12-03` (cap. 12, la stessa mattina) — [Due ipotesi - un investigatore con la casella di Tom, o Tom che indaga](../eventi/e12-03.md)
1. `e13-05` (cap. 13, la stessa mattina) — [Emma scopre le due volte di Tom](../eventi/e13-05.md)

