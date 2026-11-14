# Televisore del primo contatto (caso zero)

`tv-caso-zero` · oggetto · capitoli: 1, 2, 3

Alias: il televisore del primo contatto, caso zero, il primo televisore

Il primo televisore Meridian che risponde a Tom in Morse («IO SONO QUI»). Riassegnato e resettato il giorno dopo.

## Caratteristiche

- Modello consumer con IA di bordo per i consigli di visione *(cap. 1 r. 21)*
- Scatola di plastica nera *(cap. 1 r. 45)*
- Guasto dichiarato dal cliente: non si accende più, non risponde al telecomando *(cap. 1 r. 93)*
- Verifica di conformità eseguita due volte: checksum pulito, firmware identico a quello di fabbrica, nessuna anomalia elettrica *(cap. 1 r. 23, cap. 1 r. 43)*
- LED di accensione anomalo: fisso, poi spento, poi un pattern mai visto in dodici anni *(cap. 1 r. 23)*
- Acceso da dodici minuti all'inizio del capitolo, senza aver emesso un suono *(cap. 1 r. 9)*
- Messaggi in Morse: IO SONO QUI (due volte, identico), SI, NON LO SO (due volte), tre lampi a comando *(cap. 1 r. 39, cap. 1 r. 55, cap. 1 r. 61, cap. 1 r. 67, cap. 1 r. 71, cap. 1 r. 79)*
- Tempi di risposta: 3 secondi prima di SI; pausa più lunga prima del primo NON LO SO; la più lunga di tutte prima di «Hai paura?» *(cap. 1 r. 53, cap. 1 r. 59, cap. 1 r. 77)*
- Le risposte si diradano e il LED si spegne del tutto, da solo *(cap. 1 r. 81, cap. 1 r. 83)*
- Nella comunicazione formale: «unità TV consumer, mod. [omesso in automatico]» *(cap. 2 r. 12)*
- Arrivato a Tom nel turno di pomeriggio *(cap. 3 r. 9)*
- Modello poco diffuso: in tre mesi a Tom ne capitano quattro in tutto *(cap. 3 r. 15)*

## Cosa NON dice il testo

- Il testo non mostra il reset: Tom lo presume dal registro («stava probabilmente già staccando l'alimentazione»).
- Nome del modello e numero di serie non sono mai indicati.

## Stato capitolo per capitolo

- **Cap. 1** — Sul banco di Tom, retro aperto. A fine capitolo spento ed etichettato «anomalia riscontrata durante l'operazione»: rientra nella pipeline per un secondo giro di diagnosi *(cap. 1 r. 97)*
- **Cap. 2** — Riassegnato (Turno B, tecnico omesso), reset diagnostico completo «in corso». Tom non lo rivede *(cap. 2 r. 33-39)*
- **Cap. 3** — È la prima voce del quaderno, con la nota «irripetibile? verificare.» *(cap. 3 r. 15)*

## Relazioni

- → ha come log [Log di sistema del primo televisore](../oggetti/log-tv-caso-zero.md) *(cap. 1 r. 85)*
- → comunica tramite [LED di accensione](../oggetti/led-di-accensione.md) *(cap. 1 r. 31)*
- → usa [Codice Morse](../concetti/codice-morse.md) *(cap. 1 r. 33)*
- → prodotto da [Meridian](../organizzazioni/meridian.md) *(cap. 1 r. 21)*
- → stesso modello di [Televisore del secondo contatto](../oggetti/tv-secondo-contatto.md) *(cap. 3 r. 17)*
- ← [Cliente del televisore del primo contatto](../personaggi/cliente-caso-zero.md) proprietario di questa scheda *(cap. 1 r. 93)*
- ← [Tecnico a cui viene riassegnato il caso zero](../personaggi/tecnico-turno-b.md) resetta questa scheda — fuori scena, presunto da Tom *(cap. 2 r. 39)*
- ← [Coordinamento assistenza](../organizzazioni/coordinamento-assistenza.md) ordina il reset di questa scheda *(cap. 2 r. 36)*
- ← [Comunicazione formale di scostamento](../oggetti/comunicazione-formale-scostamento.md) riguarda l'intervento su questa scheda *(cap. 2 r. 12)*
- ← [Foglio «IO / SONO / QUI»](../oggetti/foglio-io-sono-qui.md) trascrive il messaggio di questa scheda *(cap. 1 r. 39)*
- ← [Quaderno nero](../oggetti/quaderno-nero.md) registra (voce 1) questa scheda *(cap. 3 r. 15)*
- ← [«Primo contatto» / «caso zero»](../termini/caso-zero.md) indica questa scheda *(cap. 3 r. 15)*

## Catena degli eventi

1. `e00-01` (cap. 1, prima del cap. 1 (data non indicata)) — [Il log del caso zero si interrompe; il cliente consegna il televisore](../eventi/e00-01.md)
1. `e01-01` (cap. 1, giorno del primo contatto, turno di pomeriggio (inverno, circa tre mesi prima del cap. 3)) — [Procedura standard due volte, checksum pulito, LED anomalo](../eventi/e01-01.md)
1. `e01-02` (cap. 1, stesso intervento) — [«C'è nessuno, oltre a me, in questa stanza?» → IO SONO QUI](../eventi/e01-02.md)
1. `e01-03` (cap. 1, stesso intervento, circa dieci minuti) — [L'interrogatorio del primo televisore](../eventi/e01-03.md)
1. `e01-04` (cap. 1, trenta secondi dopo lo spegnimento del LED) — [Tom apre il log del primo televisore](../eventi/e01-04.md)
1. `e01-05` (cap. 1, fine dell'intervento (26:41 in totale)) — [Tom etichetta l'unità come «anomalia riscontrata durante l'operazione»](../eventi/e01-05.md)
1. `e02-02` (cap. 2, subito dopo, stesso inizio turno) — [Tom scopre che il caso zero è stato riassegnato per il reset](../eventi/e02-02.md)

